#!/usr/bin/env python3
# coding=UTF-8

'''
92 100行打开
 @Author: Aaron
 @Date:  2019/8/2  
 @Email: AaronRootAnderson@gmail.com
 @依赖： pymysql、sqlalchemy
 '''
import json
import time

import requests

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

viperAddr = ""
DB_ID = ""

# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
engine = create_engine("mysql+pymysql://root:123456@localhost/matrix?charset=utf8")

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# centroid_2_id_result
class CentroidToIdResult(Base):
    __tablename__ = 'centroid_2_id_result'
    centroid_index_id = Column(String(255))
    # 下面两个字段一样
    centroid_seq_id = Column(Integer(), nullable=False)
    clustered_id = Column(Integer(),  primary_key=True)

    id_index_id = Column(String(255))
    id_seq_id = Column(Integer(), nullable=False)

    centroid = Column(LargeBinary())
    id_osg_url = Column(String(255),)
    id_name = Column(String(255))
    id_number = Column(String(255))

# pengzhuang_result
class PengzhuangResult(Base):
    __tablename__ = 'pengzhuang_result'
    id = Column(Integer(),  primary_key=True)

    centroid_seq_id = Column(Integer(), nullable=False)

    centroid_index_id = Column(String(255))

    id_index_id = Column(String(255))
    id_seq_id = Column(Integer())


Base.metadata.create_all(engine)

# 初始化创建session
session = DBSession()

# 撞库后的总数量
tally = session.query(PengzhuangResult).count()

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
for i in range(1,tally):
    result = session.query(PengzhuangResult).get(i)
    parameter_centroid_index_id = result.centroid_index_id
    # centroid_seq_id = cluster_id
    parameter_centroid_seq_id = result.centroid_seq_id
    parameter_cluster_id = result.centroid_seq_id
    # 身份证大库的ID
    parameter_id_index_id = result.id_index_id
    parameter_id_seq_id = result.id_seq_id

    # db_id
    # uri = "/engine/static-feature/v1/databases/" + DB_ID + "/batch_get"

    # TODO 待确认字段
    req_json = {
        # 这里传不传其实是一样的。。。。
        "col_id": "",
        "ids": [parameter_centroid_index_id]
    }
    # url = viperAddr + uri
    url = "http://localhost:9091/test"
    response = requests.post(url,json=req_json)
    if response.status_code == 200:
        response_dict = requests.post(url,json=req_json)

        feature_items = response_dict.json()["items"]
        for feature_item in feature_items:
            extra_info = feature_item["extra_info"]
            parameter_centroid = feature_item["feature"]["blob"]
            parameter_id_osg_url = feature_item["image_id"]

            # 第三方接口调用
            url = "http://localhost:9091/json"
            # url = "http://hysr.gat.js/rest/webface/queryInfoById"
            req_json_for_js = {
                "id" : extra_info,
                "addImg" : False
            }
            resp_dict = requests.post(url,json = req_json_for_js)
            info = resp_dict.json()["info"]

            parameter_name = info["name"]
            parameter_id_number = info["idCard"]

            #写入数据库
            obj = CentroidToIdResult(
                centroid_index_id = parameter_centroid_index_id,
                centroid_seq_id = parameter_centroid_seq_id,
                clustered_id = parameter_centroid_seq_id,
                id_index_id = parameter_id_index_id,
                id_seq_id = parameter_id_seq_id,
                centroid = bytes(parameter_centroid,encoding="utf-8"),
                id_osg_url = parameter_id_osg_url,
                id_name = parameter_name,
                id_number = parameter_id_number
            )
            session.add(obj)
            session.commit()
            time.sleep(0.1)

if __name__ == "__main__":
    pass

