Experimental Version 설치
========================

Moreh AI Framework는 Pytorch 1.7.1 버전뿐만이 아닌 Pytorch 1.10.0, 1.13.0 버전과 Tensorflow 2.9.0 버전에 대해서도 제공하고 있습니다. 하지만 Pytorch 1.10.0 버전, Tensorflow 2.9.0 버전은 Experimental Version이라 모델 코드 실행에 다소 불안정할 수 있습니다.

Experimental Version 설치를 위한 옵션은 다음과 같습니다.

.. tip::

    현재 제공되는 Experimental Version은 Pytorch (1.10.0), Pytorch (1.13.0), Tensorflow (2.9.0) 입니다.

- ``--torch`` : Pytorch 1.10.0 이상 버전 설치를 위한 옵션입니다. 기본으로 적용되는 버전은 1.7.1 입니다.
- ``--tensorflow`` : Tensorflow 2.9.0 이상 버전 설치를 위한 옵션입니다. 기본으로 적용되는 버전은 2.9.0 입니다.

다음과 같은 명령어로 Pytorch, Tensorflow 에 대한 Experimental Version을 설치 할 수 있습니다.


.. code-block:: bash

    # Pytorch 1.10.0 버전 설치 torch 기본 버전은 1.7.1
    update-moreh --torch 1.10.0

    # 특정 Moreh AI Framework 버전으로 Pytorch 1.10.0버전 설치
    update-moreh --torch 1.10.0 --target 22.7.2

    # tensorflow 2.9.0 (기본 버전) 설치 
    update-moreh --tensorflow

💡 Tensorflow와 Pytorch 1.10.0 버전은 **동시에 설치를 할 수 없습니다**.

.. code-block:: bash

    update-moreh --torch 1.10.0 --tensorflow
    # >> update-moreh does not support tensorflow and torch>=1.10.0 at the same time
