# -*- coding:utf8 -*-
# ***************************************************************************
# Create on 2015-12-10
#
# @Author:shiyun
#
# ***************************************************************************

from sqlalchemy import (
    create_engine,
    MetaData,
    Table)
from sqlalchemy.orm import (
    sessionmaker,
    mapper)
from sqlalchemy.pool import NullPool


class MysqlConnectEngine(object):

    def __init__(self, hostname, username, password, port, db):
        engine_url = "mysql://%s:%s@%s:%s/%s?charset=utf8" % (username,
                                                              password,
                                                              hostname,
                                                              port,
                                                              db)
        engine = create_engine(engine_url,
                               poolclass=NullPool,
                               pool_recycle=3600)
        self.metadata = MetaData(engine)
        self.Session = sessionmaker(bind=engine, autoflush=True)

    def get_session(self):

        return self.Session()

    def get_table(self, t_name):

        return Table(t_name, self.metadata, autoload=True)

    def map_table(self, t_obj):

        class ClassObj(object):
            pass

        mapper(ClassObj, t_obj)

        return ClassObj

    def on_commit(self, session):
        try:
            session.commit()
        except:
            session.rollback()

        session.close()


if __name__ == "__main__":
    mysqlserver = {"hostname": "192.168.1.249",
                   "username": "api",
                   "password": "0IEEYdQvX7#MvF^G",
                   "port": "3307",
                   "db": "device"}
    engine = MysqlConnectEngine(**mysqlserver)
    device = engine.get_table("device")
    class_obj = engine.map_table(device)
    session = engine.get_session()
    objs = session.query(class_obj).limit(5)
    for obj in objs:
        print obj.devicetoken
