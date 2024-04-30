# KT AI Accelerator 사용하기

이 문서는 하나의 Token을 가진 사용자가 여러 개의 디바이스 종류를 추가/삭제/선택하는 방법이 명세되어있습니다.

**KT AI Accelerator란?**

<aside>
KT HAC 서비스의 KT AI Accelerator 는 Token 1개당 1개 이상의 디바이스 종류를 생성/삭제할 수 있는 기능을 지원합니다. 하나 이상의 디바이스가 지원되는 것과 동시에 사용자 친화적으로 인터페이스가 구성되어 사용자가 특별한 주의를 기울이지 않더라도 하나의 Token으로 여러개의 디바이스의 프로세스를 유연하게 실행할 수 있습니다.
</aside>

---
**기존 가속기와 KT AI Accelerator의 차이점**

기존 가속기 모델은 `moreh-switch-model` 명령어로 AI 학습 수행할 시 GPU 자원의 종류를 small, medium, large, etc 까지 고를 수 있게 하는 기능을 담당합니다. 반면에, KT AI Accelerator는 여러개의 GPU 묶음을 할당하여 병렬 학습을 진행할 수 있습니다.

---

**KT AI Accelerator는 아래 4가지 명령어로 사용할 수 있습니다.**

1. `moreh-smi device --add` - KT AI Accelerator 디바이스 생성하기

2. `moreh-smi device --rm` - KT AI Accelerator 디바이스 삭제하기

3. `moreh-smi device --switch` - KT AI Accelerator 생성된 디바이스 변경하기

4. `moreh-smi -i` - KT AI Accelerator 디바이스의 활용 상태 모니터링하기

---

## 1. KT AI Accelerator 디바이스 생성하기

**`moreh-smi device --add`** 커맨드를 입력하면 moreh-switch-model과 동일한 인터페이스가 아래와 같이 등장합니다. 

```bash
Current KT AI Accelerator: Medium.128GB

1. Small.64GB
2. Medium.128GB*
3. Large.256GB
4. xLarge.512GB
5. 2xLarge.1024GB
6. 3xLarge.1536GB
7. 4xLarge.2048GB
8. 6xLarge.3072GB
9. 8xLarge.4096GB
10. 12xLarge.6144GB
11. 24xLarge.12288GB
12. 1.5xLarge.768GB

Selection (1-12, q, Q):
```

1~12 중 사용할 모델에 해당하는 정수를 입력하면 선택된 모델로 변경되었다는 메시지와 함께 해당 디바이스 모델이 생성됩니다.

- `moreh-smi device --add {SDA id}` 입력 예시
    
    ```bash
    # Large.256GBSDA 모델을 생성
    moreh-smi device add 3
    ```
    

## 2. KT AI Accelerator 디바이스 삭제하기

**`moreh-smi device --rm`** 명령어를 입력하면 device가 삭제되며 가속기 디바이스 목록에서 마지막에 사용한 디바이스가 디폴트로 표시됩니다.

특정 Device_ID에 해당하는 모델을 삭제하려면 `moreh-smi device rm {Device_ID}` 명령어를 입력하세요.

- `moreh-smi device rm {Device_ID}` 입력 예시
    
    ```bash
    moreh-smi rm 2026
    ```
    

아래 명령어를 입력하면 디바이스 목록의 모든 모델들을 삭제합니다.

- `moreh-smi device rm --all`

## 3. KT AI Accelerator 생성된 디바이스 변경하기

**`moreh-smi device --switch {Device_ID}`** 명령어를 입력하면 이미 생성된 디바이스의 ID에 해당하는 디바이스로 변경됩니다.

- `moreh-smi device --switch {Device_ID}` 입력 예시
    
    ```bash
    moreh-smi device --switch 2027
    ```
    

기존 디바이스에서 2027 ID에 해당하는 디바이스로 변경됩니다.

## 4. KT AI Accelerator 디바이스의 활용 상태 모니터링하기

**`moreh-smi -i {Device_ID}`** 명령어로 딥러닝 모델 훈련에 사용하는 GPU 장치(디바이스)가 무엇인지, GPU Client Version과 Server Version 정보와 모델 훈련 중에 GPU의 총 메모리 중에서 현재 활용되고 있는 메모리와 성능이 어느 정도 인지 등을 모니터링할 때 moreh-smi 유틸리티를 사용합니다.

- **`moreh-smi -i {Device_ID}`**

```bash
moreh-smi -i 2026
```

위 명령어 입력시 아래와 같이 2026 device의 프로세스만 확인 가능합니다.

```bash
13:40:41 October 17, 2022 
+---------------------------------------------------------------------------------------------------+
|  Moreh-SMI 22.10.1                              Client Version: 22.10.1  Server Version: 22.10.2  |
+---------------------------------------------------------------------------------------------------+
|  Device  |        Name         |      Model     |  Memory Usage  |  Total Memory  |  Utilization  |
+===================================================================================================+
|  * 2026  |  KT AI Accelerator  |  Medium.128GB  |    22240 MiB   |   131040 MiB   |  -            |
+---------------------------------------------------------------------------------------------------+

Processes:
+----------------------------------------------------------+
|  Device  |  Job ID  |  PID  |  Process  |  Memory Usage  |
+==========================================================+
|    2026  |   37054  |  26515  |  python   |  22240 MiB   |
+----------------------------------------------------------+
```

---

## 기타 참고사항

- **한 토큰에 디바이스 생성 limit**
    - `moreh-smi` 커멘드 입력 시 출력 목록에 디바이스가 최대 생성 개수 N개가 있으면 더 이상 생성이 실패하고 제거만 되도록 설정됩니다.
    - 디바이스 최대 개수 생성 초과 시 오류 메시지가 등장합니다.
- **디바이스 생성 후 자동으로 제거**
    - 디바이스 모델이 자동적으로 할당되고 해제되어 자원 사용이 유동적입니다.



---

Copyright © 2022 Moreh Corporation. All rights reserved.