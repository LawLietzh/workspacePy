#conding:utf-8
from pymongo import MongoClient
#建立客户端
client = MongoClient('10.58.69.41:27017')
#连接数据库
db = client.nerData
#删除集合 db.collection.drop()


#连接表名  如果不存在，会自动创建
collection = db.Test
#catid = fircat + "_" + seccat + "_" + thrcat+"_"+firid+"_"+thrCatid;
#展示所有数据库
print(db.dbs)

#插入
#collection.insert({"name":"菜鸟"})
#删除 数据库
#db.dropDatabase()
#遍历所有条数
#for product in collection.find():
#更新  update()

collection.update({'name':'菜鸟'},{'name':'MongoDB'})


#删除文档
collection.insert({"title": 'MongoDB 教程',
               "description": 'MongoDB 是一个 Nosql 数据库',
               "by": '菜鸟教程',
               "url": 'http://www.runoob.com',
               "tags": ['mongodb', 'database', 'NoSQL'],
               "likes": 100
               })

collection.remove({'title':'MongoDB 教程'})

#查询文档
'''
MongoDB 查询文档使用find() 方法 以非结构的方法来显示所有文档
db.collection.find(query,projection)
query 可选，使用查询操作符指定查询条件 
projection 可选
如果你需要以易读的方式来读取数据，可以使用pretty()方法

db.col.find().pretty()


'''
print(dir(collection))
print(collection.find_one())


'''
MongoDB 中的条件 查询
等于 {<key>:<value>}
小于	{<key>:{$lt:<value>}}	       db.col.find({"likes":{$lt:50}}).pretty()	
小于或等于	{<key>:{$lte:<value>}}	   db.col.find({"likes":{$lte:50}}).pretty()	
大于	{<key>:{$gt:<value>}}	       db.col.find({"likes":{$gt:50}}).pretty()	
大于或等于	{<key>:{$gte:<value>}}	   db.col.find({"likes":{$gte:50}}).pretty()	
不等于	{<key>:{$ne:<value>}}	       db.col.find({"likes":{$ne:50}}).pretty()
'''
#不加 list 返回的是 游标，而不是 具体的数据
print(list(collection.find({"firstCatId" : "cat31665542"})))


# MongoDB 条件操作符
'''
大于 $gt $lt  $ gte  $lte 
为了使用方便，我们可以先使用一下命令清空集合
'''
collection.remove({})
#插入一下数据
collection.insert({
    "title": 'PHP 教程',
    "description": 'PHP 是一种创建动态交互性站点的强有力的服务器端脚本语言。',
    "by": '菜鸟教程',
    "url": 'http://www.runoob.com',
    "tags": ['php'],
    "likes": 200
})

collection.insert({
               "title": 'Java 教程',
               "description": 'Java 是由Sun Microsystems公司于1995年5月推出的高级程序设计语言。',
               "by": '菜鸟教程',
               "url": 'http://www.runoob.com',
               "tags": ['java'],
               "likes": 150
               })

collection.insert({
               "title": 'MongoDB 教程',
               "description": 'MongoDB 是一个 Nosql 数据库',
               "by": '菜鸟教程',
               "url": 'http://www.runoob.com',
               "tags": ['mongodb'],
               "likes": 100
               })

print( list(collection.find(  {"likes":{"$gt" : 100}}  )) )
#联合查询
print( list(collection.find(  {"likes":{"$gt" : 100,"$lt" : 200}}  )) )

#MongoDB $type 操作符

#如果想获取 "col" 集合中 title 为 String 的数据，你可以使用以下命令：
collection.find({"title" : {"$type" : 2}})

#MongoDB 中读取指定数量的数据记录，可以使用MongoDB 的 limit方法，
print("limit ",list(collection.find().limit(1)))

#MongoDB sort() 方法  sort() 方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式
#其中1  为升序，-1 位降序

print("sort:",list(collection.find().sort('likes',-1)))


###MongoDB 索引   索引通常能够极大的提高查询的效率，如果没有索引，MongoDB在读取数据时必须扫描集中中每个文件并选取那些
#符合查询条件的记录是非常耗时的
#索引是特殊的数据结构，索引存储在一个易于遍历读取的数据集合中，索引是对数据库表中一列或多列的值 进行排序的一种结构

#  create_index（） 方法来创建索引  1为指定按升序创建索引，如果你想按降序来创建索引指定为-1即可。
#之前的老方法 ensureindex() 已经不用了
collection.create_index([("likes",1)])

#mongoDB 聚合 （aggregate）







