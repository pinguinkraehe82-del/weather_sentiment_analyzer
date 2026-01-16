import logging.config
import os
from pathlib import Path

def setup_logging():
    PROJECT_ROOT = Path(__file__).parent.parent
    LOG_DIR = PROJECT_ROOT / "logging"

    LOGGING_INI = PROJECT_ROOT / "logging" / "logging.ini"

    # Set environment variable for log path
    os.environ["LOG_FILE_PATH"] = str(LOG_DIR / "app.log")

    logging.config.fileConfig(str(LOGGING_INI))