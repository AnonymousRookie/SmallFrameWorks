#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging as _logging
import threading
import os,time

# Don't use this directly. Use get_logger() instead.
_logger = None
_logger_lock = threading.Lock()

def get_logger():
    global _logger
    # Use double-checked locking to avoid taking lock unnecessarily.
    if _logger:
        return _logger
    _logger_lock.acquire()
    try:
        if _logger:
            return _logger
        logger = _logging.getLogger('SdmLogParser')
        logger.setLevel(_logging.INFO)
        log_path = './Logs/'
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_name = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        log_file = '{0}{1}.log'.format(log_path, log_name)
        handler = _logging.FileHandler(log_file, mode='a')
        handler.setLevel(_logging.INFO)
        strFmt = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        formatter = _logging.Formatter(strFmt)
        console = _logging.StreamHandler()
        console.setLevel(_logging.INFO)
        console.setFormatter(formatter)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(console)
        _logger = logger
        return _logger
    finally:
        _logger_lock.release()

# --------------------------------------------------------------------------------------------------
if __name__=="__main__":
    get_logger().warning("test warning log message")
    get_logger().fatal("test fatal log message")
    get_logger().error("test error log message")
    get_logger().info("test info log message")