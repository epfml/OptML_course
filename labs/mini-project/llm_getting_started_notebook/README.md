# A notebook for LLM training

The notebook will show you how to train a GPT2-like model from scratch, in a reasonable time, and without needing a whole compute cluster.
You can modify the optimizers to see how different optimizers (such as from PyTorch) behave during the training.

For some similar resources, see also 
- https://github.com/kellerjordan/modded-nanogpt (speed run competition)
- https://github.com/karpathy/autoresearch (same but in a loop for agent-assisted edits of the recipe)
- https://github.com/epfml/llm-baselines (based on nanoGPT as above, with some useful hyperparameters)

We recommend running this notebook on the EPFL RCP or scitas clusters, with a single A100 GPU (smaller or older GPUs can work as well), or alternatively on. Here is an example how to submitting an RCP interactive training job. Do not forget to kill the runai job after use, as the GPU hour costs money and competes for resources with other researchers:

```
runai submit \
        --name <pod-name> \
        --interactive \
        --image ic-registry.epfl.ch/ivrl/pajouheshgar/pytorch2.1jax:cuda12.1v1 \ # An example of the image, good starting point.
        --gpu 1 \
        --large-shm \
        --node-pools default \
        --existing-pvc claimname=<>,path=<> \
        --environment CLUSTER_USER=<user_name> \
        --environment CLUSTER_USER_ID=<user_id> \
        --environment CLUSTER_GROUP_NAME=<group_name> \
        --environment CLUSTER_GROUP_ID=<group_id> \
        --command \
        -- /bin/bash -c 'source /opt/lab/setup.sh && pip install --upgrade jupyterlab && su <user_name> -c "jupyter lab --ip=0.0.0.0 --no-browser --notebook-dir=/"'
```

The information for filling out the blank fields will come with the RCP access. We provide an install.sh file for necessary dependencies. 

The notebook could also be run on a Google Colab environment, or in the EPFL gnoto.epfl.ch system (you have access). However, the free session of Colab only supports a T4 GPU, and it will be slow to run the training on it.
