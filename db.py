# -*- coding: utf-8 -*-
import pymysql.cursors
import config as cf






class db(object):
    def __init__(self,conn_dict,conn=None,cursor=None):
        self._conn_dict = conn_dict
        self.conn = None
        self.cursor = None

    @property
    def get_conn(self):
        return self.conn

    @property
    def get_cursor(self):
        return self.cursor




    def set_conn(self):
        self.conn=pymysql.connect(host=self._conn_dict['host'],
                             port=self._conn_dict['port'],
                             user=self._conn_dict['user'],
                             password=self._conn_dict['password'],
                             db=self._conn_dict['db'],
                             charset=self._conn_dict['charset'],
                             cursorclass=self._conn_dict['cursorclass'])
    def set_cursor(self):
        self.cursor = self.conn.cursor()



    def conn_close(self):
        if(self.conn):
            self.conn.close()



if __name__ == "__main__":
    databse=db(cf.conn_dict)
    databse.set_conn()
    databse.set_cursor()
    conn=databse.conn
    cursor=databse.cursor

