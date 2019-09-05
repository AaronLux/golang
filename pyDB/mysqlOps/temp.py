import pymysql

# 创建连接
connection = pymysql.connect(host='localhost', user='root', password='anderson', charset='utf8mb4')
# 创建游标
cursor = connection.cursor()

DBN = "testDB"
sql = "CREATE DATABASE IF NOT EXISTS " + DBN
cursor.execute(sql)

sql = "use " + DBN
cursor.execute(sql)

sql = """
CREATE TABLE IF NOT EXISTS `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) 
AUTO_INCREMENT=1 ;
"""
cursor.execute(sql)
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
