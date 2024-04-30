
대덕 HAC 사용 매뉴얼 
======================

.. note::

    📌 이 매뉴얼은 KT 융합기술원 개발자들을 위한 대덕 HAC 서버 사용에 대한 세부 가이드를 제공합니다. 대덕 HAC 서버를 효과적으로 활용하고, 대형 모델 개발 작업을 원활하게 수행할 수 있도록 돕는 것을 목표로 합니다. 

- `대덕 HAC 서버 접속하기 <https://docs.moreh.io/ko/latest/HAC/6_%EB%8C%80%EB%8D%95%20HAC%20%EC%82%AC%EC%9A%A9%20%EB%A7%A4%EB%89%B4%EC%96%BC.html#id3>`_ 
- `모델 학습 실행하기 <https://docs.moreh.io/ko/latest/HAC/6_%EB%8C%80%EB%8D%95%20HAC%20%EC%82%AC%EC%9A%A9%20%EB%A7%A4%EB%89%B4%EC%96%BC.html#id4>`_
- ``update-moreh`` `Moreh 솔루션 업데이트하기 <https://docs.moreh.io/ko/latest/HAC/6_%EB%8C%80%EB%8D%95%20HAC%20%EC%82%AC%EC%9A%A9%20%EB%A7%A4%EB%89%B4%EC%96%BC.html#moreh-update-moreh>`_ 
- ``moreh-smi`` `GPU 프로세스 현황 확인하기 <https://docs.moreh.io/ko/latest/HAC/6_%EB%8C%80%EB%8D%95%20HAC%20%EC%82%AC%EC%9A%A9%20%EB%A7%A4%EB%89%B4%EC%96%BC.html#moreh-smi>`_ 
- ``moreh-switch-model`` `가속기 디바이스 변경하기 <https://docs.moreh.io/ko/latest/HAC/6_%EB%8C%80%EB%8D%95%20HAC%20%EC%82%AC%EC%9A%A9%20%EB%A7%A4%EB%89%B4%EC%96%BC.html#ai-sda>`_ 
- `Multi SDA 설정해서 프로세스 진행하기 <https://docs.moreh.io/ko/latest/HAC/6_%EB%8C%80%EB%8D%95%20HAC%20%EC%82%AC%EC%9A%A9%20%EB%A7%A4%EB%89%B4%EC%96%BC.html#multi-kt-ai-accelerator>`_ 
- ``moreh-smi device --add``  `AI 가속기 디바이스(SDA) 추가하기 <https://docs.moreh.io/ko/latest/HAC/6_%EB%8C%80%EB%8D%95%20HAC%20%EC%82%AC%EC%9A%A9%20%EB%A7%A4%EB%89%B4%EC%96%BC.html#id5>`_ 
- ``moreh-smi device --rm`` `생성된 가속기 디바이스 삭제하기 <https://docs.moreh.io/ko/latest/HAC/6_%EB%8C%80%EB%8D%95%20HAC%20%EC%82%AC%EC%9A%A9%20%EB%A7%A4%EB%89%B4%EC%96%BC.html#id6>`_ 
- `VM token 정보 확인하기 <https://docs.moreh.io/ko/latest/HAC/6_%EB%8C%80%EB%8D%95%20HAC%20%EC%82%AC%EC%9A%A9%20%EB%A7%A4%EB%89%B4%EC%96%BC.html#id7>`_ 
- `외부 Python 라이브러리 설치시 Proxy 설정하기 <https://docs.moreh.io/ko/latest/HAC/6_%EB%8C%80%EB%8D%95%20HAC%20%EC%82%AC%EC%9A%A9%20%EB%A7%A4%EB%89%B4%EC%96%BC.html#id8>`_ 

대덕 HAC 서버 접속하기
~~~~~~~~~~~~~~~~~~~~~~~~
먼저 login 서버로 접속합니다. 접속 시 아래와 같은 출력이 나타납니다.

