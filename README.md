data目录下包括公司数据:

公司数据：
company_industry50W.xlsx

行业数据：
t.xls

自定义分词库：
disc.txt

停词库:
stopword.txt

关词词提取:companInfoEtl.py文件

里面两个方法：

readInFile：方法提取行业关键词

readCompanyFile：方法提取公司经营范围关键词


对于不需要的关键词可以加入到stopword.txt当中
对于分词不准关键词可以加入到dict.txt


