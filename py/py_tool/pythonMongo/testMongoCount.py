#conding:utf-8
from pymongo import MongoClient
#建立客户端
client = MongoClient('10.58.69.41:27017')
#连接数据库
db = client.nerData
#删除集合 db.collection.drop()


#连接表名  如果不存在，会自动创建
collection = db.NerTestData

collection.insert({
    "title": 'MongoDB 教程',
    "description": 'MongoDB 是一个 Nosql 数据库',
    "by": '菜鸟教程',
    "url": 'http://www.runoob.com',
    "tags": ['mongodb'],
    "term": {"A":"aaaaa","A":"bbbb"}
})

collection.insert({
    "title": 'MongoDB 教程',
    "description": 'MongoDB 是一个 Nosql 数据库',
    "by": '菜鸟教程',
    "url": 'http://www.runoob.com',
    "tags": ['mongodb'],
    "likes": 100
})
count = collection.count()
print(count)

