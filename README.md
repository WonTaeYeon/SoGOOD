# SoGOOD
[멋사x쏘카]해커톤

Project : SoGOOD

TEAM :
  강태혁
  김현진
  박성민
  원태연 - 리더
  장주찬
  
  Train :
    python -u train.py --train_list {train path} --val_list {test_path} --n_classes 3 --batch_size 1 --sample_size 224 --lr 0.001 --epochs {epoch}
    
  Test :
    python -u .\video_test.py --n_classes 3 --batch_size 1 --sample_size 224 --model {model_path} --testdata {data_path} --visuable {bool} --video_name {video_name}
