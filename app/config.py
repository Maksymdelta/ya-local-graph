# -*- coding: utf-8 -*-

import os

DB_USER = 'ya'
DB_PSWD = 'ya'
DB_NAME = 'ya'

DEBUG = False
CUSTOM_WAIT_TIMEOUT = (5, 15)
FIND_TIMEOUT = 15
REQUEST_TIMEOUT = 15
CHROME_DRIVER_PATH = os.path.sep.join([os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'chromedriver'])
HOST = 'https://music.yandex.ru'
DISPLAY = True
