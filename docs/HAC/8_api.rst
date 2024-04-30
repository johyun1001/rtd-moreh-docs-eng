Moreh API Document
===========================

이 문서는 Moreh API 및 구현 방법을 소개합니다.
`Moreh API <https://dev-console.moreh.dev/api-docs/>`_ 는 오픈 소스 GRPC 기반 사용자 API 이며 KT Portal에서 REST로 호출됩니다.

Moreh API 시작하기
API를 사용하기 위해서는 애플리케이션 등록을 하셔야 합니다.
애플리케이션을 등록하면 token이 발급되며, API Key를 이용하여 오픈 API 서비스를 이용할 수 있습니다.
오픈 API 이용을 위해서는 API 호출 시 HTTP 헤더 또는 요청 변수에 API Key를 포함해야 합니다.


• 사전 작업 (WIP)
API 사용에 앞서 보통 계정을 등록하거나 또는 API Key 등록과 인증하는 등의 사전 작업이 필요할 수 있습니다.
예를 들어 Web API를 이용하여 Bot을 생성할 때, 자동으로 부여받은 인증키(MCP 인증키)를 통해 어떤 Bot에서 받은 요청인지 인증 및 권한을 검사하는 작업이 필요합니다. 따라서 시작 가이드에는 사전에 인증키(App key)를 어떻게 발급할 수 있고 어떤 용도로 사용되는지 상세히 설명


API 구성 요소
~~~~~~~~~~~~~~~~~~~~~~~~

요청 (Request)
-------------------

먼저 API 요청을 제대로 하기 위해서는 특정 항목들을 일정 포맷에 따라 호출해야 합니다.
API 요청 규격을 구성하는 요소는 **메소드** (GET, POST, PUT, DELETE)와 API를 요청하기 위한 **파라미터** 가 있습니다.

**메소드**

- GET
   - GET 메서드는 특정 리소스의 표시를 요청합니다. GET을 사용하는 요청은 오직 데이터를 받기만 합니다.

- POST
   - POST 메서드는 특정 리소스에 엔티티를 제출할 때 쓰입니다. 이는 종종 서버의 상태의 변화나 부작용을 일으킵니다.

- PUT
   - PUT 메서드는 목적 리소스 모든 현재 표시를 요청 payload로 바꿉니다.

- DELETE
   - DELETE 메서드는 특정 리소스를 삭제합니다.


**파라미터(Query Parameter)**

파라미터는 요청 처리에 필요한 데이터를 전달하는 데 사용합니다. 키와 값의 쌍으로 구성되며, 쿼리 스트링(Query string) 또는 바디(Body)를 통해 전달합니다.
각 파라미터는 자료형(Data type)과 필수 전달 여부가 지정돼 있습니다.
이 문서에는 API 메소드 당 전달해야하는 파라미터 type과 필수 여부 설명 등이 제공됩니다. 간혹 Element가 없는 요청도 있는데 정보를 불러올 때 사용하는 GET 메서드에서 Element가 없는 요청이 나타나기도 합니다.


응답 (Response)
-------------------
응답은 API 요청에 대한 결과값을 의미합니다. 예를 들어 특정 사용자 정보(사용자 고유 Key)를 불러올때 정상적으로 불러왔는지 결과를 확인할 수 있습니다.
Response Element에서는 API 요청에 대한 결과값을 확인할 수 있습니다. 요청한 API의 메서드에 따라 응답 형태는 달라질 수 있는데요. POST와 같이 값을 Body에 실어보낼 때는 해당 값이 잘 저장되었는지, 전달되었는지를 나타내는 성공여부를 나타내기도 하고, GET과 같이 특정 정보를 조회하거나 받아올 때는 값들을 코드로 확인할 수 있거나 자동적으로 다운로드 되기도 합니다.

이 문서에는 API당 응답 및 에러가 어떤 형식과 구성으로 제공되는지 참고할 수 있도록 example response(응답 예제)가 포함되어있습니다.

요청 성공 시: HTTP 상태 코드 및 API별 성공 응답 필드 반환
   - 200 : 클라이언트 요청 정상수행 (응답에 대한 메시지가 포함)

요청 실패 시: HTTP 상태 코드 및 JSON 형식의 에러 응답 필드 반환, 에러 응답 필드에 에러 코드 및 메시지 포함
   - 600 : 일반적인 오류 (주로 API에 필요한 필수 파라미터와 관련하여 서버가 클라이언트 오류를 감지해 요청을 처리하지 못한 상태)
   - 601 : 유효하지 않은 토큰으로 요청했거나 데이터 조회가 안되는 경우


User
~~~~~~~~~~~~

Sign in 관련 사용자 정보를 다룹니다.

.. http:get::  /api/user

    사용자 목록을 불러옵니다.

    :query string id: 특정 사용자만 부르고 싶을 경우 ID 지정

    :>json code 200: ``{ code: ResponseCode }`` successful operation
    :>json String 601: database error

**Example Request:**

id 가 user101인 사용자 목록을 불러옵니다.

.. code-block:: shell 

    Curl

    curl -X 'GET' \
      'https://dev-console.moreh.dev/api/user?id=user101' \
      -H 'accept: application/json'

Request URL: https://dev-console.moreh.dev/api/user?id=user101


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          [
            {
              "nId": 1,
              "sId": "moreh",
              "sName": "모레",
              "sSalt": "Wdsafwerkcjvy4Twev...",
              "sQuestion": "회사의 위치는?"
            }
          ]

   .. tab:: 601

      database error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "Can`t connect to MySQL server on x.x.x.x"
        }


