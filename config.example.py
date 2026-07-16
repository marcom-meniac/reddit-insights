"""
config.example.py

Example configuration for the Reddit Marketing Intelligence application.

Copy this file to `config.py` or configure the values using
environment variables before running the application.
"""

import os
from dotenv import load_dotenv

# =============================================================================
# Load Environment Variables
# =============================================================================

load_dotenv()

# =============================================================================
# Reddit API Configuration
# =============================================================================

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")

USERNAME = os.getenv("REDDIT_USERNAME", "")
PASSWORD = os.getenv("REDDIT_PASSWORD", "")

USER_AGENT = os.getenv(
    "REDDIT_USER_AGENT",
    "Marketing Intelligence Research Tool v1.0"
)

# =============================================================================
# Database Configuration
# =============================================================================

DB_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://username:password@localhost:5432/marketing_intelligence"
)

# =============================================================================
# Reddit Data Collection
# =============================================================================

DEFAULT_SUBREDDITS = [
    "sysadmin",
    "devops",
    "aws",
    "azure",
    "gcp",
    "cloud",
    "kubernetes",
    "networking",
    "cybersecurity",
    "datacenter",
    "selfhosted",
    "storage",
    "linux",
    "vmware",
    "artificial",
    "machinelearning"
]

DEFAULT_SORT = "hot"

DEFAULT_POST_LIMIT = 50

REQUEST_TIMEOUT = 30

REQUEST_DELAY = 2

# =============================================================================
# Feature Flags
# =============================================================================

ENABLE_SENTIMENT_ANALYSIS = True

ENABLE_TOPIC_CLASSIFICATION = True

# =============================================================================
# Output
# =============================================================================

OUTPUT_DIRECTORY = "output"

# =============================================================================
# Logging
# =============================================================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

LOG_FILE = "logs/reddit_app.log"