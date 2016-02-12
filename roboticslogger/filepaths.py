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
