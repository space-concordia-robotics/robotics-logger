import logging
import os
import errno
import datetime

def get_timestamped_filepath():
    """ Gets a timestamped filepath for the logfiles """
    return os.path.join(os.path.expanduser('~'), '.config', 'rover', 'logs')

def try_create_path(path, filename):
    """ Tries to create a directory at 'path' and returns the directory + filename """
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

    return os.path.join(path, datetime.date.today().isoformat() + "." + filename + ".log")

class RoboticsFileHandler(logging.FileHandler):
    """ Custom logger file handler that creates the file in a predefined and timestamped folder structure. Only unix-like supported for now """
    def __init__(self, filename, mode = 'a', encoding = None, delay = 0):
        try:
            full_path = try_create_path(get_timestamped_filepath(), filename)
            logging.FileHandler.__init__(self, full_path, mode, encoding, delay)
        except OSError as e:
            print "OS error on try to create directory. Aborting file handler creation"
