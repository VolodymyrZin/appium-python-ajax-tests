import logging
from colorama import Fore, Style, init

init(autoreset=True)


class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, "")
        message = super().format(record)
        return color + message + Style.RESET_ALL


def get_logger(name="test_logger"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # file handler
    file_handler = logging.FileHandler("test_logs.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    # console handler (colored)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColorFormatter("%(levelname)s | %(message)s"))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = get_logger()
