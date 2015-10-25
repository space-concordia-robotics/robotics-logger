import logging
import time

class Logger(logging.getLoggerClass()):
    logfile = ""

    def __init__(self, name="log.txt"):
        self.logfile = name
        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                            filename=name,
                            filemode='w',
                            level=logging.DEBUG)

    " Used to log information."
    def info(self, msg):
        logging.info(msg)

    " Used to log warnings."
    def warn(self, msg):
        logging.warning(msg)

    " Used to log errors."
    def err(self, msg):
        logging.error(msg)

    " Used to log critical errors."
    def crit(self, msg):
        logging.critical(msg)

    " Shutdown logger gracefully."
    def shutdown(self):
        pass
