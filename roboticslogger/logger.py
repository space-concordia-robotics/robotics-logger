import logging
from roboticslogger.file_handler import RoboticsFileHandler

class Logger(logging.getLoggerClass()):
    logfile = ""

    def __init__(self, name="default"):
        self.logfile = name
        
        formatter = logging.Formatter(fmt = '%(asctime)s: %(levelname)s: %(message)s')
        roboticsFileHandler = RoboticsFileHandler(filename = name, mode = 'w')
        roboticsFileHandler.setFormatter(formatter)

        logging.getLogger('').addHandler(roboticsFileHandler)

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
        logging.shutdown()

    def run(self, conn):
        msg = conn.recv()

        while msg[0] != "done":
            if msg[0] == "info":
                self.info(msg[1])
            elif msg[0] == "err":
                self.err(msg[1])
            elif msg[0] == "warn":
                self.warn(msg[1])
            elif msg[0] == "crit":
                self.crit(msg[1])
            else:
                self.err("Failed to log message.")

            msg = []
            msg = conn.recv()

        self.shutdown()
        conn.close()
