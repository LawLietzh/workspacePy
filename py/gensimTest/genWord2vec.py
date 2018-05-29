#coding:utf-8
import gensim
import os
#sentences = gensim.models.word2vec.Text8Corpus()

class MySentences(object):
    def __init__(self, dirname):
         self.dirname = dirname

    def __iter__(self):
        for line in open(self.dirname,'r',encoding='utf-8'):
            yield line.split()



path = 'C://Users/zhangheng/Desktop/预料标注/train4_wenti.txt'
sentences = MySentences(path)

#print(sentences[0:3])
model = gensim.models.word2vec.Word2Vec(sentences,size=100, alpha=0.015, window=3, min_count=2, iter=5)
model.save('./model/genWord2vec.model')
#不知道这个 有什么特殊用处
#model.save_word2vec_format("./model/genWord2vec.model",binary=True)
#model= gensim.models.word2vec.Word2Vec.load_word2vec_format("./text8.model.bin", binary=True)
em = model[u'手机']
print(em.shape)
print(em)
