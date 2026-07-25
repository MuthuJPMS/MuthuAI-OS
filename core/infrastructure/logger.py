import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from core.infrastructure.config import config


class LoggerManager:

    def __init__(self):

        self._logger = None

        self._initialize()


    def _initialize(self):

        if self._logger is not None:
            return


        config.LOG_DIR.mkdir(parents=True, exist_ok=True)

        log_file = Path(config.LOG_DIR) / "muthuai.log"


        logger = logging.getLogger("MuthuAI")

        logger.setLevel(logging.INFO)

        logger.handlers.clear()


        formatter = logging.Formatter(

            "[%(asctime)s] "

            "[%(levelname)s] "

            "[%(name)s] "

            "%(message)s"

        )


        file_handler = RotatingFileHandler(

            log_file,

            maxBytes=5 * 1024 * 1024,

            backupCount=5,

            encoding="utf-8"

        )

        file_handler.setFormatter(formatter)


        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)


        logger.addHandler(file_handler)

        logger.addHandler(console_handler)


        self._logger = logger


    @property
    def logger(self):

        return self._logger


    def info(self, message):

        self.logger.info(message)


    def warning(self, message):

        self.logger.warning(message)


    def error(self, message):

        self.logger.error(message)


    def critical(self, message):

        self.logger.critical(message)


    def debug(self, message):

        self.logger.debug(message)


logger = LoggerManager()