.. http:post:: /api/user

    사용자 정보를 저장합니다.

    ``﹡`` = required 

    :query string id: ``﹡`` 사용자 ID 
    :query string name: ``﹡`` 사용자 이름 
    :query string salt: ``﹡`` 사용자 고유 Key (보안용) 
    :query string password: ``﹡`` 사용자 PWD 
    :query string question: ``﹡`` 사용자 QnA 질문 
    :query string answer: ``﹡`` 사용자 QnA 정답

    :>json String 200: ``"OK"`` successful operation
    :>json String 601: ``ErrorResponse`` database error 

**Example Request:**

id 가 user101인 사용자 정보(id, password,사용자 보안 Key, 사용자 QnA 질문 및 정답) 를 저장합니다.

.. code-block:: shell 

    Curl

    curl -X 'POST' \
    'https://dev-console.moreh.dev/api/user?id=user101&name=username&salt=Wdsafwerkcjvy4Twev&password=userpassword&question=%ED%9A%8C%EC%82%AC%EC%9D%98%20%EC%9C%84%EC%B9%98%EB%8A%94%3F&answer=%EC%84%A0%EB%A6%89' \
    -H 'accept: application/json' \
    -d ''

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "affectedRows": 1,
            "insertId": 0,
            "warningStatus": 0
          }

   .. tab:: 601

      database error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "Can`t connect to MySQL server on x.x.x.x"
        }


.. http:put:: /api/user

    사용자 정보를 재설정합니다.

    ``﹡`` = required 

    :query string id: ``﹡`` 사용자 ID 
    :query string password: ``﹡`` 사용자 PWD 
    :query string answertoken: ``﹡`` 암호화된 사용자 QnA 정답

    :>json String 200: ``"OK"`` successful operation
    :>json String 601: ``ErrorResponse`` database error 


**Example Request:**

id 가 user101인 사용자 정보(id, password, 암호화된 사용자 QnA 정답)를 재설정합니다.

.. code-block:: shell 

    Curl

    curl -X 'PUT' \
    'https://dev-console.moreh.dev/api/user?id=user101&password=userpassword&answertoken=%EC%84%A0%EB%A6%89' \
    -H 'accept: application/json'


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "affectedRows": 1,
            "insertId": 0,
            "warningStatus": 0
          }

   .. tab:: 601

      database error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "Can`t connect to MySQL server on x.x.x.x"
        }


.. http:get::  /api/user/signin

    Sign in 상태를 확인합니다.

    :query string id: ``﹡`` 사용자 ID
    :query string password: ``﹡`` 사용자 PWD

    :>json String 200: ``"OK"`` successful operation
    :>json String 601: ``ErrorResponse`` database error

**Example Request:**

사용자 아이디와 PWD로 정상적으로 로그인되었는지 확인합니다.

.. code-block:: shell 

    Curl

    curl -X 'GET' \
    'https://dev-console.moreh.dev/api/user/signin?id=user101&password=userpassword' \
    -H 'accept: application/json'


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          "success"

   .. tab:: 601

      database error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "Can`t connect to MySQL server on x.x.x.x"
        }

.. http:get::  /api/user/qna

    패스워드 재설정을 위한 QnA를 확인합니다.
    
    ``﹡`` = required 

    :query string id: ``﹡`` 사용자 ID
    :query string salt: ``﹡`` 사용자 고유 Key 보안용
    :query string answer: ``﹡`` 사용자 QnA 정답

    :>json String 200: ``"OK"`` successful operation
    :>json String 601: ``ErrorResponse`` database error

**Example Request:**

사용자 패스워드를 변경하기 위한 질문에 알맞은 답변을 입력했는지 확인합니다.

.. code-block:: shell 

    Curl

    curl -X 'GET' \
    'https://dev-console.moreh.dev/api/user/qna?id=user101&salt=userkey&answer=%EC%84%A0%EB%A6%89' \
    -H 'accept: application/json'


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          "success"

   .. tab:: 601

      database error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "Can`t connect to MySQL server on x.x.x.x"
        }


Check
~~~~~~~~~~~~

API 와 DB 및 gRPC 상태를 확인합니다. API가 에러일 경우 모두 에러로 표시됩니다.

.. http:get::  /api/check

    API 및 gRPC 상태를 확인합니다.

    ``﹡`` = required 

    :query string type: Node IP를 지정할 경우, 해당 노드의 정보만 불러옵니다. 이 값이 정해져있지 않으면 모든 노드의 정보를 불러옵니다. (Available values : api, ipmi, db, grpc 중 선택 (default = api))
    :query string node: ``﹡`` 자세히 보고 싶은 노드의 IP를 입력합니다.
    :query string param_name: ``﹡`` 자세히 보고 싶은 정보를 입력합니다. (temp_gpu, temp_mem, util_gpu, util_mem, usage)

    :>json String 200: ``"OK"`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error

**Example Request:**

API 요청이 정상적으로 호출되는지 확인합니다.

.. code-block:: shell 

    Curl

    curl -X 'GET' \
    'https://dev-console.moreh.dev/api/check?type=api' \
    -H 'accept: application/json'

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

         "success"

   .. tab:: 601

      database error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "Can`t connect to MySQL server on x.x.x.x"
        }


Hardware
~~~~~~~~~~~~
moreh-smi에서 넘어오는 정보(SDA 및 token, 학습 process 정보)들을 다룹니다.

