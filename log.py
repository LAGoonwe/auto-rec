# coding=utf-8
import os
import sys
import platform
import logging
import datetime
from logging.handlers import RotatingFileHandler


class Log(object):
    logger = None

    @classmethod
    def create_log_file(cls):
        currenttime = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        currentplatform = platform.system()

        if currentplatform == 'Windows':
            logpath = os.path.abspath('./log')
            logpath = logpath.replace("\\", '/')
            logfile = str(logpath) + '/' + currenttime + '.log'
        else:
            logfile = '%s/%s.log' % (os.path.abspath(os.path.join(os.path.dirname(__file__), './', 'log')), currenttime)

        cls.logger = logging.getLogger(__name__)
        cls.logger.setLevel(logging.DEBUG)

        # log to file
        filehandle = RotatingFileHandler(
            logfile,
            maxBytes=20 * 1024 * 1024,
            backupCount=3,
            encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s::%(filename)s::%(funcName)s:: %(message)s\n')
        filehandle.setFormatter(formatter)
        cls.logger.addHandler(filehandle)

        # log to screen
        console = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s : %(message)s')
        console.setFormatter(formatter)
        cls.logger.addHandler(console)

if __name__ == '__main__':
    Log.create_log_file()
    Log.logger.debug("你好")
    Log.logger.info('info log')
