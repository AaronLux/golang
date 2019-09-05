#!/usr/bin/env python3
# coding=UTF-8

'''
 @Author: Aaron
 @Date:  2019/8/12  
 @Email: AaronRootAnderson@gmail.com  
 '''
import requests
from gevent import monkey;
import gevent


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    print(resp.status_code)
    data = resp.content
    print('%d bytes received from %s.' % (len(data), url))


for i in range(0, 10):
    gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://github.com/'),
    ])
