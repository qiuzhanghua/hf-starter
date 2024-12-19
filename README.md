# Python Starter Project

## Requirement

```bash
pip i -r requirements.txt
```

## Features

1. logging
2. huggingface cache utils

## Run

```bash
python app.py
```

## Sample envs set by fish shell

```fish
set -x HF_HOME $HOME/ai/cache/huggingface
set -x HUGGINGFACE_HUB_CACHE $HOME/ai/cache/huggingface/hub
set -x HF_DATASETS_CACHE $HOME/ai/cache/huggingface/datasets

set -x HF_ENDPOINT https://hf-mirror.com

set -x PATH /usr/local/cuda-12.4/bin $PATH

if [ -z "$LD_LIBRARY_PATH" ]
        set -x LD_LIBRARY_PATH /usr/local/cuda-12.4/lib64
else
        set -x LD_LIBRARY_PATH /usr/local/cuda-12.4/lib64 $LD_LIBRARY_PATH
```

## download datasets

python

```python
from datasets import load_dataset

dataset = load_dataset('squad', download_mode='force_redownload')
# download to HF_DATASETS_CACHE
 ```

huggingface cli

```bash
huggingface-cli download --repo-type dataset wikitext
huggingface-cli download --repo-type dataset zalando-datasets/fashion_mnist
# ...
# download to HUGGINGFACE_HUB_CACHE
```

## download model
```bash
 huggingface-cli download THUDM/glm-4-9b-chat
```