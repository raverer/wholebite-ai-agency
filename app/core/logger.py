import logging
from pathlib import Path


class Logger:

    def __init__(self):

        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        logging.basicConfig(
            filename=log_dir / "wholebite.log",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

        self.logger = logging.getLogger("WholeBite")

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)


logger = Logger()