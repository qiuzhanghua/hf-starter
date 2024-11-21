import logging
import yaml
import logging.config
import os

from utils.hf_cache import find_hf_hub_dir, find_hf_datasets_dir, find_hf_home_dir

if __name__ == '__main__':

    current_file_path = os.path.abspath(__file__)
    log_dir = os.path.join(os.path.dirname(current_file_path), "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = None
    with open("logging_config.yaml", "r", encoding="utf8") as f:
        logging_config = yaml.safe_load(f)
        logging.config.dictConfig(logging_config)
        logger = logging.getLogger("app")

    print(find_hf_hub_dir())
    print(find_hf_datasets_dir())
    print(find_hf_home_dir())
    logger.info("Hello World")
