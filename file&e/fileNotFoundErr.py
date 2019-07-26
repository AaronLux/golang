file_name = 'alice.txt'

# 当我们open时候不需要手动close，解释器会在合适的时候关闭文件资源

# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
try:
    with open(file_name) as f:
        f.read()
except FileNotFoundError:
    message = "sorry, the file " + file_name + " does not exit."
    print(message)