.. code-block:: shell

    Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.13.0-35-generic x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage

    System information as of Fri 16 Jun 2023 05:24:42 PM KST

    System load:                      0.11
    Usage of /:                       14.6% of 437.58GB
    Memory usage:                     1%
    Swap usage:                       0%
    Processes:                        1548
    Users logged in:                  3
    IPv4 address for br-30451918adf3: 172.18.0.1
    IPv4 address for br-e0f0a01d0dc8: 172.30.0.1
    IPv4 address for docker0:         172.17.0.1
    IPv4 address for enp68s0f0:       192.168.0.61
    IPv4 address for enp68s0f1:       10.100.100.234
    IPv4 address for ib0:             10.0.0.61

    * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
    just raised the bar for easy, resilient and secure K8s cluster deployment.

    https://ubuntu.com/engage/secure-kubernetes-at-the-edge

    186 updates can be applied immediately.
    130 of these updates are standard security updates.
    To see these additional updates run: apt list --upgradable

    The list of available updates is more than a week old.
    To check for new updates run: sudo apt update
    New release '22.04.2 LTS' available.
    Run 'do-release-upgrade' to upgrade to it.

    Last login: Fri Jun 16 09:58:16 2023 from 1.249.213.151
    -bash: /home/kt_ailab/anaconda3/bin/conda: /home/kt_ailab/anaconda3/bin/python: bad interpreter: Input/output error

mi100-37 ~ mi100-40 중 선택해서 이동하세요. 둘 중 어떤 서버로 접속할지는 융기원 측 인프라 담당자와 상의하세요. 아래 예시에서는 mi100-37 로 접속합니다.

.. code-block:: shell

    kt_ailab@AIOT-LOGIN-01:~$ ssh mi100-37


모델 학습 실행하기
~~~~~~~~~~~~~~~~~~~~~~~~

학습하고자 하는 모델 폴더(bert)로 이동합니다.

.. code-block:: shell

    kt_ailab@AIOT-MI100:~$ ls
    FastConvMAE  anaconda3  morehtools  resnet   bert   sample
    kt_ailab@AIOT-MI100:~$ cd bert
    (moreh) kt_ailab@AIOT-MI100:~/bert$ python train.py

- ``python train.py`` 를 실행하여 pretraining을 진행합니다.
- 모델 학습 도중 중지 혹은 종료할 경우, 프로그램이 제대로 종료되지 않을 수 있습니다.

Moreh 솔루션 업데이트하기 ``update-moreh``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

    해당 내용은 23.7.0 배포 이후부터 사용가능한 가이드입니다.
    혹은 $HOME경로의 .moreh 폴더를 삭제했을 경우에도 아래와 같은 작업이 필요합니다.

1. default-update-moreh 다운로드 진행 및 실행

.. code-block:: shell

    curl -L http://sys.deploy.kt-epc.moreh.io/package/default-update-moreh/update-moreh --output ./update-moreh

2. 다운로드한 update-moreh 스크립트를 실행가능하도록 변경

.. code-block:: shell

    chmod +x update-moreh

3. update-moreh스크립트를 활용하여 23.7.0으로 업데이트 진행

.. code-block:: shell

    ./update-moreh --force --target 23.7.0
    source ~/.bashrc

4. 이후 기존에 다운로드했던 update-moreh 스크립트 삭제

.. code-block:: shell

    rm update-moreh


학습 프로세스 확인하기  ``moreh-smi``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

대부분의 사용자들에게 GPU 메모리 및 활용률을 확인하는 것은 CPU 정보를 확인하는 것 보다 복잡한 일입니다. 시스템 관리 인터페이스(SMI) 툴이 없다면 GPU의 유형과 기능을 결정하는 것조차 어려울 수 있습니다. 다행히도 Moreh의 최신 소프트웨어 툴은 **`moreh-smi`** 명령어를 통해 현재 선택된 AI 가속기 모델의 실행 중인 학습 프로세스 및 GPU Resource를 얼마나 할당받고 있는지를 확인할 수 있습니다.

.. code-block:: shell

    (moreh) kt_ailab@AIOT-MI100:~$ moreh-smi
    23:23:07 June 13, 2023 
    +---------------------------------------------------------------------------------------------+
    |                                            Current Version: 23.3.0  Latest Version: 23.6.0  |
    +---------------------------------------------------------------------------------------------+
    |  Device  |    Name     |       Model      |  Memory Usage  |  Total Memory  |  Utilization  |
    +=============================================================================================+
    |    0     |  Moreh SDA  |  Small.64GB      |  -             |  -             |  -            |
    |  * 1     |  Moreh SDA  |  2xLarge.1024GB  |  -             |  -             |  -            |
    +---------------------------------------------------------------------------------------------+


