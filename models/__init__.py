# coding: utf-8

"""数据库操作
"""
from pymongo import MongoClient

__author__ = 'zdt'

client = MongoClient('localhost', 27017)
db = client.Material