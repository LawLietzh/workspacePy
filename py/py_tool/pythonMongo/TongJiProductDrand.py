#conding:utf-8
from pymongo import MongoClient
#建立客户端
client = MongoClient('10.115.3.97:27017')
#连接数据库
db = client.nerData
#删除集合 db.collection.drop()


#连接表名  如果不存在，会自动创建
#训练库
#collection = db.NerLabelData
#训练库
collection = db.NerLabelDataTrain
count = collection.count()
print(count)
p = 0
b = 0
for product in collection.find():
    if "tags" in product:
        for tag in product["tags"]:
            if "product" in tag:
                p = p +1
            if "brand" in tag:
                b = b + 1
print("改动的物品词",p)
print("改动的品牌词",b)
print("产品词正确率",(count - p)/count)
print("品牌词正确率",(count - b)/count)