from sys import argv
import jieba
import gensim
import re
import os
import jieba.analyse
import html

#获取指定路径的文件内容
def getStr(argv):
    f = open(argv, 'r', encoding='utf-8')
    f_read = f.read()
    f.close()
    return f_read
 
#去除停用词，结巴分词
def filter(string):
    jieba.analyse.set_stop_words('stopwords.txt')
    reExp = re.compile(r'(<style>.*?</style>)|(<[^>]+>)', re.S)
    string = reExp.sub(' ', string)
    string = html.unescape(string)
    result = [i for i in jieba.cut(string, cut_all=True) if i != '']
    keywords = jieba.analyse.extract_tags("|".join(result), topK=200, withWeight=False)
    return keywords
 
#过滤后，计算余弦相似度
def calculate(text1, text2):
    texts = [text1, text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-temp', corpus, num_features=len(dictionary))
    testCorpus1 = dictionary.doc2bow(text1)
    cosineSim = similarity[testCorpus1][1]
    return cosineSim
 
 
#计算相似度
#返回原文分段后的字符串
str1 = getStr(argv[1])
str2 = getStr(argv[2])

#过滤去除停用词并分词
text1 = filter(str1)
text2 = filter(str2)

#计算相似度
sim = calculate(text1, text2)

#取小数点后四位
result=round(sim.item(),4)

#显示相似度
resultStr = f'{argv[1]}和{argv[2]}余弦相似度为: %.2f%%' % (result*100)+"\n"
print(resultStr)

#打开结果输出文件
answer = open(argv[3],'a+',encoding='utf-8')
#写入
answer.writelines(resultStr)
answer.close()
