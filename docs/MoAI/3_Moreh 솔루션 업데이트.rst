Moreh 솔루션 업데이트 하기
=====================

가속기를 업데이트하는 명령어입니다. 

``update-moreh`` 
~~~~~~~~~~~~~~~~


기본적으로 위 명령어 실행 시 현재까지 배포된 버전 중 최신 버전으로 업데이트를 진행합니다.


.. tip::

    ``update-moreh --tensorflow`` 시 update가 진행되지 않거나 Python 패키지가 잡히지 않는다면 .local 이슈로 인한 문제일 수 있습니다. 해당 폴더 ~/.local/lib, ~/.local/bin 을 삭제 후 재시도해보시기 바랍니다.


**Supported Arguments**


``--target`` 
~~~~~~~~~~~~


Moreh AI Framework를 특정 버전으로 다운(업)그레이드를 할 수 있는 옵션입니다. ``--target`` 옵션 뒤에는 특정 버전을 아래와 같이 기입해주시면 됩니다.

.. code-block:: bash
    
    # 22.7.2 버전이 현재보다 낮은 버전이라면 다운그레이드 가능
    update-moreh --target 22.7.2


.. code-block:: bash
    
    # 23.3.0 버전으로 업데이트 및 롤백 경우
    update-moreh --target 23.3.0


.. warning::

    동일한 버전으로 다시 Moreh 솔루션을 설치하고 싶은 경우나, 원하는 타깃 버전으로 업(다운)그레이드가 정상적으로 되지 않을 경우 ``--force`` 옵션을 통해 강제로 Moreh 솔루션의 업데이트를 진행할 수 있습니다.
    하지만 가급적이면 Moreh 솔루션 사용시 ``--force`` command는 지양하고 있으니 버전이슈로 인한 에러가 발생한 경우 고객지원을 요청 바랍니다.

    .. code-block:: bash

        # 22.10.2 버전을 강제 설치
        update-moreh --target 22.10.2 --force



