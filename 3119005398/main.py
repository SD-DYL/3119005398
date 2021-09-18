from sys import argv
import jieba
import gensim
import re
import jieba.analyse
import html
import os


# 获取指定路径的文件内容
def get_str(route):
    f = open(route, 'r', encoding='utf-8')
    f_read = f.read()
    f.close()
    return f_read


# 去除停用词，结巴分词
def str_filter(string):
    jieba.analyse.set_stop_words('stopwords.txt')
    re_exp = re.compile(r'(<style>.*?</style>)|(<[^>]+>)', re.S)
    string = re_exp.sub(' ', string)
    string = html.unescape(string)
    res = [i for i in jieba.cut(string, cut_all=True) if i != '']
    keywords = jieba.analyse.extract_tags("|".join(res), topK=200, withWeight=False)
    return keywords


# 过滤后，计算余弦相似度
def calculate(text_a, text_b):
    texts = [text_a, text_b]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-temp', corpus, num_features=len(dictionary))
    test_corpus1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus1][1]
    return cosine_sim


if __name__ == '__main__':
    # 计算相似度
    # 返回原文分段后的字符串
    if not os.path.exists(argv[1]):
        print("论文原文文件不存在！")
        exit()
    if not os.path.exists(argv[2]):
        print("抄袭版论文文件不存在！")
        exit()
    str1 = get_str(argv[1])
    str2 = get_str(argv[2])

    # 过滤去除停用词并分词
    text1 = str_filter(str1)
    text2 = str_filter(str2)

    # 计算相似度
    sim = calculate(text1, text2)

    # 取小数点后四位
    result = round(sim.item(), 4)

    # 显示相似度
    resultStr = f'{argv[1]}和{argv[2]}余弦相似度为: %.2f%%' % (result*100)+"\n"
    print(resultStr)

    # 打开结果输出文件
    answer = open(argv[3], 'a+', encoding='utf-8')
    # 写入
    answer.writelines(resultStr)
    answer.close()
