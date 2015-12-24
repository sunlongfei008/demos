# -*- coding:utf8 -*-
# ***************************************************************************
# Create on 2015-12-24
#
# @Author:sunlf
#
# ***************************************************************************

import redis
import cPickle


class RedisHandler(object):

    def __init__(self, connect_args):
        pool = redis.ConnectionPool(**connect_args)
        self.redis_client = redis.StrictRedis(connection_pool=pool)

    def get_value(self, key):
        value = self.redis_client.get(key)
        if value:
            value = cPickle.loads(value)
        return value

    def set_value(self, key, value):

        return self.redis_client.set(key, cPickle.dumps(value))

    def set_expire_value(self, key, value, expire):

        return self.redis_client.setex(key, expire, value)

    def del_key(self, key):

        return self.redis_client.delete(key)


if __name__ == "__main__":
    connect_args = {"host": "127.0.0.1", "port": 6379, "db": 0}
    handler = RedisHandler(connect_args)
    handler.set_value("a", "b")
    handler.set_expire_value("c", "afaf", 100)
