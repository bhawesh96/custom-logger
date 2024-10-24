# Logger Class Documentation

## Installation

```bash
pip install git+https://git@github.com/bhawesh96/custom-logger.git
```

## Overview

The `Logger` class is a Python utility designed to simplify logging within applications. It provides a flexible and easy-to-use interface for logging information, warnings, errors, debugging messages, and custom banners.

## Features

- **Automatic Log File Generation:** The class automatically generates log filenames based on the provided log name and the current date and time.

- **Configurable Logging Directory:** Users can specify a custom log directory, and if not provided, a default "log" directory in the current working directory will be used.

- **Logging Levels:** Supports standard logging levels such as INFO, WARNING, ERROR, and DEBUG.

- **Console and File Logging:** Logs are simultaneously output to both the console and a file for easy access and troubleshooting.

- **Custom Banners:** Includes a utility method for logging custom banners with a consistent format.

## Usage

### Initialization

```python
from custom_logger import Logger, LogLevel

# Create a Logger instance with default values
logger = Logger()

# Create a Logger instance with a custom log name and directory
logger = Logger(log_name="my_app", log_dir="/path/to/logs", log_level=LogLevel.INFO)

# log a step without step number
logger.step('Download the app')

# log a step with step number
logger.step('Install the app', 1)

# Log a message at INFO level
logger.info('This is an info message')

# Log a message at ERROR level
logger.info('This is an error message')

# Log a banner for marking the start / end of a section
logger.small_banner("Small important Section")

# Log a banner for marking the start / end of a section
logger.big_banner("Big important Section")
```

### Output
```
2023-12-12 14:52:34,769 [INFO] STEP: Download the app
2023-12-12 14:52:34,769 [INFO] STEP 1: Install the app
2023-12-12 14:52:34,770 [INFO] This is an info message
2023-12-12 14:52:34,770 [INFO] ******************** SMALL IMPORTANT SECTION ********************
2023-12-12 14:52:34,770 [INFO] 
********************************************************************************
**                             BIG IMPORTANT SECTION                             **
********************************************************************************
```

## File naming convention
_\<log_name>\_\<formatted_date_time>.log_

Example: app_12_04_2023_14_30_45.log

## Want to request a feature?
Raise an issue [here](https://github.com/bhawesh96/custom-logger/issues) or directly raise a pull request adhering to community standards
