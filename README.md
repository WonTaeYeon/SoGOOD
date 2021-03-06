# [멋사x쏘카]해커톤

# TEAM : SoGOOD
![SoGOOD](https://user-images.githubusercontent.com/34120950/148390331-6f4c18be-c0ce-4a91-93c4-5cdedfc81945.png)   
* 선한 운전력 전파를 위한 작은 발자국!

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
- 사고가 날 수도 있는 혹은 사고가 난 블랙박스 영상을 학습으로하여 위험도를 Normal, Warning, Danger로 사용자에게 경고할 수 있도록 함      

### Dataset   
- DoTA(Detection of Traffic Anomaly) Dataset을 이용
    - 해당 데이터는 정상적이지 않은 교통 상황 영상이 4,667개 포함되어 있음
- DoTA 데이터 중에서 발생하는 블랙박스 영상 약 300개 이상에서 3,000장이 넘는 프레임을 학습과 검증 및 테스트에 사용
- 프레임 별로 나눠 위험도 단계를 3개로 Labeling하여 사용
- Dataset에서 랜덤하게 10 프레임을 뽑아 전처리를 통해 학습과 검증에 사용
- [Label Download](https://drive.google.com/uc?export=download&id=10Ouw21vsdNEWB8eMOzmoFM4f63XTNz6x)
- [Dataset Download](https://drive.google.com/uc?export=download&id=10TTGd-dGOmHz-SnQG5rSA5-5OD6dfi1d)

### Architectures
- 모델은 3D-Resnet 기반으로한 3D-CNN을 사용함
    - 3D Convloution를 이용하여 공간 정보와 프레이 간의 시간적 연결을 연산하여 특징을 추출
    - Resnet-101을 기반으로 3D-Resnet을 구성함
    - Kinetics 데이터로 사전 학습된 딥 러닝 모델로 전이 학습하여 성능을 향상 시켰음
- 입력으로는 224x224 사이즈로 된 10 프레임의 RGB 영상을 입력으로 사용
- 결과로는 각 클래스에 대한 수치가 나오고 제일 수치가 높은 클래스를 위험도로 사용함   

![pic_1](https://user-images.githubusercontent.com/34120950/148449839-c803df6b-7e32-4207-b5fb-ad5ba763d2ae.png)
      
      
   <details>
   <summary>모델 구조 자세히 보기(클릭)</summary>
   <div markdown="1">   
      

| Layer (type) |              Output Shape |        Param #|
|:---|:---:|---:|
|            Conv3d-1      |[1, 64, 10, 112, 112]|          65,856|
|       BatchNorm3d-2      |[1, 64, 10, 112, 112]|             128|
|              ReLU-3      |[1, 64, 10, 112, 112]|               0|
|         MaxPool3d-4         |[1, 64, 5, 56, 56]|               0|
|            Conv3d-5         |[1, 64, 5, 56, 56]|           4,096|
|       BatchNorm3d-6         |[1, 64, 5, 56, 56]|             128|
|              ReLU-7         |[1, 64, 5, 56, 56]|               0|
|            Conv3d-8         |[1, 64, 5, 56, 56]|         110,592|
|       BatchNorm3d-9         |[1, 64, 5, 56, 56]|             128|
|             ReLU-10         |[1, 64, 5, 56, 56]|               0|
|           Conv3d-11        |[1, 256, 5, 56, 56]|          16,384|
|      BatchNorm3d-12        |[1, 256, 5, 56, 56]|             512|
|             ReLU-13        |[1, 256, 5, 56, 56]|               0|
|       Bottleneck-14        |[1, 256, 5, 56, 56]|               0|
|           Conv3d-15         |[1, 64, 5, 56, 56]|          16,384|
|      BatchNorm3d-16         |[1, 64, 5, 56, 56]|             128|
|             ReLU-17         |[1, 64, 5, 56, 56]|               0|
|           Conv3d-18         |[1, 64, 5, 56, 56]|         110,592|
|      BatchNorm3d-19         |[1, 64, 5, 56, 56]|             128|
|             ReLU-20         |[1, 64, 5, 56, 56]|               0|
|           Conv3d-21        |[1, 256, 5, 56, 56]|          16,384|
|      BatchNorm3d-22        |[1, 256, 5, 56, 56]|             512|
|             ReLU-23        |[1, 256, 5, 56, 56]|               0|
|       Bottleneck-24        |[1, 256, 5, 56, 56]|               0|
|           Conv3d-25         |[1, 64, 5, 56, 56]|          16,384|
|      BatchNorm3d-26         |[1, 64, 5, 56, 56]|             128|
|             ReLU-27         |[1, 64, 5, 56, 56]|               0|
|           Conv3d-28         |[1, 64, 5, 56, 56]|         110,592|
|      BatchNorm3d-29         |[1, 64, 5, 56, 56]|             128|
|             ReLU-30         |[1, 64, 5, 56, 56]|               0|
|           Conv3d-31        |[1, 256, 5, 56, 56]|          16,384|
|      BatchNorm3d-32        |[1, 256, 5, 56, 56]|             512|
|             ReLU-33        |[1, 256, 5, 56, 56]|               0|
|       Bottleneck-34        |[1, 256, 5, 56, 56]|               0|
|           Conv3d-35        |[1, 128, 5, 56, 56]|          32,768|
|      BatchNorm3d-36        |[1, 128, 5, 56, 56]|             256|
|             ReLU-37        |[1, 128, 5, 56, 56]|               0|
|           Conv3d-38        |[1, 128, 3, 28, 28]|         442,368|
|      BatchNorm3d-39        |[1, 128, 3, 28, 28]|             256|
|             ReLU-40        |[1, 128, 3, 28, 28]|               0|
|           Conv3d-41        |[1, 512, 3, 28, 28]|          65,536|
|      BatchNorm3d-42        |[1, 512, 3, 28, 28]|           1,024|
|             ReLU-43        |[1, 512, 3, 28, 28]|               0|
|       Bottleneck-44        |[1, 512, 3, 28, 28]|               0|
|           Conv3d-45        |[1, 128, 3, 28, 28]|          65,536|
|      BatchNorm3d-46        |[1, 128, 3, 28, 28]|             256|
|             ReLU-47        |[1, 128, 3, 28, 28]|               0|
|           Conv3d-48        |[1, 128, 3, 28, 28]|         442,368|
|      BatchNorm3d-49        |[1, 128, 3, 28, 28]|             256|
|             ReLU-50        |[1, 128, 3, 28, 28]|               0|
|           Conv3d-51        |[1, 512, 3, 28, 28]|          65,536|
|      BatchNorm3d-52        |[1, 512, 3, 28, 28]|           1,024|
|             ReLU-53        |[1, 512, 3, 28, 28]|               0|
|       Bottleneck-54        |[1, 512, 3, 28, 28]|               0|
|           Conv3d-55        |[1, 128, 3, 28, 28]|          65,536|
|      BatchNorm3d-56        |[1, 128, 3, 28, 28]|             256|
|             ReLU-57        |[1, 128, 3, 28, 28]|               0|
|           Conv3d-58        |[1, 128, 3, 28, 28]|         442,368|
|      BatchNorm3d-59        |[1, 128, 3, 28, 28]|             256|
|             ReLU-60        |[1, 128, 3, 28, 28]|               0|
|           Conv3d-61        |[1, 512, 3, 28, 28]|          65,536|
|      BatchNorm3d-62        |[1, 512, 3, 28, 28]|           1,024|
|             ReLU-63        |[1, 512, 3, 28, 28]|               0|
|       Bottleneck-64        |[1, 512, 3, 28, 28]|               0|
|           Conv3d-65        |[1, 128, 3, 28, 28]|          65,536|
|      BatchNorm3d-66        |[1, 128, 3, 28, 28]|             256|
|             ReLU-67        |[1, 128, 3, 28, 28]|               0|
|           Conv3d-68        |[1, 128, 3, 28, 28]|         442,368|
|      BatchNorm3d-69        |[1, 128, 3, 28, 28]|             256|
|             ReLU-70        |[1, 128, 3, 28, 28]|               0|
|           Conv3d-71        |[1, 512, 3, 28, 28]|          65,536|
|      BatchNorm3d-72        |[1, 512, 3, 28, 28]|           1,024|
|             ReLU-73        |[1, 512, 3, 28, 28]|               0|
|       Bottleneck-74        |[1, 512, 3, 28, 28]|               0|
|           Conv3d-75        |[1, 256, 3, 28, 28]|         131,072|
|      BatchNorm3d-76        |[1, 256, 3, 28, 28]|             512|
|             ReLU-77        |[1, 256, 3, 28, 28]|               0|
|           Conv3d-78        |[1, 256, 2, 14, 14]|       1,769,472|
|      BatchNorm3d-79        |[1, 256, 2, 14, 14]|             512|
|             ReLU-80        |[1, 256, 2, 14, 14]|               0|
|           Conv3d-81       |[1, 1024, 2, 14, 14]|         262,144|
|      BatchNorm3d-82       |[1, 1024, 2, 14, 14]|           2,048|
|             ReLU-83       |[1, 1024, 2, 14, 14]|               0|
|       Bottleneck-84       |[1, 1024, 2, 14, 14]|               0|
|           Conv3d-85        |[1, 256, 2, 14, 14]|         262,144|
|      BatchNorm3d-86        |[1, 256, 2, 14, 14]|             512|
|             ReLU-87        |[1, 256, 2, 14, 14]|               0|
|           Conv3d-88        |[1, 256, 2, 14, 14]|       1,769,472|
|      BatchNorm3d-89        |[1, 256, 2, 14, 14]|             512|
|             ReLU-90        |[1, 256, 2, 14, 14]|               0|
|           Conv3d-91       |[1, 1024, 2, 14, 14]|         262,144|
|      BatchNorm3d-92       |[1, 1024, 2, 14, 14]|           2,048|
|             ReLU-93       |[1, 1024, 2, 14, 14]|               0|
|       Bottleneck-94       |[1, 1024, 2, 14, 14]|               0|
|           Conv3d-95        |[1, 256, 2, 14, 14]|         262,144|
|      BatchNorm3d-96        |[1, 256, 2, 14, 14]|             512|
|             ReLU-97        |[1, 256, 2, 14, 14]|               0|
|           Conv3d-98        |[1, 256, 2, 14, 14]|       1,769,472|
|      BatchNorm3d-99        |[1, 256, 2, 14, 14]|             512|
|            ReLU-100        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-101       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-102       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-103       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-104       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-105        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-106        |[1, 256, 2, 14, 14]|             512|
|            ReLU-107        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-108        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-109        |[1, 256, 2, 14, 14]|             512|
|            ReLU-110        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-111       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-112       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-113       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-114       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-115        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-116        |[1, 256, 2, 14, 14]|             512|
|            ReLU-117        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-118        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-119        |[1, 256, 2, 14, 14]|             512|
|            ReLU-120        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-121       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-122       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-123       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-124       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-125        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-126        |[1, 256, 2, 14, 14]|             512|
|            ReLU-127        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-128        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-129        |[1, 256, 2, 14, 14]|             512|
|            ReLU-130        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-131       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-132       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-133       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-134       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-135        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-136        |[1, 256, 2, 14, 14]|             512|
|            ReLU-137        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-138        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-139        |[1, 256, 2, 14, 14]|             512|
|            ReLU-140        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-141       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-142       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-143       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-144       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-145        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-146        |[1, 256, 2, 14, 14]|             512|
|            ReLU-147        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-148        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-149        |[1, 256, 2, 14, 14]|             512|
|            ReLU-150        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-151       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-152       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-153       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-154       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-155        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-156        |[1, 256, 2, 14, 14]|             512|
|            ReLU-157        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-158        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-159        |[1, 256, 2, 14, 14]|             512|
|            ReLU-160        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-161       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-162       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-163       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-164       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-165        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-166        |[1, 256, 2, 14, 14]|             512|
|            ReLU-167        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-168        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-169        |[1, 256, 2, 14, 14]|             512|
|            ReLU-170        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-171       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-172       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-173       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-174       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-175        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-176        |[1, 256, 2, 14, 14]|             512|
|            ReLU-177        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-178        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-179        |[1, 256, 2, 14, 14]|             512|
|            ReLU-180        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-181       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-182       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-183       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-184       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-185        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-186        |[1, 256, 2, 14, 14]|             512|
|            ReLU-187        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-188        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-189        |[1, 256, 2, 14, 14]|             512|
|            ReLU-190        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-191       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-192       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-193       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-194       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-195        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-196        |[1, 256, 2, 14, 14]|             512|
|            ReLU-197        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-198        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-199        |[1, 256, 2, 14, 14]|             512|
|            ReLU-200        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-201       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-202       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-203       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-204       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-205        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-206        |[1, 256, 2, 14, 14]|             512|
|            ReLU-207        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-208        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-209        |[1, 256, 2, 14, 14]|             512|
|            ReLU-210        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-211       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-212       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-213       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-214       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-215        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-216        |[1, 256, 2, 14, 14]|             512|
|            ReLU-217        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-218        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-219        |[1, 256, 2, 14, 14]|             512|
|            ReLU-220        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-221       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-222       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-223       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-224       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-225        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-226        |[1, 256, 2, 14, 14]|             512|
|            ReLU-227        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-228        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-229        |[1, 256, 2, 14, 14]|             512|
|            ReLU-230        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-231       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-232       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-233       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-234       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-235        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-236        |[1, 256, 2, 14, 14]|             512|
|            ReLU-237        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-238        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-239        |[1, 256, 2, 14, 14]|             512|
|            ReLU-240        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-241       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-242       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-243       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-244       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-245        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-246        |[1, 256, 2, 14, 14]|             512|
|            ReLU-247        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-248        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-249        |[1, 256, 2, 14, 14]|             512|
|            ReLU-250        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-251       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-252       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-253       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-254       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-255        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-256        |[1, 256, 2, 14, 14]|             512|
|            ReLU-257        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-258        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-259        |[1, 256, 2, 14, 14]|             512|
|            ReLU-260        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-261       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-262       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-263       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-264       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-265        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-266        |[1, 256, 2, 14, 14]|             512|
|            ReLU-267        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-268        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-269        |[1, 256, 2, 14, 14]|             512|
|            ReLU-270        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-271       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-272       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-273       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-274       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-275        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-276        |[1, 256, 2, 14, 14]|             512|
|            ReLU-277        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-278        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-279        |[1, 256, 2, 14, 14]|             512|
|            ReLU-280        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-281       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-282       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-283       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-284       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-285        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-286        |[1, 256, 2, 14, 14]|             512|
|            ReLU-287        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-288        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-289        |[1, 256, 2, 14, 14]|             512|
|            ReLU-290        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-291       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-292       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-293       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-294       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-295        |[1, 256, 2, 14, 14]|         262,144|
|     BatchNorm3d-296        |[1, 256, 2, 14, 14]|             512|
|            ReLU-297        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-298        |[1, 256, 2, 14, 14]|       1,769,472|
|     BatchNorm3d-299        |[1, 256, 2, 14, 14]|             512|
|            ReLU-300        |[1, 256, 2, 14, 14]|               0|
|          Conv3d-301       |[1, 1024, 2, 14, 14]|         262,144|
|     BatchNorm3d-302       |[1, 1024, 2, 14, 14]|           2,048|
|            ReLU-303       |[1, 1024, 2, 14, 14]|               0|
|      Bottleneck-304       |[1, 1024, 2, 14, 14]|               0|
|          Conv3d-305        |[1, 512, 2, 14, 14]|         524,288|
|     BatchNorm3d-306        |[1, 512, 2, 14, 14]|           1,024|
|            ReLU-307        |[1, 512, 2, 14, 14]|               0|
|          Conv3d-308          |[1, 512, 1, 7, 7]|       7,077,888|
|     BatchNorm3d-309          |[1, 512, 1, 7, 7]|           1,024|
|            ReLU-310          |[1, 512, 1, 7, 7]|               0|
|          Conv3d-311         |[1, 2048, 1, 7, 7]|       1,048,576|
|     BatchNorm3d-312         |[1, 2048, 1, 7, 7]|           4,096|
|            ReLU-313         |[1, 2048, 1, 7, 7]|               0|
|      Bottleneck-314         |[1, 2048, 1, 7, 7]|               0|
|          Conv3d-315          |[1, 512, 1, 7, 7]|       1,048,576|
|     BatchNorm3d-316          |[1, 512, 1, 7, 7]|           1,024|
|            ReLU-317          |[1, 512, 1, 7, 7]|               0|
|          Conv3d-318          |[1, 512, 1, 7, 7]|       7,077,888|
|     BatchNorm3d-319          |[1, 512, 1, 7, 7]|           1,024|
|            ReLU-320          |[1, 512, 1, 7, 7]|               0|
|          Conv3d-321         |[1, 2048, 1, 7, 7]|       1,048,576|
|     BatchNorm3d-322         |[1, 2048, 1, 7, 7]|           4,096|
|            ReLU-323         |[1, 2048, 1, 7, 7]|               0|
|      Bottleneck-324         |[1, 2048, 1, 7, 7]|               0|
|          Conv3d-325          |[1, 512, 1, 7, 7]|       1,048,576|
|     BatchNorm3d-326          |[1, 512, 1, 7, 7]|           1,024|
|            ReLU-327          |[1, 512, 1, 7, 7]|               0|
|          Conv3d-328          |[1, 512, 1, 7, 7]|       7,077,888|
|     BatchNorm3d-329          |[1, 512, 1, 7, 7]|           1,024|
|            ReLU-330          |[1, 512, 1, 7, 7]|               0|
|          Conv3d-331         |[1, 2048, 1, 7, 7]|       1,048,576|
|     BatchNorm3d-332         |[1, 2048, 1, 7, 7]|           4,096|
|            ReLU-333         |[1, 2048, 1, 7, 7]|               0|
|      Bottleneck-334         |[1, 2048, 1, 7, 7]|               0|
|       AvgPool3d-335         |[1, 2048, 1, 1, 1]|               0|
|          Linear-336                     |[1, 3]|           6,147|
|          ResNet-337                     |[1, 3]|               0|
|  Total params: |82,474,691|
|  Trainable params: |82,474,691|
|  Non-trainable params: |0|

 </div>
   </details><br/>    
  


### Conclusion   
  
  #### 결과  

  1. 딥 러닝으로 학습을 통해 학습 시 사용하지 않은 검증 데이터에서 약 66%에 달하는 성능을 보임
  2. 테스트를 통해서 연속된 영상에서도 위험도를 알려줄 수 있음을 확인함  
  
  - [Model Download](https://drive.google.com/uc?export=download&id=1qiJ4RwOIegiL45t8wqyT8F5UbR2rQnaL)

  #### 기대효과  

  1. 해당 딥 러닝 모델과 유튜브 크롤링을 통해 더 많은 위험도 평가 데이터 수집 가능
  2. 추후 해당 딥 러닝 모델을 이용해 Feature Extraction하여 위험도에 영향을 주는 특징들 추출하여 새로운 딥 러닝 모델로 사용자 경고 시스템이나 자율 주행 연구에 기여 기대  
   
# Guide   
  * ## Quick install dependencies   
    
    ```
    pip install -r requirements.txt
    ```

  * ## Train
   
    ```   
    python -u train.py --train_list {train path} --val_list {test_path} --n_classes 3 --batch_size {batch_size} --sample_size 224 --lr 0.001 --epochs {epoch} --resume {pretrained_model_path} --snapshot_pref {saved_model_path}
    ``` 
  
  
  * ## Test
   
    ```
    python -u .\video_test.py --n_classes 3 --batch_size 1 --sample_size 224 --model {model_path} --testdata {data_path} --visuable {bool} --video_name {video_name}
    ```   

  * ## Test Result
  　　　 ![Test_Result](https://user-images.githubusercontent.com/34120950/148645456-d122e5c2-7b6f-4b78-8d2c-e462d4959d21.gif)

# References 
1. KATAOKA, Hirokatsu, et al. Would mega-scale datasets further enhance spatiotemporal 3D CNNs?. arXiv preprint arXiv:2004.04968, 2020.   
2. HARA, Kensho; KATAOKA, Hirokatsu; SATOH, Yutaka. Can spatiotemporal 3d cnns retrace the history of 2d cnns and imagenet?. In: Proceedings of the IEEE conference on Computer Vision and Pattern Recognition. 2018. p. 6546-6555.   
3. YAO, Yu, et al. Unsupervised traffic accident detection in first-person videos. In: 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2019. p. 273-280.   

