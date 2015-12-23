#!/usr/bin/env python
# -*- coding:utf8 -*-
# ***************************************************************************
# Create on 2015-12-09
#
# @Author:sunlf
#
# ***************************************************************************
import os
import sys
import logging
import importlib

import Ice

from config import setting
from utils.init_system import init_logging


class Server(Ice.Application):
    def __init__(self, interface_path, servants):
        self._load_interface_files(interface_path)
        self.servants = servants

    def run(self, args):
        if len(args) > 1:
            logging.error(self.appName() + ": too many arguments")
            return 1
        adapter = self._create_adapter("Adapter")
        self._add_servant(adapter, self.servants)
        adapter.activate()
        self._show_listen_port(adapter)
        try:
            self.communicator().waitForShutdown()
        except:
            logging.exception("communicator:")

        if self.interrupted():
            logging.error(self.appName() + ": terminating")

        return 0

    def _create_adapter(self, adapter_name):

        return self.communicator().createObjectAdapter(adapter_name)

    def _add_servant(self, adapter, servants):
        '''自动增加servant'''
        for servant in servants:
            module_name = servant[:servant.rindex(".")]
            class_name = servant[servant.rindex(".") + 1:]
            module = importlib.import_module(module_name)
            servant_instance = getattr(module, class_name)()
            servant_name = servant_instance.servant_name()
            adapter.add(servant_instance,
                        self.communicator().stringToIdentity(servant_name))

    def _show_listen_port(self, adapter):
        endPoints = adapter.getEndpoints()[0].toString()
        port = endPoints.split()[2]
        logging.info("Server listening on %s..." % port)

    def _load_interface_files(self, interface_path):
        '''自动添加接口文件'''
        if os.path.exists(interface_path):
            files = os.listdir(interface_path)
            for fname in files:
                if fname.endswith(".ice"):
                    file_path = os.path.join(interface_path, fname)
                    try:
                        Ice.loadSlice(file_path)
                        return True
                    except:
                        pass
                logging.warning("Invalid file cannot be loaded, file=%s" %
                                fname)
        else:
            logging.warning("Interface file directory does not exist")

        return False


def main():
    init_logging(setting.LOG_PATH, setting.LOG_CONSOLE, setting.LOG_LEVEL)
    app = Server(setting.INTERFACE_DIR, setting.INSTALLED_SERVANTS)
    sys.exit(app.main(sys.argv, setting.ICE_CONFIG_PATH))


if __name__ == "__main__":
    main()
