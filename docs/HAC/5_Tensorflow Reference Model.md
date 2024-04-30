

# Tensorflow Reference Model 


**Tensorflow Reference Model (이하 TF RM) 이란?**

Moreh framework에서 학습, 추론이 가능한 Tensorflow 딥러닝 모델을 의미합니다. 정기적으로 프레임워크와 함께 배포되며 Moreh 솔루션에서 딥러닝 학습에 필수적인 단계들을 수행할 수 있는 약 15종의 모델을 다운로드할 수 있습니다.
따라서 사용자는 TF RM을 활용하여 직접 코딩하지 않아도 바로 학습, 추론을 수행할 수 있습니다. 


TensorFlow 가상 환경
처음 VM 생성 시 기본으로 `tensorflow` 이름의 Tensorflow용 conda 가상환경이 존재합니다.
Tensorflow conda 환경이 없는 사용자 분들은 아래와 같은 방법으로 TensorFlow를 위한 가상환경을 생성하시기 바랍니다.


## 1. Tensorflow RM 코드 다운로드

`get-reference-model` 명령어 한 줄로 다양한 Reference Model(이하 RM) Code를 얻게 됩니다.

```bash
//Resnet 모델 다운로드 예시
ubuntu@vm:~$ get-reference-model --tensorflow resnet
```
위와 같은 명령어 실행 시 ResNet에 대한 RM Code 설치 파일 및 샘플 데이터을 다운로드하게 되며, 동시에 해당 설치 파일을 실행시켜 실행환경을 세팅해줍니다. 명령어 실행 완료 시 모델명에 따른 폴더가 생성이 되며 해당 폴더로 들어가 아래 명령어로 바로 모델을 실행(학습)시킬 수 있습니다.

```bash
# 학습 모델 폴더로 이동
ubuntu@vm:~$ cd resnet

# 학습 모델 실행
ubuntu@vm:~$ python train.py
```

## 2. RM 옵션 값 확인하기

현재 `get-reference-model`에서 지원하는 옵션 값들을 보고 싶으시다면, 아무런 옵션 값을 주지 않고 실행하거나, `-h`옵션을 주면 보실 수 있습니다.
```bash
ubuntu@vm:~$ get-reference-model -h

Usage: get-reference-model [-h|--help] [--download-only] [--download-dir] [-s|--show] (MODEL_NAME)
Example: get-reference-model resnet

Avaiable options:
-h, --help           Print help and exit
-s, --show           Print the available list of models
--download-only	     Download the model shell script file without running
--download-dir       Set the installation path of a model default path: /home/ubuntu
--tensorflow         Set all option towards tensorflow reference model
                     ex) get-reference-model --tensorflow --show
                     ex) get-reference-model --tensorflow bert

```
## 3. 모델 학습 시작하기
홈 디렉터리 아래의 해당 모델 디렉터리로 이동한 다음 train.py 스크립트를 실행하여 모델 학습을 시작할 수 있습니다.

```bash
(tensorflow) ubuntu@vm:~$ cd ~/resnet
(tensorflow) ubuntu@vm:~/resnet$ python train.py --train_batch_size 32
...
[info] Requesting resources for KT AI Accelerator from the server...
[info] Initializing the worker daemon for KT AI Accelerator...
[info] [1/1] Connecting to resources on the server (192.168.00.00:00000)...
[info] Establishing links to the resources...
[info] KT AI Accelerator is ready to use.
...
| INFO | moreh_controller.py:_train_n_steps:474 TRAIN_STEP | Iteration : 100/69300 | Loss : 5.113 | Throughput : 462.375 samples/s | Duration : 83.049 s | Estimated Time Remaining : 22063.482 s
....
```

### Hyperparameter 변경하기

b 옵션은 mini-batch size, 즉 학습 이미지 몇 장을 한 번에 AI 가속기에서 학습시킬 것인지를 지정합니다. AI 가속기 사양이 높아질수록 거기에 맞춰 mini-batch size를 키워 주어야 최적의 성능을 얻을 수 있습니다.
Hyperscale AI Computing의 AI 가속기 모델별로 권장하는 실행 옵션은 해당 모델 매뉴얼을 참고하십시오.


## 4. RM 설치 파일 설정하기

모델 설치 경로를 수정하고 싶으시다면 `—-download-dir` 옵션 값으로 모델 설치 경로를 수정하실 수 있습니다.
해당 옵션 값이 존재하지 않을 경우에는 기본 경로인 `/home/ubuntu`에 설치가 됩니다.

-  `/data/tf-rm` 경로에 ResNet 모델 파일을 다운받는 명령어 예시입니다.
```bash
ubuntu@vm:~$ get-reference-model --tensorflow resnet --download-dir /data/tf-rm
```



---

Copyright © 2022 Moreh Corporation