#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 20:24
# @Author  : gaoxudong
# @File    : logger.py
# @Software: PyCharm
'''日志模块'''
import os
import logbook
from logbook.more import ColorizedStderrHandler
from functools import wraps
from config.config_T import logpath


check_path = logpath
LOG_DIR = os.path.join(check_path)
file_stream = True
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    file_stream = True


def get_logger(name='APPuiTest', file_log=file_stream, level='debug'):
    """ get logger Factory function """
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        os.path.join(LOG_DIR, '%s.log' % name),
        date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)


LOG = get_logger(file_log=file_stream, level='INFO')



def logger(param):
    """ fcuntion from logger meta """

    def wrap(function):
        """ logger wrapper """

        @wraps(function)
        def _wrap(*args, **kwargs):
            """ wrap tool """
            LOG.info("当前模块 {}".format(param))
            return function(*args, **kwargs)

        return _wrap

    return wrap
