import os
import sys

import paste
from bottle import run, route, request
# 静态服务器的搭建
from bottle import static_file


@route('/')
def hello():
    return 'hello, this bottle server.'


@route('/sayHi')
def func():
    return 'hi, anderson'


# 对动态路由的支持
@route('/path/<sub_path>')
def do_path(sub_path):
    return 'You are visiting /path/%s' % sub_path


# 静态服务器
@route('/static/<filename>')
def do_download(filename):
    return static_file(filename, root="/tmp")


# upload file use default name
@route('/upload/<save_name>', method='POST')
def do_upload(save_name):
    upload = request.files.get('filename')
    # 这里的目录权限的问题要注意，
    # save_path = os.path.join('/aaron_data', save_name)
    # upload.save(save_path)
    upload.save(save_name + ".pdf")
    print(upload)
    return 'OK'


# json的支持
@route('/json', method='POST')
def do_json():
    data = request.json
    message = data.get('message')
    resp = {}
    resp['rtn'] = 0
    resp['msg'] = 'Your message is %s.' % message
    resp['info'] = {
        "idCard": "322535199502035652",
        "name": " aaron"
    }
    return resp


@route('/unstableSever', method='POST')
def handle_unstable_sever():
    import time, random
    data = request.json
    message = data.get('message')
    resp = {}
    resp['rtn'] = 0
    resp['msg'] = 'Your message is %s.' % message
    resp['info'] = {
        "idCard": "322535199502035652",
        "name": " aaron"
    }
    time.sleep(random.randint(0, 5))
    return resp


def main():
    # 阻塞的服务器，使用其他方式来实现非阻塞服务器
    # run(host='0.0.0.0', port=9001)

    # 通过paste 实现非阻塞的服务器   cmd:easy_install paste
    run(server='paste', host='0.0.0.0', port=8080)


if __name__ == "__main__":
    sys.exit(main())
