#!/usr/bin/env python3
# coding=UTF-8

'''
 @Author: Aaron
 @Date:  2019/8/2  
 @Email: AaronRootAnderson@gmail.com  
 '''
import random
import time

import requests
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, LargeBinary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



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

engine = create_engine("mysql+pymysql://root:123456@localhost/matrix?charset=utf8")
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# centroid_2_id_result
class Centroid_2_id_result(Base):
    __tablename__ = 'centroid_2_id_result'
    centroid_index_id = Column(String(255))
    centroid_seq_id = Column(Integer(), nullable=False)
    clustered_id = Column(Integer(),  primary_key=True)
    id_seq_id = Column(Integer(), nullable=False)
    centroid = Column(LargeBinary())
    id_osg_url = Column(String(100),)
    id_number = Column(String(18))

# pengzhuang_result
class Pengzhuang_result(Base):
    __tablename__ = 'pengzhuang_result'
    id = Column(Integer(),  primary_key=True)
    centroid_index_id = Column(String(255))
    centroid_seq_id = Column(Integer(), nullable=False)
    id_index_id = Column(String(255))
    id_seq_id = Column(Integer())

# shenting_feature_osg
class Shenting_feature_osg(Base):
    __tablename__ = 'shenting_feature_osg'
    id = Column(Integer(),  primary_key=True)
    index_id = Column(Integer(), nullable=False)
    seq_id = Column(Integer())
    id_osg_url = Column(String(255))

# centroid_feature
class Centroid_feature(Base):
    __tablename__ = 'centroid_feature'
    id = Column(Integer(),  primary_key=True)
    clustered_id = Column(Integer(), nullable=False)
    seq_id = Column(Integer())
    index_id = Column(String(255))


# 如果表不存在就创建表
Base.metadata.create_all(engine)


# orm的测试类
class OrmTest(object):
    # 初始化创建session
    def __init__(self):
        self.session = DBSession()

    # 添加数据
    def add_one(self):
        new_obj = Centroid_2_id_result(
            centroid_index_id = "200",
            centroid_seq_id = 300,
            clustered_id = 5220,
            id_seq_id = 600,
            centroid = bytes('sdf',encoding='utf8'),
            id_osg_url = "200",
            id_number = "200"
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

if __name__ == '__main__':

    viperAddr = "http://10.111.32.112:30080"
    # 初始化创建session
    session = DBSession()

    """
    test_obj = Centroid_2_id_result(
        centroid_index_id = "200",
        centroid_seq_id = 300,
        clustered_id = random.randint(1,10000),
        id_seq_id = 600,
        centroid = bytes('sdf',encoding='utf8'),
        id_osg_url = "200",
        id_number = "200"
    )

    session.add(new_obj)
    session.commit()
    """

    # 撞库后的总数量
    tally = session.query(Pengzhuang_result).count()
    """
    TODO 批量逻辑
    nodes = list(range(0,tally,15))

    for i in nodes:
        result_list = session.query(Pengzhuang_result).limit(16).offset(i).all()
        for result in result_list:
            url_centroid_index_id = result.centroid_index_id
            url_id_index_id = result.id_index_id
            req_json = {
                
            }
    """

    for i in range(0,tally):
        result = session.query(Pengzhuang_result).get(i)
        url_centroid_index_id = result.centroid_index_id
        url_id_index_id = result.id_index_id
        # TODO 待确认字段
        req_json = {
            "col_id": url_centroid_index_id,
            "ids": url_id_index_id
        }
        uri = "/engine/static-feature/v1/databases/" + col_id + "/batch_get"

        url = viperAddr + uri
        r = requests.post(url,json=req_json)

        items = r.json()["items"]
        for item in items:
            extra_info = item["extra_info"]
            blob = item["feature"]["blob"]
            image_id = item["image_id"]
            # 第三方接口调用
            url = ""
            req_json_for_js = {
                "id" : extra_info,
                "addImg" : False
            }
            resp = requests.post(url,json = req_json_for_js)
            infos = resp.json()["info"]
            for info in infos:
                name = info["name"]
                idCard = info["idCard"]

                #写入数据库
                obj = Centroid_2_id_result(
                    centroid_index_id = url_centroid_index_id
                    centroid_seq_id = result.centroid_seq_id,
                    clustered_id = result.centroid_seq_id,
                    id_seq_id = url_id_index_id,
                    centroid = blob
                    id_osg_url = image_id,
                    id_number = idCard
                )
                session.add(new_obj)
                session.commit()
                # TODO 待控制
                # time.sleep(1000)