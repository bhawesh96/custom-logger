import datetime
import logging
import os


class LogLevel:
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    WARN = logging.WARN
    ERROR = logging.ERROR


class Logger():
    def __init__(self, log_name="app", log_dir=None, log_level=LogLevel.INFO):
        self.log_filename = self.__generate_log_filename(log_name)
        if log_dir is None:
            log_dir = os.path.join(os.curdir, 'log')
        self.log_dir = os.path.join(log_dir, self.log_filename.split('.log')[0])

        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        try:
            self.__configure_logging(_level=log_level)
        except FileNotFoundError:
            os.mkdir(self.log_dir)
            self.__configure_logging(_level=log_level)

    def get_log_dir(self):
        """
        Get the log directory
        :return: the log directory
        """
        return self.log_dir

    @staticmethod
    def __generate_log_filename(log_name):
        """
        Generate the log filename
        :return: the log filename
        """
        current_datetime = datetime.datetime.now()
        formatted_date_time = current_datetime.strftime('%d_%m_%Y_%H_%M_%S')
        return f'{log_name}_{formatted_date_time}.log'

    def __configure_logging(self, _level=LogLevel.INFO):
        """
        Configure logging
        """
        logging.basicConfig(level=_level, format="%(asctime)s [%(levelname)s] %(message)s",
                            handlers=[logging.FileHandler(os.path.join(self.log_dir, self.log_filename)),
                                      logging.StreamHandler()])

    def info(self, msg):
        """
        Log an info message
        :param msg: the message to be logged
        """
        logging.info(msg)

    def warn(self, msg):
        """
        Log a warn message
        :param msg: the message to be logged
        """
        logging.warning(msg)

    def error(self, msg):
        """
        Log a error message
        :param msg: the message to be logged
        """
        logging.error(msg)

    def debug(self, msg):
        """
        Log a debug message
        :param msg: the message to be logged
        """
        logging.debug(msg)

    def small_banner(self, msg):
        """
        Log a small banner
        :param msg: the message to be logged inside the banner
        """
        message_length = len(msg)
        num_asterisks = 60
        asterisks_on_each_side = (num_asterisks - message_length - 2) // 2

        banner = f"{'*' * asterisks_on_each_side} {msg.upper()} {'*' * asterisks_on_each_side}"

        logging.info(banner)

    def big_banner(self, msg):
        """
        Log a big banner
        :param msg: the message to be logged inside the banner
        """
        message_length = len(msg)
        num_asterisks = 80
        asterisks_on_each_side = (num_asterisks - message_length - 4) // 2

        banner = f"\n{'*' * num_asterisks}\n{'*' * 2}" \
                 f"{' ' * asterisks_on_each_side}" \
                 f"{msg.upper()}" \
                 f"{' ' * asterisks_on_each_side}" \
                 f"{'*' * 2}\n{'*' * num_asterisks}\n"

        logging.info(banner)

    def step(self, msg, step_num=-1):
        """
        Log the steps of the program
        :param msg: the message describing the step
        :param step_num: step number
        """
        if step_num == -1:
            self.info(f'STEP: {msg}')
        else:
            self.info(f'STEP {step_num}: {msg}')
