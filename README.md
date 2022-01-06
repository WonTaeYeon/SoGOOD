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

### Introduction   
- 허버트 윌리엄 하인리히는 <산업재해 예방 : 과학적 접근>이라는 책에서 1명의 사망 사고 있기전에 동일한 원인의 부상 사고 29건, 경미하거나 사고가 일어날뻔한 경우가 300건 있다고 통계학적인 상관관계를 밝혀냄
- 하인리히 법칙과 유사하게 우리나라 교통 관련 연구원에서 발표한 자료에서도 교통사고로 인한 사망 사고 1회가 일어나기전에 30~40회 정도 가벼운 사고가 있었고, 약 300건 이상의 교통 법규 위반 사례가 적발되었다고 함
- 즉, 유사한 교통 법규 위반 사례가 많아 질 수록 경미한 사고부터 대형 사고가 발생하는 횟수도 늘어날 확률이 높음
- 본 프로젝트는 하인리히 법칙을 역이용하여 사고로 이어지는 운전 패턴과 상황을 학습한 딥 러닝으로 사용자에게 알려주어 위험도 높은 운전 빈도를 낮춰 사고 방지에 기여하는 것이 목표
- 사고가 날 수도 있는 혹은 사고가 난 블랙박스 영상을 학습으로하여 위험도를 Normal, Waring, Danger로 사용자에게 경고할 수 있도록 함      

### Dataset   
- DoTA(Detection of Traffic Anomaly) Dataset을 이용
    - 해당 데이터는 정상적이지 않은 교통 상황 영상이 4,667개 포함되어 있음
- DoTA 데이터 중에서 발생하는 블랙박스 영상 약 2,000개 이상에서 200,000장이 넘는 프레임을 학습과 검증 및 테스트에 사용
- 프레임 별로 나눠 위험도 단계를 3개로 Labeling하여 사용
- Dataset에서 랜덤하게 10 프레임을 뽑아 전처리를 통해 학습과 검증에 사용

### Architectures
- 모델은 3D-Resnet 기반으로한 3D-CNN을 사용함
    - 3D Convloution를 이용하여 공간 정보와 프레이 간의 시간적 연결을 연산하여 특징을 추출
    - Resnet-34를 기반으로 3D-Resnet을 구성함
    - Kinetics 데이터로 사전 학습된 딥 러닝 모델로 전이 학습하여 성능을 향상 시켰음
- 입력으로는 224x224 사이즈로 된 10 프레임의 RGB 영상을 입력으로 사용
- 결과로는 각 클래스에 대한 수치가 나오고 제일 수치가 높은 클래스를 위험도로 사용함
![pic_1](https://user-images.githubusercontent.com/34120950/148449839-c803df6b-7e32-4207-b5fb-ad5ba763d2ae.png)

# Guide   
  * ## Train
   
      !python -u train.py --train_list {train path} --val_list {test_path} --n_classes 3 --batch_size 1 --sample_size 224 --lr 0.001 --epochs {epoch}
     
  * ## Test
   
      !python -u .\video_test.py --n_classes 3 --batch_size 1 --sample_size 224 --model {model_path} --testdata {data_path} --visuable {bool} --video_name {video_name}
  
     
  * ## Test Result
  　　　 ![Test_Result_1](https://user-images.githubusercontent.com/34120950/148389164-f04d34d9-3795-4208-b44d-c0b64e3f92f9.gif)
 

