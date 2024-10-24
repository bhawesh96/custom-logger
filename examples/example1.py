from src.custom_logger import Logger, LogLevel

logger = Logger('hey', log_level=LogLevel.INFO)

# log a step without step number
logger.step('Download the app')

# log a step with step number
logger.step('Install the app', 1)

# Log a message at INFO level
logger.info('This is an info message')

# Log a message at ERROR level
logger.info('This is an error message')

# Log a banner for marking the start / end of a section
logger.small_banner("Important Section")

# Log a banner for marking the start / end of a section
logger.big_banner("Important Section")