# encoding: utf-8

import logging as lg
import os
from datetime import datetime


def initialize_logger():
    # creating a folder for the logs
    logs_path = './logs/'  # define the path
    try:
        os.mkdir(logs_path)
    except OSError:
        print("Creation of the directory %s failed – it does not have to be bad" % logs_path)
    else:
        print("Successfully created log directory")

    # renaming each log depending on the time
    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_name = date + '.log'
    currentLog_path = logs_path + log_name

    # log parameters
    # level: Specifies the minimum logging level to be handled (e.g., logging.DEBUG, logging.INFO,
    # logging.WARNING, logging.ERROR, logging.CRITICAL).
    lg.basicConfig(filename=currentLog_path, format='%(asctime)s - %(levelname)s: %(message)s', level=lg.INFO)
    # Handlers define where log messages will be sent. They act as the output mechanism for the
    # logging system.
    lg.getLogger().addHandler(lg.StreamHandler())

    # init message
    lg.info('Log initialized')
