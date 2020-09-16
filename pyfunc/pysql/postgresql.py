# -*- coding: utf-8 -*-
# author: Wu Mingchun
"""postgresql.

构建本地连接类，封装具体的连接信息
"""

import psycopg2
from pyfunc.pysql import conf


class Posgre():
    """posgre."""
    def __init__(self, table: str):
        """__init__."""
        self._conn = psycopg2.connect(database=conf.DATABASE,
                                      user=conf.USER,
                                      password=conf.PWD,
                                      host=conf.HOST,
                                      port=conf.PORT)
        self._curser = self._conn.cursor()
        self._table = table

    def export(self):
        """export."""
        return (self._conn, self._curser)

    def insert(self, values: str):
        """insert."""
        self._curser.execute("insert into public.{0} values{1}".format(
            self._table, values))

    def commit(self):
        """commit."""
        self._conn.commit()

    def close(self):
        """close."""
        self._curser.close()
        self._conn.close()


if __name__ == "__main__":
    posgre = Posgre('demo')
    posgre.insert("('1',100)")
    posgre.commit()
    posgre.close()
