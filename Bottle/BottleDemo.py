import sys
from bottle import run, route

@route('/')
def hello():
    return 'hello, world'


def main():
    run(host='0.0.0.0', port=9001)

if __name__ == "__main__":
    sys.exit(main())