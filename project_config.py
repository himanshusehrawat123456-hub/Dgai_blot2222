"""
DG AI Enterprise Platform
Project Configuration

Version : 1.0.0
Status  : Production Foundation
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProjectConfig:
    """Global configuration for the DG AI platform."""

    PROJECT_NAME: str = "DG AI"
    VERSION: str = "1.0.0"
    ORGANIZATION: str = "DG AI"

    ROOT_DIR: Path = Path(__file__).resolve().parent.parent
    CONFIG_DIR: Path = ROOT_DIR / "configs"
    DOCS_DIR: Path = ROOT_DIR / "docs"
    LOGS_DIR: Path = ROOT_DIR / "logs"
    DATA_DIR: Path = ROOT_DIR / "data"
    TEMP_DIR: Path = ROOT_DIR / "temp"

    DEBUG: bool = True
    TESTING: bool = False


config = ProjectConfig()
