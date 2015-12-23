#!/usr/bin/env python
# -*- coding:utf8 -*-
# ***************************************************************************
# Create on 2015-12-09
#
# @Author:sunlf
#
# ***************************************************************************
import sys
import traceback

import Ice
Ice.loadSlice("../services/interface/sms.ice")

import SMS


class ClientFactory(object):
    def __init__(self, host="127.0.0.1", port="10000"):
        self.ic = Ice.initialize(sys.argv)
        self.adapter = "default -h %s -p %s" % (host, port)

    def create(self, servant):
        base = self.ic.stringToProxy("%s:%s" % (servant, self.adapter))

        return SMS.SmsSendPrx.checkedCast(base)

    def destory(self):
        if self.ic:
            try:
                self.ic.destroy()
            except:
                traceback.print_exc()

    def __del__(self):
        if self.ic:
            try:
                self.ic.destroy()
            except:
                traceback.print_exc()

if __name__ == "__main__":
    client = ClientFactory()
    proxy = client.create("sms")
    phone = "18600415159" # + ",13366996127"
    tempId = "user_register"
    code = "803057"
    date = "2015-12-16 17:45:00"
    # result = proxy.sendStandard(phone, "refund_notice")
    # result = proxy.sendScheduler(phone, "warn_msg", date)
    # result = proxy.sendIdentifyingCode(phone, "ybdw_register")
    # result = proxy.checkIdentifyingCode(phone, code)
    # result = proxy.sendMessageByUser(phone, tempId)
    result = proxy.test()
    # print proxy.getSmsTemplates()
    # print result
    print result["message"]
