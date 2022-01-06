# [멋사x쏘카]해커톤

# TEAM : SoGOOD
![SoGOOD](https://user-images.githubusercontent.com/34120950/148390331-6f4c18be-c0ce-4a91-93c4-5cdedfc81945.png)   
* 선한 운전력 전파를 위해!

## Project : SoGOOD   
  * 딥 러닝 기반 운전 위험도를 평가하여 안전한 운전을 유도하여 사고 방지에 기여하는 것이 목표

### TEAM :

  - 강태혁
  - 김현진
  - 박성민
  - 원태연 - 리더
  - 장주찬

# Guide   
  * ## Train   
     
    !python -u train.py --train_list {train path} --val_list {test_path} --n_classes 3 --batch_size 1 --sample_size 224 --lr 0.001 --epochs {epoch}   
    
  * ## Test   
     
    !python -u .\video_test.py --n_classes 3 --batch_size 1 --sample_size 224 --model {model_path} --testdata {data_path} --visuable {bool} --video_name {video_name}   
    
       
   * ## Test Result   
   ![Test_Result_1](https://user-images.githubusercontent.com/34120950/148389164-f04d34d9-3795-4208-b44d-c0b64e3f92f9.gif)
