#!/usr/bin/env python3
# coding=UTF-8

'''
 @Author: Aaron
 @Date:  2019/8/2  
 @Email: AaronRootAnderson@gmail.com  
 '''
import  pymysql


class MysqlConnection(object):

    # 初始化
    def __init__(self, host = '127.0.0.1', port = 3306, user = 'root', password = '123456', db = 'matrix',charset='utf8'):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._db = db
        self._charset = charset
        self._conn = None
        self._cursor = None
        self.get_conn()

    # 关闭数据库连接
    def close(self):
        if self._cursor:
            self._cursor.close()
            self._cursor = None

        if self._conn:
            self._conn.close()
            self._conn = None

    def commit(self):
        self._conn.commit()

    # 获取数据库连接
    def get_conn(self):
        try:
            self._conn = pymysql.connect(
                host = self._host,
                user = self._user,
                password = self._password,
                db = self._db,
                port = self._port,
                charset = self._charset
            )

            self._cursor = self._conn.cursor()
        except pymysql.Error as e:
            print('mysql error:%s' % e)

    def add_one(self):
        sql = 'insert into users(email,password) values(%s, %s)'
        self._cursor.execute(sql, ('aaron@gmail.com','v1pass'))
        self.commit()
        self.close()



def main():
    obj = MysqlConnection()
    # rst = obj.get_more()
    # rst = obj.get_one()
    # print(rst)
    # obj.add_one()
    obj.run()
if __name__ == '__main__':
    main()