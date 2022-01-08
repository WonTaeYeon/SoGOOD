import torch
from torch import nn
from torch.autograd import Variable
from spatial_transforms import (Compose, Normalize, Scale, CenterCrop, CornerCrop, MultiScaleCornerCrop,
                                MultiScaleRandomCrop, RandomHorizontalFlip, ToTensor)
from temporal_transforms import LoopPadding, TemporalRandomCrop
import numpy as np
import os
import json
import glob
import cv2
from model import generate_model
from opts import parse_opts
from mean import get_mean
from PIL import Image

def pil_loader(path):
    with open(path, 'rb') as f:
        with Image.open(f) as img:
            return img.convert('RGB')

def load_imgs(img):
    spatial_transform = Compose([Scale(opt.sample_size),
                                 CenterCrop(opt.sample_size),
                                 ToTensor(1),
                                 Normalize(opt.mean, [1, 1, 1])])
    return spatial_transform(pil_loader(img))

def eval_drive(videos, model):
    inputs = torch.stack(videos, 0).permute(1, 0, 2, 3)
    model.eval()
    with torch.no_grad():
        inputs =  Variable(inputs)
    outputs = model(inputs.unsqueeze(dim=0))
    _, top = torch.topk(outputs, 1, dim=1)
    return np.squeeze(top.cpu().numpy())

def take_img(img, top, opt):
    v_img = cv2.imread(img)
    
    text = ["Normal", "Warning", "Danger"]
    color = [(0,255,0), (255, 0, 0), (0, 0, 255)]
    
    cv2.putText(v_img, text[top], (10,30), cv2.FONT_HERSHEY_COMPLEX, 1, color[top], 2)
    
    if opt.visuable:
        cv2.imshow("test", v_img)
        k = cv2.waitKey(1)
        if k == 27: # esc key
            cv2.destroyAllWindow()
        
    return v_img

def test(model, opt):
    imgs = sorted((glob.glob(opt.testdata+"/*")))
    videos = []
    top = 0
    if opt.video_name:
        fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X') 
        out = cv2.VideoWriter(opt.video_name, fcc, opt.sample_duration, (1280, 720))
    for img in imgs:
        videos.append(load_imgs(img))
        if len(videos) == opt.sample_duration:
            top = eval_drive(videos, model)
            videos.pop(0)
            w_img = take_img(img, top, opt)
            if opt.video_name:
                out.write(w_img)
    if opt.video_name:
        out.release()
        
if __name__ == '__main__':
    opt = parse_opts()
    opt.mean = get_mean()
    opt.arch = '{}-{}'.format(opt.model_name, opt.model_depth)
    opt.sample_duration = 10
    
    model, _ = generate_model(opt)
    model = nn.DataParallel(model).cuda()
    print('loading model {}'.format(opt.model))
    model_data = torch.load(opt.model)
    assert opt.arch == model_data['arch']
    model.load_state_dict(model_data['state_dict'])
    model.eval()
    
    test(model, opt)

