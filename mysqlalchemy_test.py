#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

engine = create_engine("mysql+pymysql://root:jinxin@127.0.0.1/python",encoding='utf-8',echo=True)
#echo=True，就是把整个过程打印出来

Base=declarative_base() #生成ORM基类

class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer,primary_key=True) #字段，整形，主键 column是导入的
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine) #创建表结构


'''
创建数据，有个游标的东西叫做sessionmaker需要单独导入
'''
from sqlalchemy.orm import sessionmaker
#实例与socket绑定,创建与数据库的绘画session class，注意，这里返回
#给session的是一个class，不是实例
Session_class = sessionmaker(bind=engine)
#生成session实例，cursor
Session = Session_class()

#生产你要创建的数据对象
xiedi_obj = User(name="alex",password="123")
xiedi_obj2 = User(name="jack",password="123")
#目前还没有创建对象，可以打印看看，上面只是申明
print(xiedi_obj.name,xiedi_obj.id)

#把要创建的数据对象添加到这个session里，一会同一创建
Session.add(xiedi_obj)
Session.add(xiedi_obj2)
#这里依旧没有创建
print(xiedi_obj.name,xiedi_obj.id)

#现在才同一提交，创建数据
Session.commit()