AI 가속기 디바이스(SDA) 변경하기 ``moreh-switch-model``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    (moreh) kt_ailab@AIOT-MI100:~/FastConvMAE$ moreh-switch-model
    Current KT AI Accelerator: 4xlarge
    1. micro
    2. small
    3. large
    4. xlarge
    5. 2xlarge
    6. 3xlarge
    7. 4xlarge
    8. 18xlarge
    9. 30xlarge
    10. 60xlarge
    11. 12xlarge
    12. 24xlarge
    13. 48xlarge *
    14. 6xlarge
    15. 16xlarge
    16. 32xlarge
    Selection (1-16, q, Q): 


``moreh-switch-model`` 명령어를 통해 AI 가속기 디바이스를 변경하여 VM에서 사용할 GPU리소스의 양을 조정할 수 있습니다.


Multi KT AI Accelerator 설정하기
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**기존 가속기와 Multi KT AI Accelerator의 차이점**

> 기존 가속기 모델은 ``moreh-switch-model`` 명령어로 AI 학습 수행할 시 GPU 자원의 종류를 Small, Medium, Large, etc까지 고를 수 있게 하는 기능을 담당합니다. 반면에, Multi KT AI Accelerator는 하나의 가상 머신에서 여러 개의 AI 가속기 디바이스를 동시에 실행할 수 있습니다.

하나의 가상 머신에서 여러 개의 AI 가속기 디바이스를 동시에 실행함으로써 아래와 같은 다양한 장점을 얻을 수 있습니다.

- 가상 머신 1개를 여러 명이 동시에 공유해야 할 경우, 가상 머신의 자원을 효율적으로 활용할 수 있습니다.
- 학습에 사용할 하이퍼파라미터를 탐색하기 위한 Hyperparameter Tuning 작업을 여러 번의 학습을 동시에 실행하여 최적의 설정 값을 찾을 수 있습니다.

이러한 병렬적인 작업을 통해 작업 효율성을 극대화하고 다중 사용자 환경에서 자원을 최적으로 활용할 수 있습니다.

예를들어 아래와 같이 ``moreh-smi`` 로 AI 가속기를 추가하여 총 2개의 AI 가속기가 설정되었다면 1개의 user Token 에 대해 VM 한 곳에서 2개의 AI 가속기 프로세스를 동시에 실행 가능합니다.

KT HAC 서비스의 Multi KT AI Accelerator 는 Token 1개당 1개 이상의 디바이스 종류를 생성/삭제할 수 있는 기능을 지원합니다. 하나 이상의 디바이스가 지원되는 것과 동시에 사용자 친화적으로 인터페이스가 구성되어 사용자가 특별한 주의를 기울이지 않더라도 하나의 Token으로 여러 개의 디바이스의 프로세스를 유연하게 실행할 수 있습니다.


.. code-block:: shell

    (moreh) kt_ailab@AIOT-MI100:~$ moreh-smi
    +------------------------------------------------------------------------------------+
    |                                 Current Version: 23.5.0  Latest Version: 23.3.108  |
    +------------------------------------------------------------------------------------+
    |  Device  |    Name     |  Model  |  Memory Usage  |  Total Memory  |  Utilization  |
    +====================================================================================+
    |    0     |  Moreh SDA  |  small  |  -             |  -             |  -            |
    |  * 1     |  Moreh SDA  |  small  |  -             |  -             |  -            |
    +------------------------------------------------------------------------------------+

KT HAC 서비스의 Multi KT AI Accelerator 는 Token 1개당 1개 이상의 디바이스 종류를 생성/삭제할 수 있는 기능을 지원합니다. 하나 이상의 디바이스가 지원되는 것과 동시에 사용자 친화적으로 인터페이스가 구성되어 사용자가 특별한 주의를 기울이지 않더라도 하나의 Token으로 여러 개의 디바이스의 프로세스를 유연하게 실행할 수 있습니다.

**실행 프로세스**

``$ MOREH_VISIBLE_DEVICE=0 python train_your_script_00.py``
``$ MOREH_VISIBLE_DEVICE=1 python train_your_Script_01.py``