.. http:get::  /api/signal  

    moreh-smi 가 설치된 노드들의 정보를 불러옵니다.

    :query string period: 시간 단위(ms, s, m, h, d, w, y)를 입력합니다.
    :query string node: 자세히 보고 싶은 노드의 IP를 입력합니다.
    :query string param_name: 자세히 보고 싶은 정보(temp_gpu, temp_mem, util_gpu, util_mem, usage)를 입력합니다. 

    :>json String 200: ``PrometheusData []`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 604: ``ErrorResponse`` axios error

**Example Request:**

초 단위로 moreh-smi 가 설치된 노드들의 정보(GPU 사용량 등)를 불러옵니다.

.. code-block:: shell 

    Curl

    curl -X 'GET' \
      'https://dev-console.moreh.dev/api/signal?period=s&node=ipinfo&param_name=usage' \
      -H 'accept: application/json'


**Example Response:**

.. tabs::

   .. tab:: 200

      Prometheus reseponse. json array.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

         [
            {
               "metric": {
                  "__name__": "gpu_info",
                  "device_index": "0",
                  "gpu_type": "AMD",
                  "instance": "backnode01",
                  "job": "moreh_exporter",
                  "param_name": "temp_gpu, temp_mem, util_gpu, util_mem, usage"
               },
               "value": [
                  0,
                  "string"
               ]
            }
         ]

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

         {
         "code": 10061,
         "details": "SyntaxError. check parameters type."
         }

   .. tab:: 604

      axios error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

         "string"



Backend
~~~~~~~~~~~~

moreh-smi에서 넘어오는 정보들 중 Backend 관련 정보를 다룹니다.

.. http:get:: /api/backend

    Backend 정보를 모두 불러옵니다.

    :query Integer id: 특정 Backend 정보를 가져올 경우 ID를 입력하십시오.

    :>json String 200: successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 604: ``ErrorResponse`` axios error

**Example Request:**

사용자 아이디가 user101인 특정 Backend 정보를 불러옵니다.

.. code-block:: shell 

    Curl

    curl -X 'GET' \
      'https://dev-console.moreh.dev/api/backend?id=user101' \
      -H 'accept: application/json'


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

         [
          {
            "id": 1,
            "type": "UCX",
            "ip": "192.168.x.x",
            "port": "21545",
            "devices": [
              {
                "id": 1,
                "name": "Deivce 1",
                "backendId": "1",
                "status": "IDLE"
              }
            ],
            "name": "rx5700-0",
            "status": "SHUTDOWN",
            "group": {
              "id": 1,
              "name": "Group 1",
              "index": 1,
              "combine": true,
              "tokenlist": [
                {
                  "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                  "description": "Token API 테스트용",
                  "priority": 10,
                  "grouplist": [
                    "string"
                  ]
                }
              ]
            },
            "ipmi": {
              "ip": "192.168.0.1",
              "status": -1
            }
          }
        ]

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 604

      grpc error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:post:: /api/backend  

    Backend 정보를 생성합니다.

    ``﹡`` = required 

    :query String node: ``﹡`` IPMI IP
    :query String label: ``﹡`` Backend 별칭
    :query Integer group: ``﹡`` Backend 그룹 
    :query String workerip: ``﹡`` Backend IP 

    :>json String 200: ``{ code: ResponseCode, result: Backend }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Request:**

Backend 정보를 생성합니다.

.. code-block:: shell 

    Curl

    curl -X 'POST' \
      'https://dev-console.moreh.dev/api/backend?node=192.168.x.x&label=2&group=1&workerip=192.168.0.1' \
      -H 'accept: application/json' \
      -d ''


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS",
            "result": {
              "id": 1,
              "type": "UCX",
              "ip": "192.168.x.x",
              "port": "21545",
              "devices": [
                {
                  "id": 1,
                  "name": "Deivce 1",
                  "backendId": "1",
                  "status": "IDLE"
                }
              ],
              "name": "rx5700-0",
              "status": "SHUTDOWN",
              "group": {
                "id": 1,
                "name": "Group 1",
                "index": 1,
                "combine": true,
                "tokenlist": [
                  {
                    "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                    "description": "Token API 테스트용",
                    "priority": 10,
                    "grouplist": [
                      "string"
                    ]
                  }
                ]
              },
              "ipmi": {
                "ip": "192.168.0.1",
                "status": -1
              }
            }
          }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 604

      grpc error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:put:: /api/backend

    Backend 정보를 수정하거나 전원 원격 제어를 위해 IPMI 명령어를 실행합니다.

    ``﹡`` = required 

    :query String command: ``﹡`` 다음 command중 하나를 입력하세요. ``update``: Worker 정보 수정, ``reconnect``: IPMI 설정 확인하며 재연결, ``on``: 전원 ON, ``off``: 전원 off, ``cycle``: 전원 CYCLE, ``reset``: 전원 RESET (Available values : update, reconnect, on, off, cycle, reset)
    :query Integer id: ``﹡`` Backend ID, update 명령을 사용하기 위해서는 필수로 입력하세요.
    :query String node: ``﹡`` IPMI IP, reconnect 명령을 사용하기 위해서는 필수로 입력하세요.
    :query String label: Backend 별칭, update 명령을 사용하려면 입력하세요.
    :query String workerip: Backend IP
    :query String user: IPMI ID: on, off, cycle, reset 명령을 사용하려면 입력하세요.
    :query String pwd: IPMI PWD: on, off, cycle, reset 명령을 사용하려면 입력하세요.

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error
    :>json String 603: ``ErrorResponse`` ipmitool error 

**Example Request:**

Backend ID가 1이면서 IPMI IP가 192.168.0.1인 Worker 정보를 수정합니다.

.. code-block:: shell 

    Curl

    curl -X 'PUT' \
      'https://dev-console.moreh.dev/api/backend?command=update&id=1&node=192.168.0.1' \
      -H 'accept: application/json'


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      grpc error.

      **Media Type**: application/json



      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }
  
   .. tab:: 603

      ipmitool error

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        "Unable to establish IPMI v1.5 / RMCP session"

.. http:delete:: /api/backend

    Backend 정보를 삭제합니다.

    :query Integer id: ``﹡`` Backend ID

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Request:**

Backend ID 가 1에 해당하는 Backend 정보를 삭제합니다.

.. code-block:: shell 

    Curl

    curl -X 'DELETE' \
      'https://dev-console.moreh.dev/api/backend?id=1' \
      -H 'accept: application/json'

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      grpc error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:get:: /api/backend/device/status

    Backend ID를 지정하여 Device들의 Status를 변경합니다.

    :query Integer id: ``﹡`` Backend ID
    :query String status: ``﹡`` 백엔드 상태를 입력합니다. (Available values: SHUTDOWN, IDLE, BUSY)

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Request:**

Backend ID 가 1에 해당하는 디바이스를 SHUTDOWN 합니다.

.. code-block:: shell 

    Curl

    curl -X 'PUT' \
      'https://dev-console.moreh.dev/api/backend/device/status?id=1&status=shutdown' \
      -H 'accept: application/json'

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      grpc error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:post:: /api/backend/grouping

     Backend로 이루어진 Group들 간에 관계를 수정합니다.

    :query Integer group: ``﹡`` Group ID
    :query Integer backend: ``﹡`` Backend ID

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Request:**

ID가 2인 backend group에 특정 (ID가 1인)backend를 추가합니다.

.. code-block:: shell 

    Curl

    curl -X 'POST' \
      'https://dev-console.moreh.dev/api/backend/grouping?group=2&backend=1' \
      -H 'accept: application/json' \
      -d ''

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:put:: /api/backend/grouping

    Backend로 이루어진 Group들 간에 관계를 수정합니다.

    :query Integer group: ``﹡`` Group ID
    :query Integer backend: ``﹡`` Backend ID

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Request:**

ID가 1인 backend의 기존 Group을 ID가 3인 Group으로 변경합니다.

.. code-block:: shell 

    Curl

    curl -X 'PUT' \
      'https://dev-console.moreh.dev/api/backend/grouping?group=3&backend=1' \
      -H 'accept: application/json'

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:delete:: /api/backend/grouping

    Backend의 Grouping 된 것을 해제합니다.

    :query Integer group: Group ID
    :query Integer backend: Backend ID

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Request:**

backend의 그룹 ID가 3인 Group을 제거합니다.

.. code-block:: shell 

    Curl

    curl -X 'DELETE' \
      'https://dev-console.moreh.dev/api/backend/grouping?group=3&backend=1' \
      -H 'accept: application/json'

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:get:: /api/backend/group

    Backend의 group 정보를 불러옵니다.

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:post:: /api/backend/group

    Backend Group 정보를 생성합니다.

    :query String group: ``﹡`` 그룹 별칭

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Request:**

그룹 label이 "ktc"인 Backend 그룹을 생성합니다.

.. code-block:: shell 

    Curl

    curl -X 'POST' \
      'https://dev-console.moreh.dev/api/backend/group?label=ktc' \
      -H 'accept: application/json' \
      -d ''

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS",
            "result": {
              "id": 1,
              "name": "Group 1",
              "index": 1,
              "combine": true,
              "tokenlist": [
                {
                  "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                  "description": "Token API 테스트용",
                  "priority": 10,
                  "grouplist": [
                    "string"
                  ]
                }
              ]
            }
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:put:: /api/backend/group

    Backend 그룹 정보를 수정합니다.

    :query Integer id: ``﹡`` Group ID
    :query String label: ``﹡`` Group 별칭

    :>json String 200: ``{ code: Success }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Request:**

.. code-block:: shell 

    Curl

    curl -X 'DELETE' \
      'https://dev-console.moreh.dev/api/backend/group?id=2' \
      -H 'accept: application/json'


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS",
            "result": {
              "id": 1,
              "name": "Group 1",
              "index": 1,
              "combine": true,
              "tokenlist": [
                {
                  "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                  "description": "Token API 테스트용",
                  "priority": 10,
                  "grouplist": [
                    "string"
                  ]
                }
              ]
            }
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:delete:: /api/backend/group

    Backend 그룹 정보를 삭제합니다.

    :query Integer id: ``﹡`` Group ID

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS",
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }



SDA Model
~~~~~~~~~~~~~~~~~~

SDAModel를 관리합니다.


.. http:get:: /api/sdamanager/sdamodel

    SDA Model 목록을 불러옵니다 (ex micro, small, large, xlarge ...).

    :query String token: token 값

    :>json String 200: ``SDAModel []`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          [
            {
              "id": 1,
              "name": "micro",
              "numDevices": 1,
              "description": "micro SDA Model",
              "group": {
                "id": 1,
                "name": "Group 1",
                "index": 1,
                "combine": true,
                "tokenlist": [
                  {
                    "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                    "description": "Token API 테스트용",
                    "priority": 10,
                    "grouplist": [
                      "string"
                    ]
                  }
                ]
              }
            }
          ]


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:post:: /api/sdamanager/sdamodel

    SDA Model 을 추가합니다.

    :query String name: ``﹡`` SDA Model 명
    :query Integer numDevices: ``﹡`` 사용할 디바이스 갯수
    :query String desc: ``﹡`` SDA Model 설명

    :>json String 200: ``{ code: ResponseCode, result: SDAModel }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS",
            "result": {
              "id": 1,
              "name": "micro",
              "numDevices": 1,
              "description": "micro SDA Model",
              "group": {
                "id": 1,
                "name": "Group 1",
                "index": 1,
                "combine": true,
                "tokenlist": [
                  {
                    "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                    "description": "Token API 테스트용",
                    "priority": 10,
                    "grouplist": [
                      "string"
                    ]
                  }
                ]
              }
            }
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:delete:: /api/sdamanager/sdamodel

    SDA Model을 삭제합니다.

    :query Integer sdamodel: ``﹡`` SDA Model ID

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:post:: /api/sdamanager/sdamodel/grouping

    SDA Model의 Grouping을 생성합니다.

    :query Integer sdamodel: ``﹡`` SDA Model ID
    :query Integer group: ``﹡`` Group ID

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:delete:: /api/sdamanager/sdamodel/grouping

    SDA Model의 Grouping을 해제합니다.

    :query Integer sdamodel: ``﹡`` SDA Model ID
    :query Integer group: ``﹡`` Group ID

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:get:: /api/sdamanager/sdamodel/group

    SDA Model 그룹 정보를 불러옵니다.

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:post:: /api/sdamanager/sdamodel/group

    SDA Model 그룹 정보를 생성합니다.

    :query String label: ``﹡`` 그룹 별칭
    :query Integer groupId: ``﹡`` Backend group ID. 지정되지 않을 경우 default backend group

    :>json String 200: ``{ code: ResponseCode, result: Group }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

    

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:put:: /api/sdamanager/sdamodel/group

    SDA Model 그룹 정보를 수정합니다.

    :query Integer id: ``﹡`` 그룹 ID 
    :query String label: ``﹡`` 그룹 별칭

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }



