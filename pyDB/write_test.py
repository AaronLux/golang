#!/usr/bin/env python3
# coding=UTF-8

'''
 @Author: Aaron
 @Date:  2019/8/2  
 @Email: AaronRootAnderson@gmail.com  
 '''


"""
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;

"""

"""
CREATE TABLE IF NOT EXISTS `pengzhuang_result` (
      `id` int NOT NULL AUTO_INCREMENT,
      `centroid_index_id` varchar(255),
      `centroid_seq_id` bigint,
      `id_index_id` varchar(255),
      `id_seq_id` bigint,
      PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;

"""

import pymysql
import time
from concurrent.futures import ProcessPoolExecutor


def data_handler(urls):
    conn = pymysql.connect(host='localhost',user='root',password='123456',database='matrix',charset='utf8')
    cursor = conn.cursor()
    for i in range(urls[0],urls[1]):
        sql = 'insert into users(email,password) values(%s,%s);'
        res = cursor.execute(sql,["root"+str(i),i])
        conn.commit()
    cursor.close()
    conn.close()


def run():
    # 21.079573154449463
    urls = [(1,2001),(2001,5001),(5001,8001),(8001,10001)]
    with ProcessPoolExecutor() as executor:
        executor.map(data_handler,urls)  ##ProcessPoolExecutor 提供的map函数，可以直接接受可迭代的参数，并且结果可以直接for循环取出


if __name__ == '__main__':
    start_time = time.time()
    run()
    stop_time = time.time()
    print('run time is %s' % (stop_time - start_time))
