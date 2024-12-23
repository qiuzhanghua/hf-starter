import logging
import logging.config
import os

import click
import yaml
import torch

from tjutil import find_hf_hub_dir, find_hf_datasets_dir, find_hf_home_dir

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)


@click.command()
@click.option("--epochs", "-e", help="Epochs", type=int, default=10)
def main(epochs):
    current_file_path = os.path.abspath(__file__)
    log_dir = os.path.join(os.path.dirname(current_file_path), "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    with open("config/logging.yaml", "r", encoding="utf8") as f:
        logging_config = yaml.safe_load(f)
        logging.config.dictConfig(logging_config)
        logger = logging.getLogger("app")

    logger.info(f"Hugging Face Home Dir: {find_hf_home_dir()}")
    logger.info(f"Hugging Face Hub Dir: {find_hf_hub_dir()}")
    logger.info(f"Hugging Face Datasets Dir: {find_hf_datasets_dir()}")
    logger.info(f"Default Device: {device}")
    logger.info(f"epochs: {epochs}")
    logger.info("begin training ...")
    for i in range(epochs):
        logger.info(f"Epoch {i + 1}/{epochs}")
    logger.info("end training.")


if __name__ == "__main__":
    main()
