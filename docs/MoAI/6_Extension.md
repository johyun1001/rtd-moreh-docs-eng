# MoAI Pytorch extension

이 문서는 Moreh AI Framework에서 어떻게 NVIDIA APEX(A PyTorch EXtention)와 같은 기능을 사용하는지 대한 설명이 담겨있는 페이지입니다.

## NVIDIA APEX란?

NVIDIA APEX는 모델 학습 시 사용되는 Mixed Precision 기능 및 다양한 기능들을 Pytorch에서 간편하게 사용할 수 있도록 만들어진 확장 라이브러리입니다.

- https://github.com/NVIDIA/apex

## Moreh APEX 소개

Moreh 솔루션에서도 APEX 기능을 사용하실 수 있으며, 다음과 같이 NVIDIA APEX 코드를 대체할 수 있습니다. 더 좋은 점은 **Moreh 솔루션에서는 NVIDIA APEX 라이브러리를 설치하실 필요 없다는 것입니다**. 아래는 일반적인 NVIDIA APEX 코드 사용법과 이를 어떻게 Moreh APEX로 교체하는지 방법을 서술합니다.

## Distributed Data Parallel (DDP)
DDP는 NVIDIA APEX에서 제공하는 대표적인 기능중 하나이며, Pytorch에서도 기본적으로 DDP 기능을 제공하고 있습니다. 아래는 두가지 라이브러리에 대한 각각의 예시코드입니다.

- **NVIDIA APEX DDP** example pseudocode

```python
from apex.parallel import DistributedDataParallel

parser = argparse.ArgumentParser()

# FOR DISTRIBUTED:  Parse for the local_rank argument, which will be supplied

# automatically by torch.distributed.launch.

parser.add_argument("--local_rank", default=0, type=int)

args = parser.parse_args()

# WORLD_SIZE is define numbers of GPU 
args.distributed = False
if 'WORLD_SIZE' in os.environ:
    args.distributed = int(os.environ['WORLD_SIZE']) > 1

if args.distributed:
    # FOR DISTRIBUTED:  After amp.initialize, wrap the model with
    # apex.parallel.DistributedDataParallel.
    model = DistributedDataParallel(model)

# Start to training model
model.fit(x_train, y_train)
```

- **Pytorch DDP** example code

```python
import torch
import torch.distributed as dist
import torch.multiprocessing as mp
import torch.nn as nn
import torch.optim as optim
from torch.nn.parallel import DistributedDataParallel as DDP

def example(rank, world_size):
    # create default process group
    dist.init_process_group("gloo", rank=rank, world_size=world_size)
    # create local model
    model = nn.Linear(10, 10).to(rank)
    # construct DDP model
    ddp_model = DDP(model, device_ids=[rank])
    # define loss function and optimizer
    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(ddp_model.parameters(), lr=0.001)

    # forward pass
    outputs = ddp_model(torch.randn(20, 10).to(rank))
    labels = torch.randn(20, 10).to(rank)
    # backward pass
    loss_fn(outputs, labels).backward()
    # update parameters
    optimizer.step()

def main():
    world_size = 2
    mp.spawn(example,
        args=(world_size,),
        nprocs=world_size,
        join=True)

if __name__=="__main__":
    # Environment variables which need to be
    # set when using c10d's default "env"
    # initialization mode.
    os.environ["MASTER_ADDR"] = "localhost"
    os.environ["MASTER_PORT"] = "29500"
    main()
```

위 예시들처럼 DDP를 코드에 적용하기에는 다소 복잡한 부분이 존재합니다. 하지만, **Moreh 솔루션에서는 해당 기능을 사용하지않고 기본적으로 모든 데이터 처리를 DDP를 통합니다**. 따라서, Moreh 솔루션에서는 아래와 같이 DDP를 활용하는 코드를 없애도 무방합니다.

- **Moreh Solution** example code

```python
import torch
import torch.nn as nn
import torch.optim as optim
# -- Remove DDP library import --
# import torch.distributed as dist
# import torch.multiprocessing as mp
# from torch.nn.parallel import DistributedDataParallel as DDP

def example():
    # create local model
    model = nn.Linear(10, 10)
    # define loss function and optimizer
    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001)
    # backward pass
    loss_fn(outputs, labels).backward()
    # update parameters
    optimizer.step()

def main():
    example()

if __name__=="__main__":
    main()
```

## Mixed Precision

NVIDIA APEX에서 일반적인 Mixed Precision 사용방법은 다음과 같습니다.

- **NVIDIA APEX DDP** example code

```bash
from apex import amp

# Declare model and optimizer as usual, with default (FP32) precision
model = torch.nn.Linear(D_in, D_out).cuda()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

# Allow Amp to perform casts as required by the opt_level
model, optimizer = amp.initialize(model, optimizer, opt_level="O1")
...
# loss.backward() becomes:
with amp.scale_loss(loss, optimizer) as scaled_loss:
    scaled_loss.backward()
...
```

Moreh 솔루션에서의 Mixed Precision 사용방법은 다음과 같습니다. 위에서 설명드린것처럼, Moreh 솔루션은 별도의 NVIDIA APEX 라이브러리 설치가 필요없습니다. 따라서, Pytorch 라이브러리를 바로 사용합니다.

- **Moreh Solution** example code

```bash
import torch

# Declare model and optimizer as usual, with default (FP32) precision
model = torch.nn.Linear(D_in, D_out).cuda()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)
# 
amp = torch.moreh.apex.amp

# Allow Amp to perform casts as required by the opt_level
model, optimizer = amp.initialize(model, optimizer, opt_level="O1")
...
# loss.backward() becomes:
with amp.scale_loss(loss, optimizer) as scaled_loss:
    scaled_loss.backward()
...
```
## FusedLAMB

LAMB는 “Layer-wise Adaptive Moments optimizer for Batch training’의 약자이며, 비교적 큰 배치크기에서도 모델의 학습 속도를 안정적인 높이기 위해 사용하는 Optimizer중에 하나입니다.

NVIDIA APEX에서 일반적인 FusedLAMB Optimizer사용방법은 다음과 같습니다.

- **NVIDIA APEX FusedLAMB** example code

```bash
# (NVIDIA APEX 라이브러리 설치 필요)
import torch
from apex.multi_tensor_apply import multi_tensor_applier

# apex.optimizers.FusedLAMB의 사용법은 일반 Pytorch optimizer 동일
# Amp와 함께 FusedLAMB를 사용하려면 원하는 opt_level을 선택 가능

opt = apex.optimizers.FusedLAMB(model.parameters(), lr = ....)
model, opt = amp.initialize(model, opt, opt_level="O0" or "O1 or "O2")
...
opt.step()
```

Moreh 솔루션에서의 FusedLAMB Optimizer 간단한 사용 방법 예시는 다음과 같습니다. 해당 함수도 동일하게 별도 라이브러리 설치가 필요없습니다. `import torch`만으로 바로 사용이 가능합니다.

- **Moreh Solution** example code

```bash
import torch

...

# Declare model
model = torch.nn.Linear(D_in, D_out).cuda()

# In Moreh Solution, you have to add code like below for using FusedLAMB function
moreh_lamb = torch.ops.moreh.FusedLAMB
opt = moreh_lamb(model.parameter(), lr = 0.001)
```

