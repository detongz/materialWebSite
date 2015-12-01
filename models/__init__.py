# coding: utf-8

"""数据库操作
"""
__author__ = 'zdt'


from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.Material