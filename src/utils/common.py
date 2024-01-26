import os
import yaml

from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox

from src.custom_logger import logger

@ensure_annotations
def read_yaml(file_path: Path):
    try:

        with open(file_path) as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return ConfigBox(content)

    except Exception as error:
        logger.error(f"Error reading yaml file: {error}")