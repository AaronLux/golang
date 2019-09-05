import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', user='root', password='anderson', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

DBN = "testDB"
sql = "CREATE DATABASE IF NOT EXISTS " + DBN
cursor.execute(sql)