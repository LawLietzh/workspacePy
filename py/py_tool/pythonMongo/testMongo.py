#coding:utf-8

#from pymongo import MongoClient
from pymongo import MongoClient
client = MongoClient('10.58.69.41:27017')
db = client.product_info
collection = db.simple_json

dbw = client.nerData
collectionw = dbw.nerGomeProduct
t = 0
#catid = fircat + "_" + seccat + "_" + thrcat+"_"+firid+"_"+thrCatid;
for product in collection.find():
    if "state" in  product  and "catInfo" in product and "name" in product:
        if(product["state"] == 4 and "firstCatId" in product["catInfo"] and "firstCatName" in product["catInfo"] ):
            if(product["catInfo"]["firstCatId"] == "cat31665542"):
                firstCatId = product["catInfo"]["firstCatId"]
                firstCatName = product["catInfo"]["firstCatName"]
                name = product["name"]
                data = {'firstCatId' : firstCatId, 'firstCatName':firstCatName, 'name':name}
                t = t+1
                print(data)
                collectionw.insert(data)


print(t)
# with open("first.txt", "w", "utf-8") as out_file:
#     for info in collection.find():
#         try:
#             out_file.write(info["name"] + "\n")
#         except KeyError:
#             continue























