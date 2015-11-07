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


    def run(self, conn):
        msg = conn.recv()

        while msg[0] != "done":
            if msg[0] == "info":
                self.info(msg[1])

            elif msg[0] == "err":
                self.error(msg[1])

            elif msg[0] == "warn":
                self.warn(msg[1])

            elif msg[0] == "crit":
                self.crit(msg[1])
            
            else:
                error("Cannot log properly msg.")

            msg = conn.recv()