.. http:delete:: /api/sdamanager/sdamodel/group

    SDA Model 그룹 정보를 수정합니다.

    :query Integer id: ``﹡`` 그룹 ID 
    :query Integer sdaid: 지정된 SDA ID가 있을 경우 해당 SDA만 삭제

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


SDA
~~~~~~~~~~~~~~~~~~

SDA를 관리합니다.

.. http:get:: /api/sdamanager/sda

    SDA 정보를 모두 불러옵니다. 할당된 SDA가 존재한다면 할당된 device와 backend 또한 출력합니다.

    :query String token: ``﹡`` 특정 Token을 가진 SDA 정보만 가져올 경우, 해당 Token의 값을 입력하십시오.

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "id": 1,
            "modelId": 1,
            "token": {
              "value": "bWkxASDFVDyMzM0NjQ4MTA=",
              "description": "Token API 테스트용",
              "priority": 10,
              "grouplist": [
                {
                  "id": 1,
                  "name": "Group 1",
                  "index": 1,
                  "combine": true,
                  "tokenlist": [
                    "string"
                  ]
                }
              ]
            },
            "reserved": false,
            "numDevices": 4,
            "backends": [
              {
                "id": 1,
                "type": "UCX",
                "ip": "192.168.x.x",
                "port": "21545",
                "devices": [
                  {
                    "id": 1,
                    "name": "Deivce 1",
                    "backendId": "1",
                    "status": "IDLE"
                  }
                ],
                "name": "rx5700-0",
                "status": "SHUTDOWN",
                "group": {
                  "id": 1,
                  "name": "Group 1",
                  "index": 1,
                  "combine": true,
                  "tokenlist": [
                    "string"
                  ]
                },
                "ipmi": {
                  "ip": "192.168.0.1",
                  "status": -1
                }
              }
            ],
            "description": "SDA API 테스트용",
            "sdamodelName": "large"
          }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:post:: /api/sdamanager/sda

    SDA Model, Token, 고정할당유무, 별칭을 지정하면 SDA를 생성합니다.

    :query Integer model: ``﹡`` SDA Model ID
    :query String token: ``﹡`` Token 값
    :query String desc: ``﹡`` SDA 별칭
    :query boolean reserved: ``﹡`` 고정 할당 유무

    :>json String 200: ``{ code: ResponseCode, result: SDA }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS",
            "result": {
              "id": 1,
              "modelId": 1,
              "token": {
                "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                "description": "Token API 테스트용",
                "priority": 10,
                "grouplist": [
                  {
                    "id": 1,
                    "name": "Group 1",
                    "index": 1,
                    "combine": true,
                    "tokenlist": [
                      "string"
                    ]
                  }
                ]
              },
              "reserved": false,
              "numDevices": 4,
              "backends": [
                {
                  "id": 1,
                  "type": "UCX",
                  "ip": "192.168.x.x",
                  "port": "21545",
                  "devices": [
                    {
                      "id": 1,
                      "name": "Deivce 1",
                      "backendId": "1",
                      "status": "IDLE"
                    }
                  ],
                  "name": "rx5700-0",
                  "status": "SHUTDOWN",
                  "group": {
                    "id": 1,
                    "name": "Group 1",
                    "index": 1,
                    "combine": true,
                    "tokenlist": [
                      "string"
                    ]
                  },
                  "ipmi": {
                    "ip": "192.168.0.1",
                    "status": -1
                  }
                }
              ],
              "description": "SDA API 테스트용",
              "sdamodelName": "large"
            }
          }


   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:put:: /api/sdamanager/sda

    Token 값을 지정하고 SDA Model ID를 선택하면 Token의 SDA Model이 지정된 값으로 수정합니다.

    :query String token: ``﹡`` Token 값
    :query Integer sdaId: ``﹡`` SDA ID
    :query Integer model: ``﹡`` SDA Model ID

    :>json String 200: ``{ code: ResponseCode, result: SDA }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }       

   .. tab:: 600

      syntax error.

      **Media Type**: application/json
    

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:delete:: /api/sdamanager/sda

    Token 값을 지정하면 해당 SDA를 삭제합니다.

    :query String token: ``﹡`` Token 값

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }       

   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:get:: /api/sdamanager/sdautilizations

    SDA의 할당 정보(메모리 사용량, 프로세스 정보)를 불러옵니다.

    :query String token: ``﹡`` Token 값
    
    :>json String 200: ``SDAUtilizationRespons`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "id": 1,
            "pid": 28658,
            "ptype": "service",
            "processName": "python pytorch-sample.py",
            "sdautils": [
              {
                "totalMemory": 1024,
                "usedMemory": 512,
                "temperature": 56,
                "gpuPower": 90,
                "sda": {
                  "id": 1,
                  "modelId": 1,
                  "token": {
                    "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                    "description": "Token API 테스트용",
                    "priority": 10,
                    "grouplist": [
                      {
                        "id": 1,
                        "name": "Group 1",
                        "index": 1,
                        "combine": true,
                        "tokenlist": [
                          "string"
                        ]
                      }
                    ]
                  },
                  "reserved": false,
                  "numDevices": 4,
                  "backends": [
                    {
                      "id": 1,
                      "type": "UCX",
                      "ip": "192.168.x.x",
                      "port": "21545",
                      "devices": [
                        {
                          "id": 1,
                          "name": "Deivce 1",
                          "backendId": "1",
                          "status": "IDLE"
                        }
                      ],
                      "name": "rx5700-0",
                      "status": "SHUTDOWN",
                      "group": {
                        "id": 1,
                        "name": "Group 1",
                        "index": 1,
                        "combine": true,
                        "tokenlist": [
                          "string"
                        ]
                      },
                      "ipmi": {
                        "ip": "192.168.0.1",
                        "status": -1
                      }
                    }
                  ],
                  "description": "SDA API 테스트용",
                  "sdamodelName": "large"
                }
              }
            ],
            "code": "SUCCESS"
          }   

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


Token
~~~~~~~~~~~~~~~~~~

Token 및 Group 정보를 관리합니다.

.. http:get:: /api/sdamanager/token

    Token 정보를 모두 불러옵니다.

    :query String token: ``﹡`` Token 값
    :query Integer maxDuplicates: ``﹡``  0: infinity, 1: off, 2~: maxDuplicates 설정값 (중복 허용치)
    
    :>json String 200: ``Token []`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        [
          {
            "value": "bWkxASDFVDyMzM0NjQ4MTA=",
            "description": "Token API 테스트용",
            "priority": 10,
            "grouplist": [
              {
                "id": 1,
                "name": "Group 1",
                "index": 1,
                "combine": true,
                "tokenlist": [
                  "string"
                ]
              }
            ]
          }
        ]    

   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:post:: /api/sdamanager/token

    Token 별칭을 입력하면 고유한 값을 가진 Token을 생성합니다.

    :query String desc: ``﹡`` Token 설명
    :query Integer priority: ``﹡`` Token 우선순위
    :query Integer maxDuplicates: ``﹡``  0: infinity, 1: off, 2~: maxDuplicates 설정값 (중복 허용치)
    
    :>json String 200: ``{ code: ResponseCode, result: Token }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": "SUCCESS",
          "result": {
            "value": "bWkxASDFVDyMzM0NjQ4MTA=",
            "description": "Token API 테스트용",
            "priority": 10,
            "grouplist": [
              {
                "id": 1,
                "name": "Group 1",
                "index": 1,
                "combine": true,
                "tokenlist": [
                  "string"
                ]
              }
            ]
          }
        }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:put:: /api/sdamanager/token

    Token이 가지고 있는 고유한 값을 입력하면 Token을 수정합니다.

    :query String token: ``﹡`` Token 값
    :query String desc: ``﹡`` Token 설명
    :query Integer priority: ``﹡`` Token 우선순위
    :query Integer maxSdaCount: ``﹡`` SDA 허용 최대값
    :query Integer targetSdaId: ``﹡`` 현재 가리키고 있는 SDA ID

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": "SUCCESS"
        }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:delete:: /api/sdamanager/token

    Token이 가지고 있는 고유한 값을 입력하면 Token을 삭제합니다.

    :query String token: ``﹡`` Token 값

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": "SUCCESS"
        }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:get:: /api/sdamanager/token/group

