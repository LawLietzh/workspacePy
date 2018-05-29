#coding:utf-8
import  numpy as np
cate_list = ["a","b","c"]
cate_dict = dict()
cate_set = set(cate_list)
i = 0
for label in cate_set:
    print(label)
    print(i)
    cate_dict[label] = i
    i += 1
print("_______________________________________________")

# one-hot encoing
labels = np.array([cate_dict[tmp] for tmp in cate_set])
print(labels)
print(len(labels))
label_reform = (  np.arange(len(cate_dict)) == labels[:,None]).astype(np.float32)
print(label_reform)

