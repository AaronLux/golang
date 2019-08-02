#
# '''1.设计mysql的数据库和表
#
# id:新闻的唯一标示
# title:新闻的标题
# content:新闻的内容
# created_at:新闻添加的时间
# types:新闻的类型
# image:新的缩略图
# author:作者
# view_count:浏览量
# is_valid:删除标记
#
# # 创建新闻数据库
# create database news charset=utf8;
#
# # 创建新闻表
# create table news(
#     id int primary key auto_increment,
#     title varchar(200) not null,
#     content varchar(2000) not null,
#     types varchar(10) not null,
#     image varchar(300) null,
#     author varchar(20) null,
#     view_count int default 0,
#     created_at datetime null,
#     is_valid smallint default 1
# ) default charset="utf8";
# '''
#
# '''
#
# 插入数据
# INSERT INTO `news` VALUES ('1', '朝鲜特种部队视频公布 展示士兵身体素质与意志', '新闻内容', '推荐', '/static/img/news/01.png', null, '0', null, '1');
# INSERT INTO `news` VALUES ('2', '男子长得像\"祁同伟\"挨打 打人者:为何加害检察官', '新闻内容', '百家', '/static/img/news/02.png', null, '0', null, '1');
# INSERT INTO `news` VALUES ('3', '导弹来袭怎么办？日本政府呼吁国民堕入地下通道', '新闻内容', '本地', '/static/img/news/03.png', null, '0', null, '1');
# INSERT INTO `news` VALUES ('4', '美监:朝在建能发射3发以上导弹的3000吨级新潜艇', '新闻内容', '推荐', '/static/img/news/04.png', null, '0', null, '1');
# INSERT INTO `news` VALUES ('5', '证监会：前发审委员冯小树违法买卖股票被罚4.99亿', '新闻内容', '百家', '/static/img/news/08.png', null, '0', null, '1');
# INSERT INTO `news` VALUES ('6', '外交部回应安倍参拜靖国神社:同军国主义划清界限', '新闻内容', '推荐', '/static/img/news/new1.jpg', null, '0', null, '1');
# INSERT INTO `news` VALUES ('7', '\"萨德\"供地违法？韩民众联名起诉要求撤回供地', '新闻内容', '百家', '/static/img/news/new2.jpg', null, '0', null, '1');
# INSERT INTO `news` VALUES ('10', '标题1', '新闻内容1', '推荐', '/static/img/news/01.png', null, '0', null, '1');
#
#
# 2.python简单操作mysql之数据库的连接和简单获取数据
# #encoding:utf-8
# '''
#
# import MySQLdb
#
# '''
# # 简单的连接
# # 获取连接
# conn = MySQLdb.connect(
#     host = '127.0.0.1',
#     user = 'root',
#     password = '',
#     db = 'news',
#     port = 3306,
#     charset = 'utf8'
# )
#
# # 获取数据
# cursor = conn.cursor()
# cursor.execute('select * from news order by created_at desc')
# rest = cursor.fetchone()
# print(rest)
#
# # 关闭连接
# conn.close()
#
# 3.python简单操作mysql之数据库的连接和简单获取数据改进之捕获异常
#
# # 捕获异常
# # 获取连接
# try:
#     conn = MySQLdb.connect(
#         host = '127.0.0.1x',
#         user = 'root',
#         password = '',
#         db = 'news',
#         port = 3306,
#         charset = 'utf8'
#     )
#
#     # 获取数据
#     cursor = conn.cursor()
#     cursor.execute('select * from news order by created_at desc')
#     rest = cursor.fetchone()
#     print(rest)
#
#     # 关闭连接
#     conn.close()
# except MySQLdb.Error as e:
#     print('mysql error:%s' % e)
#
#
# 4.python简单操作mysql之数据库的连接和单获取所有数据
# # 获取连接
# try:
#     conn = MySQLdb.connect(
#         host = '127.0.0.1',
#         user = 'root',
#         password = '',
#         db = 'news',
#         port = 3306,
#         charset = 'utf8'
#     )
#
#     # 获取数据
#     cursor = conn.cursor()
#     cursor.execute('select * from news')
#     rows = cursor.fetchall()
#     print(cursor.description)
#
#     for row in rows:
#         print(row)
#
#     # 关闭连接
#     conn.close()
# except MySQLdb.Error as e:
#     print('mysql error:%s' % e)
#
#
# 5.python简单操作mysql之数据库的操作类
#
# class MysqlConnection(object):
#
#     # 初始化
#     def __init__(self, host = '127.0.0.1', port = 3306, user = 'root', password = '', db = 'news',charset='utf8'):
#         self._host = host
#         self._port = port
#         self._user = user
#         self._password = password
#         self._db = db
#         self._charset = charset
#         self._conn = None
#         self._cursor = None
#         self.get_conn()
#
#     # 关闭数据库连接
#     def close(self):
#         if self._cursor:
#             self._cursor.close()
#             self._cursor = None
#
#         if self._conn:
#             self._conn.close()
#             self._conn = None
#
#     def commit(self):
#         self._conn.commit()
#
#     # 获取数据库连接
#     def get_conn(self):
#         try:
#             self._conn = MySQLdb.connect(
#                 host = self._host,
#                 user = self._user,
#                 password = self._password,
#                 db = self._db,
#                 port = self._port,
#                 charset = self._charset
#             )
#
#             self._cursor = self._conn.cursor()
#         except MySQLdb.Error as e:
#             print('mysql error:%s' % e)
#
#
#     # 获取单条新闻
#     def get_one(self):
#
#         sql = 'select * from news where types = %s order by created_at desc'
#         # 获取数据
#         self._cursor.execute(sql,('百家',))
#         rest = dict(zip([k[0] for k in self._cursor.description], self._cursor.fetchone()))
#
#         # 关闭连接
#         self.close()
#         return rest
#
#     # 获取多条新闻
#     def get_more(self):
#
#         sql = 'select * from news where types = %s order by created_at desc'
#         # 获取数据
#         self._cursor.execute(sql,('百家',))
#         rest = [dict(zip([k[0] for k in self._cursor.description], row))
#         for row in self._cursor.fetchall()]
#
#         # 关闭连接
#         self.close()
#         return rest
#
#     def add_one(self):
#         sql = 'insert into news(title,image,content,types,is_valid) values(%s, %s, %s, %s, %s)'
#         self._cursor.execute(sql, ('标题1','/static/img/news/01.png', '新闻内容1','推荐',1))
#         self.commit()
#         self.close()
#
# def main():
#     obj = MysqlConnection()
#     # rst = obj.get_more()
#     # rst = obj.get_one()
#     # print(rst)
#     obj.add_one()
#
# if __name__ == "__main__":
#     main() """