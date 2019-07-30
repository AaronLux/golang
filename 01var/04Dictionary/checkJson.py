#!/usr/bin/env python3
# coding=UTF-8

'''
 @Author: Aaron
 @Date:  2019/7/29  
 @Email: AaronRootAnderson@gmail.com  
 '''

import json

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

data = {
    'name' : '',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
not_json_str = 'name'

print(is_json(json_str))
print(is_json(not_json_str))