Token (user) 그룹 정보를 불러옵니다.

**No Parameters**

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        [
          {
            "id": 1,
            "name": "Group 1",
            "index": 1,
            "combine": true,
            "tokenlist": [
              {
                "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                "description": "Token API 테스트용",
                "priority": 10,
                "grouplist": [
                  "string"
                ]
              }
            ]
          }
        ]

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:post:: /api/sdamanager/token/group

    Token (user) 그룹 정보를 생성합니다.

    :query String label: ``﹡`` 그룹 별칭

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": "SUCCESS",
          "result": {
            "id": 1,
            "name": "Group 1",
            "index": 1,
            "combine": true,
            "tokenlist": [
              {
                "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                "description": "Token API 테스트용",
                "priority": 10,
                "grouplist": [
                  "string"
                ]
              }
            ]
          }
        }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:put:: /api/sdamanager/token/group

    Token (user) 그룹 정보를 수정합니다.

    :query Integer id: ``﹡`` 그룹 ID
    :query String label: 그룹 별칭

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

        {
          "code": "SUCCESS"
        }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:delete:: /api/sdamanager/token/group

    Token (user) 그룹 정보를 삭제합니다.

    :query Integer id: ``﹡`` 그룹 ID

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": "SUCCESS"
        }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:delete:: /api/sdamanager/token/grouping

    Token (user) Grouping을 해제합니다.

    :query Integer group: ``﹡`` Token 그룹 ID
    :query String token: ``﹡`` 해제할 token 값

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

  

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

        {
          "code": "SUCCESS"
        }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      
      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:post:: /api/sdamanager/token/grouping

    Token (user) Grouping을 생성합니다.

    :query Integer group: ``﹡`` Token 그룹 ID
    :query String token: ``﹡`` Token 그룹에 token 추가 시 사용: 추가할 token 값

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json


      **Example Value** 

      .. code-block:: shell

        {
          "code": "SUCCESS"
        }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


