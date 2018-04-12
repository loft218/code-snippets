#-*-coding:utf-8-*-

import os
import logging
import logging.handlers
import re

#logging初始化工作
# logging.basicConfig()

#初始化
logger = logging.getLogger('task')
logger.setLevel(logging.DEBUG)

fileLogger = logging.handlers.TimedRotatingFileHandler(
    filename=os.path.join(os.path.dirname(__file__), 'out.log'),
    when='D',
    interval=1,
    backupCount=7,
    encoding='utf-8')
fileLogger.suffix = "%Y-%m-%d.log"
fileLogger.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}.log$")
fileLogger.setLevel(logging.INFO)

consoleLogger = logging.StreamHandler()
consoleLogger.setLevel(logging.DEBUG)

loggerFormater = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileLogger.formatter = loggerFormater
consoleLogger.formatter = loggerFormater

logger.addHandler(fileLogger)
logger.addHandler(consoleLogger)
