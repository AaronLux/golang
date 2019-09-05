import pymysql.cursors

# 链接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='anderson',
                             db='matrix',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('aaronrootanderson@gmail.com', 'very-secret'))

    # 需要手动提交
    connection.commit()

    with connection.cursor() as cursor:
        # 读取单条记录
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('aaron@gmail.com',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()


