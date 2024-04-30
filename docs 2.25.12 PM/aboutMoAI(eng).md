
## **What is MoAI Platform?**

**MoAI(*Moreh AI appliance for AI accelerators*) Platform** is a scalable AI platform that enables easy control of thousands of Graphics Processing Units(GPUs) essential for developing large-scale deep learning models.

# **Core Technologies of MoAI Platform**

![](/docs/imgs/1.svg)

 As deep learning models evolve, they become increasingly complex and require substantial computational resources, with parameters expanding from billions to trillions. Developing large-scale models involves managing and processing an immense number of parameters, which is very challenging and time-consuming.

The MoAI Platform's automatic parallelization addresses these challenges by simultaneously processing multiple tasks, determining the optimal calculation method for large models. This allows users to focus solely on their core AI challenges, regardless of their application scale or processor type. Furthermore, it efficiently utilizes GPU computational resources at a reasonable cost by allocating them only during calculation execution.

---

## **Various Accelerators, Multi-GPU Support**

![](/docs/imgs/2.png)

- MoAI Platform supports various accelerators capable of executing various types of operations regardless of types of GPUs.
- Users can utilize different accelerators like Intel, AMD, and others alongside NVIDIA without needing to modify their code for deep learning development and model training.
- This compatibility allows for flexible development and training of deep learning models, accommodating multiple and diverse types of GPUs.

## **GPU/NPU Virtualization**

![Screenshot 2024-02-21 at 4.24.58 PM.png](/docs/imgs/3.png)

- The MoAI Platform's virtualization feature enables thousands of GPUs or NPUs to function as a single, more powerful GPU device.
    - This unique approach suggests that instead of managing a lot of individual units, users can handle this collective resource as single entity, considerably simplifying complex tasks.
- It simplifies the process of modeling and optimization, providing users with a seamless and efficient experience.
    - By abstracting the complexity of utilizing multiple GPUs or NPUs, it enables easier management and deployment of resources for enhanced performance in deep learning tasks.

## **AI Compiler**

- In the era of AI, training and inference of large-scale models such as LLM(Large language Model) and LMM(Large Multimodal Model) require significantly large GPU clusters and effective GPU parallelization.
- Currently, most AI frameworks used with NVIDIA require manual parallelization by AI engineers depending on the size and complexity of the model and the available GPU size/cluster. This setup process is time-consuming, often taking weeks to complete.
- The MoAI Platform offers automatic parallelization can be achieved through a Moreh AI compiler that finds out the optical way to use GPU resources based on the the specific AI model and the size of GPU cluster.
- This can significantly shorten the setup and deployment time for AI models, from several weeks, as with NVIDIA, to only 2-3 days.

## **Dynamic GPU Allocation**

![Screenshot 2024-02-21 at 4.27.05 PM.png](/docs/imgs/4.png)

- On the MoAI platform, AI engineers can begin deep learning training with exactly the amount of GPU resources as needed.
- GPU resources are only allocated during computation execution, allowing for efficient use of GPU resources. This not only reduces software development cost, but also saves time for development and deployment.