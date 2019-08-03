#!/usr/bin/env python3
# coding=UTF-8
import sys

import paste
from bottle import run, route, request

@route('/json', method='POST')
def do_json():
    data = request.json
    message = data.get('message')
    resp = {}
    resp['rtn'] = 0
    resp['msg'] = 'Your message is %s.' % message
    resp['info'] = {
        "idCard":"322535199502035652",
        "name" : "aaron"
    }
    return  resp

def main():
    # 阻塞的服务器，使用其他方式来实现非阻塞服务器
    # run(host='0.0.0.0', port=9001)

    # 通过paste 实现非阻塞的服务器  easy_install paste
    run(server='paste', host='0.0.0.0', port=9999)
if __name__ == "__main__":
    sys.exit(main())

