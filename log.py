#-*- coding:utf-8 -*-

import logging
"""
默认生成的root logger的level是logging.WARNING,低于该级别的就不输出了

级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

%(levelno)s：打印日志级别的数值
%(levelname)s：打印日志级别的名称
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s：打印当前执行程序名
%(funcName)s：打印日志的当前函数
%(lineno)d：打印日志的当前行号
%(asctime)s：打印日志的时间
%(thread)d：打印线程ID
%(threadName)s：打印线程名称
%(process)d：打印进程ID
%(message)s：打印日志信息
"""
logging.basicConfig(level = logging.NOTSET,filename='log.txt',filemode='a',format = '%(asctime)s  %(levelname)s  %(message)s')
log = logging.getLogger(__name__)
