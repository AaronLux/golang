#!/usr/bin/env python3
# coding=UTF-8

'''
 @Author: Aaron
 @Date:  2019/8/3
 @Email: AaronRootAnderson@gmail.com
 '''

import requests

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, LargeBinary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# 对象基类
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


if __name__ == '__main__':


    # 初始化创建session
    session = DBSession()



    url = "http://localhost:9999/json"
    req_json_for_js = {
        "id" : "test",
        "addImg" : False
    }
    resp_dict = requests.post(url,json = req_json_for_js)
    infos = resp_dict.json()["info"]

    parameter_id_number = infos['idCard']
    print("parameter_id_number",parameter_id_number)

    #写入数据库
    obj = Centroid_2_id_result(
        centroid_index_id = "test",
        centroid_seq_id = 1213,
        clustered_id = 1223,
        id_seq_id = 1232,
        centroid = bytes("anderson",encoding="utf-8"),
        id_osg_url = "www.aaron.com/1.jpeg",
        id_number = "32222220"
    )
    session.add(obj)
    session.commit()

