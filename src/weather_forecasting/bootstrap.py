from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_URL = "https://github.com/iamdrzazgowski/weather-forecasting-thesis.git"
REPO_DIR = Path("/content/weather-forecasting-thesis")
SRC_DIR = REPO_DIR / "src"


def run(command: list[str]) -> None:
    print("$", " ".join(command))
    subprocess.run(command, check=True)


def setup_colab() -> Path:
    print("=== Weather Forecasting Thesis — Colab Bootstrap ===")

    # 1. Clone repository if necessary
    if not REPO_DIR.exists():
        print("\n[1/6] Cloning repository...")
        run([
            "git",
            "clone",
            REPO_URL,
            str(REPO_DIR),
        ])
    else:
        print("\n[1/6] Repository already exists.")

        # Update repository
        print("Updating repository...")
        run([
            "git",
            "-C",
            str(REPO_DIR),
            "pull",
            "--ff-only",
        ])

    # 2. Add src to Python path
    print("\n[2/6] Configuring Python path...")

    if str(SRC_DIR) not in sys.path:
        sys.path.insert(0, str(SRC_DIR))

    print(f"Python path: {SRC_DIR}")

    # 3. Install project dependencies
    print("\n[3/6] Installing project dependencies...")

    run([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-e",
        str(REPO_DIR),
        "--quiet",
    ])

    # 4. Test project import
    print("\n[4/6] Testing project import...")

    from weather_forecasting.config import load_config

    config = load_config()

    print("weather_forecasting: OK")
    print(f"Config: {config}")

    # 5. Check GPU
    print("\n[5/6] Checking GPU...")

    try:
        import torch

        print(f"PyTorch: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")

        if torch.cuda.is_available():
            print(f"GPU: {torch.cuda.get_device_name(0)}")
        else:
            print("GPU: not available")

    except ImportError:
        print("PyTorch is not installed.")

    # 6. Final information
    print("\n[6/6] Environment information...")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Executable: {sys.executable}")
    print(f"Repository: {REPO_DIR}")

    print("\n✅ Colab bootstrap completed.")

    return REPO_DIR