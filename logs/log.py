# coding=utf-8
'''
@Time   :2020/12/10 17:43
@Author :六月
@Email  :juneren26@gmail.com
@File   :log.py
@IDE    :PyCharm
'''

import logging
import os
import time
curPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

class Logger():
    def get_logger(self):
        # 创建日志对象
        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            sh = logging.StreamHandler()
            now = time.strftime('%Y_%m_%d %H_%M_%S')
            fh = logging.FileHandler('{}/logs/{}_log.log'.format(curPath,now),encoding='utf-8')
            fmt = logging.Formatter(fmt='[%(filename)s]:%(asctime)s - %(levelname)s - %(message)s')
            sh.setFormatter(fmt)
            sh.setLevel(logging.DEBUG)
            fh.setFormatter(fmt)
            fh.setLevel(logging.DEBUG)
            logger.addHandler(sh)
            logger.addHandler(fh)
        return logger

        # logger.info('this is info')
        # logger.warning('this is warning')
        # logger.debug('this is debug')