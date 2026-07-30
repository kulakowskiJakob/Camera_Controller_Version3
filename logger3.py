import logging
import os

import config

class Logger:

    def __init__(self):

        self.logger = logging.getLogger(
            "PiCameraServer"
        )

        self.logger.setLevel(
            logging.DEBUG
        )

        if not self.logger.handlers:

            file_handler = logging.FileHandler(
                config.LOG_FILE
            )

            file_handler.setLevel(
                logging.DEBUG
            )

            console_handler = logging.StreamHandler()

            console_handler.setLevel(
                logging.INFO
            )

            formatter = logging.Formatter(
                "%(asctime)s | "
                "%(levelname)s |"
                "%(message)s"
            )

            file_handler.setFormatter(
                formatter
            )

            console_handler.setFormatter(
                formatter
            )

            self.logger.addHandler(
                file_handler
            )

            self.logger.addHandler(
                console_handler
            )

    def get_logger(self):

        return self.logger


logger = Logger().get_logger()