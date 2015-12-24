# -*- coding:utf8 -*-
# ***************************************************************************
# Create on 2015-12-24
#
# @Author:sunlf
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


class ConnectEngine(object):
    def __init__(self, **connect_args):
        connect_string = self._get_connect_string(**connect_args)
        engine = create_engine(connect_string,
                               poolclass=NullPool,
                               pool_recycle=3600)
        self.metadata = MetaData(engine)
        self.Session = sessionmaker(bind=engine, autoflush=True)

    def get_session(self):

        return self.Session()

    def get_table(self, t_name):

        return Table(t_name, self.metadata, autoload=True)

    def get_table_class(self, table_object, class_name=None):
        if class_name is None:
            class TableClass(object):
                pass

            class_name = TableClass
        mapper(class_name, table_object)

        return class_name

    def on_commit(self, session):
        try:
            session.commit()
        except Exception, e:
            session.rollback()
            print "Session commit exception, e= %s" % e
        session.close()

    def _get_connect_string(self, **connect_args):
        db_type = connect_args.get("db_type", "mysql")
        db_name = connect_args.get("db_name", "test")
        if db_type == "sqlite":
            connect_string = db_type + "//" + db_name
        else:
            db_host = connect_args.get("db_host", "localhost")
            db_user = connect_args.get("db_user", "root")
            db_pass = connect_args.get("db_pass", "123456")
            db_port = connect_args.get("db_port", "3306")
            connect_string = db_type + "://"
            connect_string += db_user + ":" + db_pass
            connect_string += "@" + db_host + ":" + db_port
            connect_string += "/" + db_name

        return connect_string


if __name__ == "__main__":
    connect_args = {"db_host": "192.168.1.249",
                    "db_user": "api",
                    "db_pass": "0IEEYdQvX7#MvF^G",
                    "db_port": "3307",
                    "db_name": "device"}

    engine = ConnectEngine(**connect_args)
    device = engine.get_table("device")
    session = engine.get_session()
    classname = engine.get_table_class(device)
    devs = session.query(classname).limit(5)
    for dev in devs:
        print dev.open_uuid