Scheduler
~~~~~~~~~~~~~~~~~~

GPU 스케줄러의 큐와 기록을 확인합니다.

.. http:get:: /api/scheduler/queue

    GPU 스케줄러의 큐 안의 정보를 불러옵니다.

    :query String status: ``﹡`` 특정 상태의 정보만 원할 경우 선택 (Available values : running, waiting)
    :query int64 id: GPU job에 할당하는 ID

    :>json String 200: ``JobInfo []`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error



**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          [
            {
              "id": 1,
              "token": {
                "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                "description": "Token API 테스트용",
                "priority": 10,
                "grouplist": [
                  {
                    "id": 1,
                    "name": "Group 1",
                    "index": 1,
                    "combine": true,
                    "tokenlist": [
                      "string"
                    ]
                  }
                ]
              },
              "priority": 10,
              "status": "Running, Waiting, Canceled, Failed, Completed",
              "clientPid": 23315,
              "processName": "python sample.py",
              "requestTime": "2021-11-10 07:20:00.263",
              "startTime": "2021-11-10 07:20:00.263",
              "endTime": "2021-11-10 07:20:00.263",
              "referer": {
                "protocol": "1",
                "ipAddress": "ipv4:100.12.0.1:33180"
              },
              "deviceCount": 4,
              "deviceInfo": "{\"device_info\":[{\"host\":\"back-node03\",\"devices\":[0,1,2,3,4,5,6,7]}]}"
            }
          ]

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:put:: /api/scheduler/queue

    큐에서 대기중인 GPU 작업의 순서를 바꿀 때 사용합니다.

    :query Integer id: ``﹡`` 사용자의 GPU job에 할당하는 ID
    :query Integer priority: ``﹡`` GPU job의 우선순위

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:delete:: /api/scheduler/queue

    등록된 Job을 삭제합니다.

    :query Integer id: ``﹡`` 삭제 할 Job의 ID
    :query boolean isWeb: ``﹡``  웹에서 요청한 경우(True 아니면 False)인지 확인 

    :>json String 200: ``{ code: ResponseCode }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS"
          }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:get:: /api/scheduler/history

    GPU 스케줄러의 기록 정보를 불러옵니다.

    :query String (YYYY-MM-DD HH:mm) starttimeFrom: ``﹡`` 필터. 작업의 시작날짜가 {starttimeFrom}보다 뒤에 있는지 검색
    :query String (YYYY-MM-DD HH:mm) starttimeTo: ``﹡``  필터. 작업의 시작날짜가 {starttimeTo}보다 앞에 있는지 검색
    :query String (YYYY-MM-DD HH:mm) endtimeFrom: ``﹡`` 필터. 작업의 종료날짜가 {endtimeFrom}보다 뒤에 있는지 검색
    :query String (YYYY-MM-DD HH:mm) endtimeTo: ``﹡``  필터. 작업의 종료날짜가 {endtimeTo}보다 앞에 있는지 검색
    :query String status: ``﹡`` 필터. 작업의 상태를 ,로 구분(ex. completed,canceled)하여 검색
    :query String token: ``﹡``  필터. Token 값에서 해당하는 검색어가 있는지 확인
    :query Integer offset: ``﹡`` 필터. 전체 기록중에서 일부만 가져올 경우 범위 지정 (시작) (default = 0)
    :query Integer limit: ``﹡``  필터. 전체 기록중에서 일부만 가져올 경우 범위 지정 (길이) (default = 500)
    :query Integer id: ``﹡``  필터. ID 입력시 해당 아이디만 return

    :>json String 200: ``{ jobs: JobInfo [], totalCount: integer }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "jobs": [
              {
                "id": 1,
                "token": {
                  "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                  "description": "Token API 테스트용",
                  "priority": 10,
                  "grouplist": [
                    {
                      "id": 1,
                      "name": "Group 1",
                      "index": 1,
                      "combine": true,
                      "tokenlist": [
                        "string"
                      ]
                    }
                  ]
                },
                "priority": 10,
                "status": "Running, Waiting, Canceled, Failed, Completed",
                "clientPid": 23315,
                "processName": "python sample.py",
                "requestTime": "2021-11-10 07:20:00.263",
                "startTime": "2021-11-10 07:20:00.263",
                "endTime": "2021-11-10 07:20:00.263",
                "referer": {
                  "protocol": "1",
                  "ipAddress": "ipv4:100.12.0.1:33180"
                },
                "deviceCount": 4,
                "deviceInfo": "{\"device_info\":[{\"host\":\"back-node03\",\"devices\":[0,1,2,3,4,5,6,7]}]}"
              }
            ],
            "totalCount": 1
          }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }



Membership
~~~~~~~~~~~~~~~~~~

.. http:get:: /api/membership

Membership 정보를 불러옵니다.

**No Parameters**
  
**Responses**

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - Code
     - Description
     - Schema
   * - default
     - successful operation
     - ``Group []``
   * - 600
     - syntax error
     - ErrorResponse
   * - 602
     - grpc error
     - ErrorResponse

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          [
            {
              "id": 1,
              "name": "Group 1",
              "index": 1,
              "combine": true,
              "tokenlist": [
                {
                  "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                  "description": "Token API 테스트용",
                  "priority": 10,
                  "grouplist": [
                    "string"
                  ]
                }
              ]
            }
          ]

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


.. http:post:: /api/membership

    Membership 정보를 생성합니다. (Group ID와 Group ID간의 연결을 생성합니다)

    :query String parentId: ``﹡`` Membership Parent ID
    :query String childId: ``﹡`` Membership Child ID
    
    :>json String 200: ``{ code: ResponseCode, result: Group }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error

**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": "SUCCESS",
          "result": {
            "id": 1,
            "name": "Group 1",
            "index": 1,
            "combine": true,
            "tokenlist": [
              {
                "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                "description": "Token API 테스트용",
                "priority": 10,
                "grouplist": [
                  "string"
                ]
              }
            ]
          }
        }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }

.. http:delete:: /api/membership

    Membership 정보를 삭제합니다. (Group ID와 Group ID간의 연결을 삭제합니다)

    :query String parentId: ``﹡`` Membership Parent ID
    :query String childId: ``﹡`` Membership Child ID

    :>json String 200: ``{ code: ResponseCode, result: Group }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": "SUCCESS"
        }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }




Usage
~~~~~~~~~~~~~~~~~~

GPU 사용 기록을 확인합니다.

.. http:get:: /api/usage

    GPU 사용 기록을 불러옵니다.

    :query String starttime: ``﹡`` 시작 시간 (YYYY-MM-DD hh:mm:ss)
    :query String endtime: ``﹡`` 종료 시간 (YYYY-MM-DD hh:mm:ss)
    :query String token: ``﹡`` token 값

    :>json String 200: ``{ jobs: JobInfo [], totalCount: integer }`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
            "code": "SUCCESS",
            "total_usage": {
              "token": {
                "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                "description": "Token API 테스트용",
                "priority": 10,
                "grouplist": [
                  {
                    "id": 1,
                    "name": "Group 1",
                    "index": 1,
                    "combine": true,
                    "tokenlist": [
                      "string"
                    ]
                  }
                ]
              },
              "min": 0,
              "max": 8,
              "average": 1.2234,
              "min_percentage": 1.2234,
              "max_percentage": 1.2234,
              "average_percentage": 1.2234,
              "total_devices": 480
            },
            "usage_list": [
              {
                "token": {
                  "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                  "description": "Token API 테스트용",
                  "priority": 10,
                  "grouplist": [
                    {
                      "id": 1,
                      "name": "Group 1",
                      "index": 1,
                      "combine": true,
                      "tokenlist": [
                        "string"
                      ]
                    }
                  ]
                },
                "min": 0,
                "max": 8,
                "average": 1.2234
              }
            ]
          }

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }



