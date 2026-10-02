from __future__ import annotations

import sys
from pathlib import Path


REPO_DIR = Path("/content/weather-forecasting-thesis")


def setup_colab() -> Path:
    print("=== Weather Forecasting Thesis — Colab Setup ===")

    # 1. Configure Python path
    print("\n[1/3] Configuring Python path...")

    src_dir = REPO_DIR / "src"

    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))

    print(f"Source: {src_dir}")

    # 2. Install project
    print("\n[2/3] Installing project...")

    import subprocess

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-e",
            str(REPO_DIR),
            "--quiet",
        ],
        check=True,
    )

    print("Project installed.")

    # 3. Verify environment
    print("\n[3/3] Checking environment...")

    from weather_forecasting.config import load_config

    config = load_config()

    print("weather_forecasting: OK")
    print(f"Config: {config}")

    try:
        import torch

        print(f"PyTorch: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")

        if torch.cuda.is_available():
            print(f"GPU: {torch.cuda.get_device_name(0)}")

    except ImportError:
        print("PyTorch is not installed.")

    print("\n✅ Colab environment ready.")

    return REPO_DIR