위 명령어로 여러 개의 GPU 묶음을 할당하여 병렬 학습을 진행할 수 있습니다.

- Device ID 0번 AI 가속기 → ``train_your_script_00.py`` 을 실행함과 동시에
- Device ID 1번 AI 가속기 → ``train_your_Script_01.py`` 을 실행할 수 있습니다.

AI 가속기 디바이스(SDA) 추가하기 ``moreh-smi device --add``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

  - 현재 하나의 VM 내에서는 최대 5개까지의 AI 가속기를 생성할 수 있습니다.
  - VM 생성된 직후에는 AI 가속기는 1개까지만 기본값으로 제한되어 있습니다. **2개 이상의 AI 가속기 사용이 필요한 경우 Moreh 관리자에게 문의하여 제한값 설정을 요청해 주세요.**

사용자 token이 적용되어 있는 terminal 에서 ``moreh-smi device --add`` 명령어로 AI 가속기 하나를 더 생성해보겠습니다. ``moreh-smi device --add`` 커맨드를 입력하면 ``moreh-switch-model``과 동일한 인터페이스가 아래와 같이 등장합니다. 

.. code-block:: shell

    (moreh) kt_ailab@AIOT-MI100:~$ moreh-smi device --add 3
    Current KT AI Accelerator: 2xLarge.1024GB

    1. Small.64GB 
    2. Medium.128GB 
    3. Large.256GB 
    4. xLarge.512GB 
    5. 2xLarge.1024GB 
    6. 3xLarge.1536GB 
    7. 4xLarge.2048GB 
    8. 6xLarge.3072GB 
    9. 8xLarge.4096GB 
    10. 12xLarge.6144GB 
    11. 24xLarge.12288GB 
    12. 48xLarge.24576GB 
    13. 1.5xLarge.768GB 

    Selection (1-13, q, Q):


1~13 중 사용할 모델에 해당하는 정수를 입력하면 “Create device success.” 메시지와 함께 입력된 device 번호에 해당하는 AI가속기가 생성됩니다. 여기서는 3번 `Large.256GB` 로 AI 가속기를 하나 더 생성해 보겠습니다.

.. code-block:: shell

    Selection (1-13, q, Q): 3
    +---------------------------------------------------+
    |  Device  |        Name         |       Model      |
    +===================================================+
    |  * 0     |  KT AI Accelerator  |  2xLarge.1024GB  |
    |    1     |  KT AI Accelerator  |  Large.256GB     |
    +---------------------------------------------------+
    Create device success.
    1. Small.64GB 
    2. Medium.128GB 
    3. Large.256GB 
    4. xLarge.512GB 
    5. 2xLarge.1024GB 
    6. 3xLarge.1536GB 
    7. 4xLarge.2048GB 
    8. 6xLarge.3072GB 
    9. 8xLarge.4096GB 
    10. 12xLarge.6144GB 
    11. 24xLarge.12288GB 
    12. 48xLarge.24576GB 
    13. 1.5xLarge.768GB


명령어 한 줄로 대화형 prompt 없이도 ``moreh-smi device --add {model_id}``  명령어를 통해 바로 AI 가속기를 생성할 수도 있습니다. 여기서 ``{model_id}`` 는 AI 가속기 모델의 번호를 의미하며, `Large.256GB` 의 경우에는 ‘3’ 이 됩니다.  명령어의 다양한 옵션에 대해서 더 자세히 알고 싶다면 `moreh-smi --help` 로 확인 가능합니다.


생성된 가속기 디바이스 삭제하기 ``moreh-smi device --rm``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

생성된 AI 가속기를 삭제하려면 ``moreh-smi device --rm`` 명령어를 사용하면 됩니다.

``moreh-smi device --rm {Device_ID}`` 명령어로 특정 Device_ID에 해당하는 AI 가속기를 삭제해보겠습니다.

.. code-block:: shell

    (moreh) kt_ailab@AIOT-MI100:~$ moreh-smi --rm 0
    (moreh) kt_ailab@AIOT-MI100:~$ moreh-smi
    17:30:28 May 09, 2023 
    +-----------------------------------------------------------------------------------------------------+
    |                                                    Current Version: 23.5.0  Latest Version: 23.5.0  |
    +-----------------------------------------------------------------------------------------------------+
    |  Device  |        Name         |       Model      |  Memory Usage  |  Total Memory  |  Utilization  |
    +=====================================================================================================+
    |  * 1     |  KT AI Accelerator  |  Large.256GB     |  -             |  -             |  -            |
    +-----------------------------------------------------------------------------------------------------+


