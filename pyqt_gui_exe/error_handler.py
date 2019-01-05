#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import traceback
from logger import get_logger
import runtime_info

# ------------------------------------------------------------------------------
def try_except(actual_do):
    def handle_problems(*args, **keyargs):
        try:
            return actual_do(*args, **keyargs)
        except:
            exc_type, exc_instance, exc_traceback = sys.exc_info()
            formatted_traceback = ''.join(traceback.format_tb(exc_traceback))
            message = '\n{0}\n{1}: {2}'.format(
                formatted_traceback,
                exc_type.__name__,
                exc_instance
            )
            error_info = 'Error happened: %s\n\n' % message
            get_logger().error(error_info)
            runtime_info.global_runtime_info_queue.put(error_info)
        finally:
            pass
    return handle_problems