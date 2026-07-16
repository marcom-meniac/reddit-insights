"""
logging_config.py

Centralized logging configuration for the
Reddit Marketing Intelligence application.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from config import LOG_LEVEL, LOG_FILE

# =============================================================================
# Log Directory
# =============================================================================

LOG_PATH = Path(LOG_FILE)

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

# =============================================================================
# Log Format
# =============================================================================

LOG_FORMAT = (
    "%(asctime)s | %(levelname)-8s | "
    "%(name)s | %(message)s"
)

FORMATTER = logging.Formatter(LOG_FORMAT)

# =============================================================================
# Console Handler
# =============================================================================

console_handler = logging.StreamHandler()
console_handler.setFormatter(FORMATTER)

# =============================================================================
# File Handler
# =============================================================================

file_handler = RotatingFileHandler(
    LOG_PATH,
    maxBytes=5 * 1024 * 1024,
    backupCount=3,
    encoding="utf-8",
)

file_handler.setFormatter(FORMATTER)

# =============================================================================
# Root Logger
# =============================================================================

logger = logging.getLogger()

logger.setLevel(LOG_LEVEL)

if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

logger.info("Logging initialized successfully.")