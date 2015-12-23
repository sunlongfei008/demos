# -*- coding:utf8 -*-
# ***************************************************************************
# Create on 2015-12-10
#
# @Author:shiyun
#
# ***************************************************************************
import redis
import cPickle

from config.setting import (
    EXPIRED_TIME,
    REDIS_STORE
    )


# 验证码
class CodeRedis(object):

    def __init__(self):
        self.redis_client = redis.StrictRedis(**REDIS_STORE)

    def get_code_from_redis(self, key):
        value = self.redis_client.get(key)
        if value:
            value = cPickle.loads(value)
        return value

    def set_code_to_redis(self, key, value, time_out=EXPIRED_TIME):
        return self.redis_client.setex(key, time_out, cPickle.dumps(value))

    def del_code_from_redis(self, key):
        return self.redis_client.delete(key)
