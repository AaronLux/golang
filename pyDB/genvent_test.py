#!/usr/bin/env python3
# coding=UTF-8

'''
 @Author: Aaron
 @Date:  2019/8/2  
 @Email: AaronRootAnderson@gmail.com  
 '''

from gevent import monkey;monkey.patch_all()
import gevent
import requests
import time
import pymysql


def data_handler(anum,num):
    conn = pymysql.connect(host='localhost',user='root',password='123456',database='matrix',charset='utf8')
    cursor = conn.cursor()
    for i in range(anum,num):
        sql = 'insert into users(email,password) values(%s,%s);'
        res = cursor.execute(sql,["root"+str(i),i])
        conn.commit()
    cursor.close()
    conn.close()

start_time=time.time()

gevent.joinall([
    gevent.spawn(data_handler,1,2001),
    gevent.spawn(data_handler,2001,5001),
    gevent.spawn(data_handler,5001,8001),
    gevent.spawn(data_handler,8001,10001),
])


stop_time=time.time()
print('run time is %s' %(stop_time-start_time))
