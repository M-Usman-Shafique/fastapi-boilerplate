import sys

from loguru import logger

from app.configs.settings import get_settings

settings = get_settings()

logger.remove()

logger.level("INFO", color="<blue>")
logger.level("SUCCESS", color="<green>")
logger.level("DEBUG", color="<YELLOW>")
logger.level("WARNING", color="<yellow>")
logger.level("ERROR", color="<red>")
logger.level("CRITICAL", color="<RED>")

FORMAT = (
    "<level>[{time:YYYY-MM-DD HH:mm:ss}]</level> "
    "<level>[{level}]</level> "
    "<level>{message}</level>"
)

LOG_LEVEL = "INFO" if settings.APP_ENV == "production" else "DEBUG"

logger.add(
    sys.stdout,
    format=FORMAT,
    colorize=True,
    level=LOG_LEVEL,
)

if settings.APP_ENV != "production":
    logger.add(
        "app.log",
        format=FORMAT,
        level="INFO",
        colorize=False,
        rotation="10 MB",
        retention="7 days",
        compression="zip",
    )
