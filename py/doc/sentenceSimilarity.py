#coding:utf-8
import jieba
import  json
from gensim import corpora, models, similarities

def SentenceSim(str):
    #datapath = 'C://Users/zhangheng/Desktop/预料标注/train4_wenti_ChouQuX1.txt'
    datapath = './model/train.txt'
    class MyCorpus(object):
        def __iter__(self):
            for line in open(datapath,"r",encoding='utf-8'):
                yield line.split()

    Corp = MyCorpus()

    dictionary = corpora.Dictionary(Corp)


    corpus = [dictionary.doc2bow(text) for text in Corp]
    tfidf = models.TfidfModel(corpus)

   # corpus_tfidf = tfidf[corpus]

    query = str
    '''
    #分词
    seg_list = list(jieba.cut(query,cut_all = True))
    query = (','.join(seg_list)).replace(',',' ')
    '''

    vec_bow = dictionary.doc2bow(query.split())
    vec_tfidf = tfidf[vec_bow]
    #把所有评论做成索引
    #这种建立索引的方法，数据量大的情况下，会导致内存溢出
    #index = similarities.MatrixSimilarity(corpus_tfidf)
    #建议用 下面的方法  ， 这个类通过在硬盘的多个文件上分割索引

   # index = similarities.Similarity('./model/cm_txt', corpus_tfidf, len(dictionary))
    #index.save('./model/sim.index')

    index = similarities.MatrixSimilarity.load('./model/sim.index')
    sims = index[vec_tfidf]
    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
    #print( (sims))
    similarity = list(sort_sims)
    t1 = similarity[0][0]
    t2 = similarity[1][0]
    line1 = ''
    for x in (list(Corp))[t1]:
        line1 = line1+x + ' '
    line1 = line1.strip()

    line2 = ''
    for x in (list(Corp))[t2]:
        line2 = line2+x + ' '
    line2 = line2.strip()
    s = []
    s.append(line1)
    s.append(line2)
    print(s)
    j = json.dumps(s)
    return j

jj = SentenceSim('发票 哪里 下载 ？ ')
l = json.loads(jj)
print('ssssss:',l)
