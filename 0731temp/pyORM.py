#coding:utf-8
import random

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, LargeBinary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 手册地址：
# http://docs.sqlalchemy.org/en/rel_1_1/orm/index.html

'''
    id int primary key auto_increment,
    title varchar(200) not null,
    content varchar(2000) not null,
    tpes varchar(10) not null,
    image varchar(300) null,
    author varchar(20) null,
    view_count int default 0,
    created_at datetime null,
    is_valid smallint default 1
'''
# 创建对象的基类
Base = declarative_base()

# 初始化数据库连接，注意要接上charset=utf8否则中文无法支持
engine = create_engine("mysql+pymysql://root:123456@localhost/news?charset=utf8")
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 定义News对象
class Centroid_2_id(Base):
    __tablename__ = 'centroid_2_id_result'
    centroid_index_id = Column(String(200))
    centroid_seq_id = Column(Integer(), nullable=False)
    clustered_id = Column(Integer(),  primary_key=True)
    id_seq_id = Column(Integer(), nullable=False)
    centroid = Column(LargeBinary())
    id_osg_url = Column(String(100),)
    id_number = Column(String(18))



# 简单测试
# 如果表不存在就创建表
Base.metadata.create_all(engine)

# 创建session对象:
session = DBSession()
# 创建对象，新增一条测试数据

data = Centroid_2_id(
    centroid_index_id = "200",
    centroid_seq_id = 300,
    clustered_id = 50330+random.randint(1,199999),
    id_seq_id = 600,
    centroid = bytes('sdf',encoding='utf8'),
    id_osg_url = "200",
    id_number = "200"
)
# 添加到session:
session.add(data)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()


# orm的测试类
class OrmTest(object):
    # 初始化创建session
    def __init__(self):
        self.session = DBSession()

    # 添加数据
    def add_one(self):
        new_obj = Centroid_2_id(
            centroid_index_id = "200",
            centroid_seq_id = 300,
            clustered_id = 50220+random.randint(1,199999),
            id_seq_id = 600,
            centroid = bytes('sdf',encoding='utf8'),
            id_osg_url = "200",
            id_number = "200"
            )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    # 添加多条数据
    def add_more(self):
        add_list = []
        for i in range(10):
            new_obj = Centroid_2_id(
                centroid_index_id = "200"+str(i),
                centroid_seq_id = 300+i,
                clustered_id = 500+i,
                id_seq_id = 600+i,
                centroid = bytes('sdf')+bytes(i),
                id_osg_url = "200"+str(i),
                id_number = "200"+str(i)
            )
            self.session.add(new_obj)
            add_list.append(new_obj)
        self.session.commit()
        return add_list

    # 删除数据
    def delete_data(self):
        data = self.session.query(Centroid_2_id).get(51)
        self.session.delete(data)
        self.session.commit()

    # 修改单条数据
    def update_one(self, _id):
        obj = self.session.query(Centroid_2_id).get(_id)
        if obj:
            obj.is_valid = 0
            self.session.add(obj)
            self.session.commit()
            return True

        return False


    # 修改多条数据
    def update_data(self):

        # filter的使用方法
        data_list = self.session.query(Centroid_2_id).filter(Centroid_2_id.clustered_id > 45)
        for data in data_list:
            print(data.id_number)
            data.id_osg_url = "new string"
            self.session.add(data)
        self.session.commit()

    # 获取一条数据
    def get_one(self):
        return self.session.query(Centroid_2_id).get(1)

    # 获取多条数据
    def get_more(self):
        return self.session.query(Centroid_2_id).filter_by(id_number = 200)


def main():
    obj = OrmTest()
    rst = obj.add_one()
    print(rst)

    # 添加多条数据
    # rst = obj.add_more()
    # for _new in rst:
    #     print('id:{0},title{1},content:{2}'.format(_new.id,_new.title,_new.content))

    # 测试删除
    # obj.delete_data()

    # 修改单条数据
    # print(obj.update_one(50))

    # 修改多条数据
    obj.update_data()

    # 测试获取一条数据的函数
    # rst = obj.get_one()
    # print(rst.title)

    # 获取多条数据
    # rst = obj.get_more()
    # for _news in rst:
    #     print('news id: %s, title:%s, content:%s' % (_news.id,_news.title,_news.content))


if __name__ == "__main__":
    main()