# -*- coding: utf-8 -*-
import os

PORT = os.environ.get('APP_PORT', 8080)
SELENIUM_IMPLICIT_WAIT = os.environ.get('SELENIUM_IMPLICIT_WAIT', '0.1s')
SELENIUM_TIMEOUT = os.environ.get('SELENIUM_IMPLICIT_WAIT', '20s')

APP_HOST = os.environ.get('APP_HOST', "localhost")
APP_URL = os.environ.get('APP_URL', "http://%s:%s" % (APP_HOST, PORT))
BROWSER = os.environ.get('BROWSER', "Firefox")
REMOTE_URL = os.environ.get('REMOTE_URL', "")
DESIRED_CAPABILITIES = os.environ.get('DESIRED_CAPABILITIES', "")
