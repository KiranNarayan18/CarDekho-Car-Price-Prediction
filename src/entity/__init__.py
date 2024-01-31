## config entity 
from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    clean_dir: Path
    schema: dict
    target_column: str
    columns_to_drop: list


@dataclass(frozen=True)
class DataTransformationConfig:
    data_dir: Path
    transformed_dir: Path
    target_column: str