Log
~~~~~~~~~~~~~~~~~~

API 로그를 관리합니다.

.. http:get:: /api/log/sdamanager/event

    SDAManager에 발생한 Event (SDA 생성, SDA 변경 등)을 불러옵니다.

    :query String token: ``﹡`` 특정 Token 정보만 원할 경우 Token 값을 지정
    :query String action: ``﹡``  특정 액션 정보만 원할 경우 액션 값을 지정 (Available values: CREATE_SDA, UPDATE_SDA, DELETE_SDA, CREATE_SDAMODEL, DELETE_SDAMODEL 중 선택)

    :>json String 200: ``Event []`` successful operation
    :>json String 600: ``ErrorResponse`` syntax error
    :>json String 602: ``ErrorResponse`` grpc error


**Example Response:**

.. tabs::

   .. tab:: 200

      successful operation.
      
      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          [
            {
              "token": {
                "value": "bWkxASDFVDyMzM0NjQ4MTA=",
                "description": "Token API 테스트용",
                "priority": 10,
                "grouplist": [
                  {
                    "id": 1,
                    "name": "Group 1",
                    "index": 1,
                    "combine": true,
                    "tokenlist": [
                      "string"
                    ]
                  }
                ]
              },
              "action": "UPDATE_SDA",
              "request": "{\"token\":{\"value\":\"MTYzNDIxNDc0NzEwOQ==\",\"description\":\"\",\"priority\":0},\"model_id\":1,\"referer\":{\"protocol\":\"HTTP\",\"ip_addr\":\"123.142.0.237\"}}",
              "response": "{\"code\":\"SUCCESS\"}",
              "eventTime": "2021-10-11T20:28:06.521Z",
              "referer": {
                "protocol": "1",
                "ipAddress": "ipv4:100.12.0.1:33180"
              }
            }
          ]

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

          {
          "code": 10061,
          "details": "SyntaxError. check parameters type."
          }

   .. tab:: 602

      gRPC error.

      **Media Type**: application/json

      **Example Value** 

      .. code-block:: shell

        {
          "code": 10061,
          "details": "gRPCError. check parameters type."
        }


Copyright © 2022 Moreh Corporation
