import logging
import time

class Logger(logging.getLoggerClass()):
    logfile = ""

    def __init__(self, name="log.txt"):
        self.logfile = name
        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                            filename=name,
                            level=logging.DEBUG)

    " Used to log information."
    def i(self, message):
        logging.info(message)

    " Used to log warnings."
    def w(self):
        logging.warning(message)

    " Used to log errors."
    def e(self):
        logging.error(message)

    " Used to log critical errors."
    def c(self):
        logging.critical(message)

    " Shutdown logger gracefully."
    def shutdown(self):
        pass
