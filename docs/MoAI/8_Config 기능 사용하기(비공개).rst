Config 기능 사용하기
=================

Config는 Moreh 솔루션을 이용할 때 환경변수, config 파일, runtime 옵션 등을 쉽게 컨트롤하기 위해 설정하는 기능입니다. 
따라서 사용자가 모델 학습 시 특정 기능을 키고 끄거나, 설정값을 조정하여 성능 튜닝을 하는등 다양하게 활용될 수 있습니다.


Config 옵션 정의 방법
~~~~~~~~~~~~~~~~~~

Config 의 속성을 부여하기 위해서는 **config_def.cpp** 의 ``Config::DefineConfigParams()`` 함수에서 ``DefineConfig()`` 를 다음 예시와 같이 호출합니다.

.. code-block:: bash
    
    DefineConfig<int64_t>("example_config_name", /* default value*/ 50)
    .Description("explanation. blah blah...")
    .Mutable()
    .SendToBackend();


* ``DefineConfig`` 에 인자로 직접 넘기는 것 이외에는 모두 `Optional Attributes <https://moreh-corporation-moreh-test-search.readthedocs-hosted.com/ko/latest/HAC/8_Config%20%EA%B8%B0%EB%8A%A5%20%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0.html#optional-attritbutes>`_ 입니다.
* ``.Mutable().Decription(...)`` 과 같이 chaining 하며 호출 순서는 무관합니다.
* DefineConfig 간의 호출 순서는 이름 순서(알파벳) 정렬되도록 하는것을 권장합니다.

Requirement
~~~~~~~~~~~

* Config 파라미터의 이름 (위 예시의 **"example_config_name"**)
   * 대소문자 구분은 없지만, 가급적 소문자로 정의하고 단어 구분자로 underbar(**_**)를 사용합니다.
* 데이터 타입 (위 예시의 **<int64_t>**) 과 해당 타입의 default value (예시의 **50**)
   * int64_t, bool, std::string, double 네가지 타입중 하나로 지정합니다.
   * (default value의 타입으로 template type argument를 유추할 수 있는 경우 생략 가능)



Config 설정 사용 예시
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    DefineConfig("enable_conv2d_fusion", false).Mutable();
    DefineConfig("enable_pipeline_parallel", false).Mutable();
    DefineConfig("use_modnn_random_generator", false).AllowUserAccess();


위 예시에서 관리자(admin, developer)만 설정 가능한 Options은 다음과 같습니다.
  * ``enable_conv2d_fusion`` : cond2d 연산이 fusion되어서 성능이 향상될 수 있음
  * ``enable_pipeline_parallel`` : Pipeline Parallelism 을 사용하여 NLP같은 큰 모델을 학습시 모델을 각 GPU 에 나눠 담을 수 있음





