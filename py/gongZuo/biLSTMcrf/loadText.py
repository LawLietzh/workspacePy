#coding:utf-8
import numpy as np
path = "./sample_train.txt"
file_r = open(path, 'r', encoding='utf-8')
sentences = file_r.read().strip().split("\n\n")
print(sentences)
sentence_count = 4
max_len = 5
arr = np.zeros((sentence_count, max_len), dtype='int32')
print(arr)

#练习 enumerate
one_instance_items = []
for index ,sentences in enumerate(sentences):
    items = sentences.split('\n')

    print([one_instance_items.append([]) for _ in range(3)])
    #print(index,sentences)
    for item in items:
        feature_tokens = item.split('\t')
        for j in range(2):
            one_instance_items[j].append(feature_tokens[j])

print(one_instance_items)