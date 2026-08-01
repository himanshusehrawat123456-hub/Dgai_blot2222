"""
DG AI Enterprise Platform
Kernel Constants

Version : 1.0.0
Status  : Production Foundation
"""

from enum import Enum

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

PROJECT_NAME = "DG AI"
PROJECT_VERSION = "1.0.0"
PROJECT_AUTHOR = "DG AI"
PROJECT_LICENSE = "Proprietary"

# ==========================================================
# KERNEL STATUS
# ==========================================================

class KernelStatus(str, Enum):
    CREATED = "CREATED"
    INITIALIZING = "INITIALIZING"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    FAILED = "FAILED"

# ==========================================================
# ENVIRONMENTS
# ==========================================================

class Environment(str, Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"

# ==========================================================
# LOG LEVELS
# ==========================================================

class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

# ==========================================================
# DEFAULT VALUES
# ==========================================================

DEFAULT_ENCODING = "utf-8"
DEFAULT_TIMEZONE = "UTC"
DEFAULT_LANGUAGE = "en"

# ==========================================================
# EXIT CODES
# ==========================================================

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_CONFIGURATION_ERROR = 2
EXIT_RUNTIME_ERROR = 3
