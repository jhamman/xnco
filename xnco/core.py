
import os
import sys
import logging

from dask.distributed import Client


def get_client(scheduler):
    if scheduler is False:
        client = None
    elif os.path.isfile(scheduler):
        client = Client(scheduler_file=scheduler)
    else:
        client = Client(scheduler)

    return client


def get_logger(filename, log_level):
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(' - '.join(
        ["%(asctime)s", "%(name)s", "%(levelname)s", "%(message)s"]))
    ch.setFormatter(formatter)
    logger = logging.getLogger(filename)
    logger.setLevel(log_level)
    ch.setLevel(log_level)
    logger.addHandler(ch)
    return logger
