#!/usr/bin/env python3
# coding=UTF-8

'''
 @Author: Aaron
 @Date:  2019/8/12  
 @Email: AaronRootAnderson@gmail.com  
 '''
import  cProfile
import  time
import pysnooper

def fun():
    for i in range(10000):
        for j in range(10000):
            a = i * i + j * j
@pysnooper.snoop()
def func():
    time.sleep(3)
    print("222")

cProfile.run('fun()')
cProfile.run('func()')