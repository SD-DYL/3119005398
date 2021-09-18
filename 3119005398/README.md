# 个人项目

----------

| 这个作业属于哪个课程 | [< 网工1934-软件工程 >](https://edu.cnblogs.com/campus/gdgy/networkengineering1934-Softwareengineering) |
|:-----------------:|:---------------:|
| 这个作业要求在哪里| [作业要求](https://edu.cnblogs.com/campus/gdgy/networkengineering1934-Softwareengineering/homework/12136) |
| 这个作业的目标 | 代码实现论文查重，性能分析，psp记录 |

#本作业代码已上传[个人github](https://github.com/SD-DYL/3119005398)

##一、psp表格
|PSP	|Personal Software Process Stages|预估耗时（分钟|	实际耗时（分钟）|
|:-:|:-:|:-:|:-:|
|Planning		|计划					|30 	| 20|
|Estimate		|估计这个任务需要多少时间	|	30	|10 |
|Development	|	开发					|	600	|400|
|Analysis		|需求分析(包括学习新技术)	|600	|1400|
|Design Spec	|生成设计文档			|30			|5|
|Design Review	|设计复审				|30			|20|
|Coding Standard|代码规范 (为目前的开发制定合适的规范)|	60	|50|
|Design			| 具体设计				|10		|5|
|Coding			| 具体编码				|120	|120|
|Code Review	| 代码复审				|20		|5|
|Test			| 测试（自我测试，修改代码，提交修改）	|30	|30|
|Reporting		|报告					|30		|40|
|Test Repor		|测试报告				|20		|10|
|Size Measurement|计算工作量				|10		|10|
|Postmortem & Process Improvement Plan|事后总结, 并提出过程改进计划|5	|5|
|Total			|	总计					|1530	|2130|

##二、模块接口的设计与实现过程
### 主要模块
1. jieba：中文分词组件
2. gensim：计算文本相似度的程序包。
2. re：处理字符串的正则表达式re包
### 主要函数
1. get_str：获取指定路径的文件内容
2. str_filter：去除停用词，结巴分词
3. caculate：计算余弦相似度
### 设计与实现过程
####str_filter函数
经查询得知，在计算文本相似度前，应先对文章进行分词，并且去除标点符号、常用词汇（停用词），这里用到强大的具有新词识别功能的[jieba中文分词](https://github.com/fxsjy/jieba)模块。
#####jieba.cut方法
```
  import jieba
    seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))
    #我/ 来到/ 北京/ 清华大学

    seg_list = jieba.cut("他来到了网易杭研大厦")
    print(", ".join(seg_list))
    #他, 来到, 了, 网易, 杭研, 大厦(此处，“杭研”并没有在词典中，但是也被算法识别出来了)
```

####caculate函数
caculate函数无疑是重中之重，在str_filter分词后，该函数应该使用算法返回查重结果。经查询得知，余弦定理是常见的相似度衡量方法之一，类似的相似度算法还有欧几里得距离、皮尔逊相关系数等等
#####余弦相似度
余弦距离，也称为余弦相似度，是用向量空间中两个向量夹角的余弦值作为衡量两个个体间差异的大小的度量。   
余弦值越接近1，就表明夹角越接近0度，也就是两个向量越相似，这就叫"余弦相似性"。
##性能分析
###代码覆盖率
![代码覆盖率](https://img2020.cnblogs.com/blog/2528879/202109/2528879-20210918213245844-791128062.png)
###各接口、函数运行时间
![运行时间](https://img2020.cnblogs.com/blog/2528879/202109/2528879-20210918213318824-1759068127.png)
##代码测试
###测试代码
第一个参数为原文路径，第二个为抄袭文路径，第三个为结果输出路径
`    main.py TestDemo/orig.txt TestDemo/orig_0.8_dis_15.txt Result/result.txt`


###测试结果
![测试结果](https://img2020.cnblogs.com/blog/2528879/202109/2528879-20210918213404701-2019029221.jpg)
###测试结果输出文档
![测试结果输出](https://img2020.cnblogs.com/blog/2528879/202109/2528879-20210918213451745-1039241720.jpg)
##异常处理
###设计目标：文件不存在异常处理
####代码示例
```

	if not os.path.exists(argv[1]):
		print("论文原文文件不存在！")
		exit()
```

####异常示例
#####用户错误输入用例
`	python main.py 2TestDemo/orig.txt TestDemo/orig_0.8_dis_15.txt Result/result.txt`
#####测试结果
![异常测试结果](https://img2020.cnblogs.com/blog/2528879/202109/2528879-20210918213550871-173241861.jpg)