참고
~~~~~~~~~~~~~~~

.. tip::

    SSH 클라이언트와 통신이 끊겨 학습이 종료되는 문제를 방지하기 위하여, tmux 등을 활용하여 SSH 통신이 끊겨도 학습에 영향이 없도록 하여 서버를 이용하시는 것을 권장드립니다.

명령어의 다양한 옵션에 대해서 더 자세히 알고 싶다면 ``moreh-smi --help`` 로 확인 가능합니다.

만약 help message에 ``device --add`` 와 같은 옵션의 도움말이 등장하지 않는다면 사용자 token에 대한 최대 디바이스 개수가 1로 설정된 것이므로 고객지원을 요청 부탁드립니다.



VM token 정보 확인하기
-----------------------

token 값은 사용자를 식별하기 위한 hash value이며 사용자마다 고유값으로 부여됩니다. Token은 일반적으로 **사용자의 VM 안에 위치하며, 대덕HAC 서버는 Token 값을 바탕으로 사용자를 식별하고 학습이 실행되므로,** 이 Token 값이 없으면 GPU 연산 및 Python 애플리케이션이 실행되지 않습니다.

``moreh-smi --token`` 또는 ``cat $HOME/.bashrc`` 명령어로 VM에서 token 잘 설정되었는지 확인할 수 있습니다.

.. code-block:: shell

    (moreh) kt_ailab@AIOT-MI100:~$ moreh-smi --token
    15:23:58 June 14, 2023 
    +--------------------------------------------------------------------------+
    |  Device  |        Name         |            Token           |    Model   |
    +==========================================================================+
    |  * 0     |  KT AI Accelerator  |  a3RfYTE2ODU1OTY3NzE2MTA=  |  12xlarge  |
    +--------------------------------------------------------------------------+


.. code-block:: shell

    (moreh) kt_ailab@AIOT-MI100:~$ cat .bashrc

    # enable programmable completion features (you don't need to enable
    # this, if it's already enabled in /etc/bash.bashrc and /etc/profile
    # sources /etc/bash.bashrc).
    if ! shopt -oq posix; then
    if [ -f /usr/share/bash-completion/bash_completion ]; then
        . /usr/share/bash-completion/bash_completion
    elif [ -f /etc/bash_completion ]; then
        . /etc/bash_completion
    fi
    fi

    export MOREH_SDA_TOKEN="a3RfYTE2ODU1OTY3NzE2MTA="
    export MOREH_SDA_MANAGER_ADDRESS=192.168.0.71

    # >>> conda initialize >>>


터미널에 아래와 같은 Token 정보가 나오면 잘 설정된 것입니다.

``export MOREH_SDA_TOKEN="a3RfYTE2ODU1OTY3NzE2MTA="``

``export MOREH_SDA_MANAGER_ADDRESS=192.168.0.71``



외부 Python 라이브러리 설치시 Proxy 설정하기
-------------------------------------

외부 Python 라이브러리를 설치하거나 또는 인터넷이 필요한 상황이라면 아래와 같이 환경 변수로 프록시를 설정합니다.

.. code-block:: shell

    export HTTP_PROXY="192.168.0.61:3128"
    export HTTPS_PROXY="http://192.168.0.61:3128"
    export FTP_PROXY="192.168.0.61:3128"
    export http_proxy="192.168.0.61:3128"
    export https_proxy="http://192.168.0.61:3128"
    export ftp_proxy="192.168.0.61:3128"
    export NO_PROXY="localhost,127.0.0.1,::1"
    export no_proxy="localhost,127.0.0.1,::1"


외부와의 인터넷 연결 사용이 완료된 이후 Moreh 솔루션을 사용하기 위해서는 이전에 설정했던 proxy 설정 해제해야합니다.

.. code-block:: shell

    unset HTTP_PROXY
    unset HTTPS_PROXY
    unset FTP_PROXY
    unset http_proxy
    unset https_proxy
    unset ftp_proxy
    unset NO_PROXY
    unset no_proxy

