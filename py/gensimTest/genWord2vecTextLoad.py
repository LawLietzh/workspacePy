#coding:utf-8
import gensim
#加载模型
model = gensim.models.word2vec.Word2Vec.load('./model/genWord2vec.model')
em = model['手机']
if '手机' in model:
    print('sssss')
else:
    print('ttttt')
print(type(model))
print(em.shape)
print(em)











