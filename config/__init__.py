#!/usr/bin/env python
'''
  Config
  author:  y.wang
  date:    2017-06-27
'''

import os
import configparser
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../../../.env')
dotenv.load_dotenv(dotenv_path)

conf = configparser.ConfigParser()
conf_dir = os.path.join(os.path.dirname(__file__))

if os.environ.get('PYTHON_ENV') == 'production':
    print('>>> load prod.conf')
    conf.read(os.path.join(conf_dir, 'prod.conf'))
elif os.environ.get('PYTHON_ENV') == 'test':
    print('>>> load test.conf')
    conf.read(os.path.join(conf_dir, 'test.conf'))
else:
    print('>>> load dev.conf')
    conf.read(os.path.join(conf_dir, './dev.conf'))
