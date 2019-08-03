#!/usr/bin/env python3
# coding=UTF-8

'''
 @Author: Aaron
 @Date:  2019/8/2  
 @Email: AaronRootAnderson@gmail.com
 @依赖： pymysql、sqlalchemy
 '''
import json

import requests

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine("mysql+pymysql://root:123456@localhost/matrix?charset=utf8")

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# centroid_2_id_result
class CentroidToIdResult(Base):
    __tablename__ = 'centroid_2_id_result'
    centroid_index_id = Column(String(255))
    centroid_seq_id = Column(Integer(), nullable=False)
    clustered_id = Column(Integer(),  primary_key=True)
    id_seq_id = Column(Integer(), nullable=False)
    centroid = Column(LargeBinary())
    id_osg_url = Column(String(100),)
    id_number = Column(String(18))

# pengzhuang_result
class PengzhuangResult(Base):
    __tablename__ = 'pengzhuang_result'
    id = Column(Integer(),  primary_key=True)
    # 下面两个字段一样
    centroid_index_id = Column(String(255))
    id_index_id = Column(String(255))

    centroid_seq_id = Column(Integer(), nullable=False)
    id_seq_id = Column(Integer())

# shenting_feature_osg
class ShentingFeatureOSG(Base):
    __tablename__ = 'shenting_feature_osg'
    id = Column(Integer(),  primary_key=True)
    index_id = Column(Integer(), nullable=False)
    seq_id = Column(Integer())
    id_osg_url = Column(String(255))

# centroid_feature
class CentroidFeature(Base):
    __tablename__ = 'centroid_feature'
    id = Column(Integer(),  primary_key=True)
    clustered_id = Column(Integer(), nullable=False)
    seq_id = Column(Integer())
    index_id = Column(String(255))

Base.metadata.create_all(engine)


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
    
    pengzhuang_obj = PengzhuangResult(
        centroid_index_id = "anderson",
        centroid_seq_id = 100,
        id_index_id = "anderson",
        id_seq_id = 200
    )
    session.add(pengzhuang_obj)
    session.commit()
    """

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
        parameter_id_index_id = ""
        parameter_id_seq_id = result.id_seq_id

        session.query(CentroidFeature).filter()

        # db_id
        uri = "/engine/static-feature/v1/databases/" + parameter_id_index_id + "/batch_get"
        # TODO 待确认字段
        req_json = {
            # 这里传不传其实是一样的。。。。
            "col_id": "",
            "ids": [parameter_centroid_index_id]
        }
        url = viperAddr + uri

        response = requests.post(url,json=req_json)
        if response.status_code == 200:
            response_dict = requests.post(url,json=req_json).json()

            feature_items = response_dict.json()["items"]
            for feature_item in feature_items:
                extra_info = feature_item["extra_info"]
                parameter_centroid = feature_item["feature"]["blob"]
                parameter_id_osg_url = feature_item["image_id"]

                # 第三方接口调用
                url = "http://localhost:9999/json"
                req_json_for_js = {
                    "id" : extra_info,
                    "addImg" : False
                }
                resp_dict = requests.post(url,json = req_json_for_js)
                info = resp_dict.json()["info"]
                # TODO 询天要加的字段，待确定是否要保存
                # name = info["name"]
                parameter_id_number = info["idCard"]

                #写入数据库
                obj = CentroidToIdResult(
                    centroid_index_id = parameter_centroid_index_id,
                    centroid_seq_id = result.centroid_seq_id,
                    clustered_id = result.centroid_seq_id,
                    id_seq_id = parameter_id_index_id,
                    centroid = parameter_centroid,
                    id_osg_url = parameter_id_osg_url,

                    id_number = parameter_id_number
                )
                session.add(obj)
                session.commit()
                # TODO 待控制请求次数

