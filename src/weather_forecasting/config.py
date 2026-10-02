from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / "configs"


def load_config(filename: str = "base.yaml") -> dict:
    config_path = CONFIG_DIR / filename

    with config_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)
