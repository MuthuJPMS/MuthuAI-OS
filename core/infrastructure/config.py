import os
from pathlib import Path


class Config:

    PROJECT_NAME = "MuthuAI OS"

    VERSION = "2.0.0"

    ENVIRONMENT = os.getenv("MUTHUAI_ENV", "development")

    DEBUG = ENVIRONMENT == "development"

    ROOT_DIR = Path(__file__).resolve().parents[2]

    DATA_DIR = ROOT_DIR / "data"

    LOG_DIR = ROOT_DIR / "logs"

    CACHE_DIR = ROOT_DIR / "cache"

    TEMP_DIR = ROOT_DIR / "temp"

    DATABASE_DIR = ROOT_DIR / "database"

    BACKUP_DIR = ROOT_DIR / "backup"

    MAX_WORKERS = 8

    DEFAULT_LANGUAGE = "en"

    DEFAULT_TIMEZONE = "Asia/Kolkata"

    MEMORY_LIMIT_MB = 2048

    ENABLE_EVENT_BUS = True

    ENABLE_KNOWLEDGE_GRAPH = True

    ENABLE_LEARNING = True

    ENABLE_SECURITY = True

    ENABLE_TOOL_SYSTEM = True

    ENABLE_ANALYTICS = True

    @classmethod
    def initialize(cls):

        directories = [

            cls.DATA_DIR,

            cls.LOG_DIR,

            cls.CACHE_DIR,

            cls.TEMP_DIR,

            cls.DATABASE_DIR,

            cls.BACKUP_DIR

        ]

        for directory in directories:

            directory.mkdir(parents=True, exist_ok=True)


config = Config()

config.initialize()