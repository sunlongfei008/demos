# -*- coding:utf8 -*-
# ***************************************************************************
# Create on 2015-12-10
#
# @Author:sunlf
#
# ***************************************************************************


import os
import logging

from config.dbconfig import *

ENV = "beta"

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOG_PATH = os.path.join(BASE_DIR, "logs/server.log")

LOG_CONSOLE = True

LOG_LEVEL = logging.INFO

ICE_CONFIG_PATH = os.path.join(BASE_DIR, "config/config.server")

INTERFACE_DIR = os.path.join(BASE_DIR, "interface")

INSTALLED_SERVANTS = (
    "libs.api.smsI.SmsSendI",
    )

REDIS_STORE = REDIS_LIST[ENV]
