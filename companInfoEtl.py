#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd
import jieba

import re
import jieba.analyse


g_dict ={}
c_dict = {}

jieba.analyse.set_stop_words("data/stopword.txt")
jieba.load_userdict("data/dict.txt")


def readInFile():
    data = xlrd.open_workbook("data/t.xls")

    table = data.sheet_by_index(0)
    old_str_v_cell3 = ""
    for i in range(6, 1167):

        v_cell3 = table.cell(i, 3).value
        str_v_cell3 =''

        v_cell4 = ''
        v_cell5 =''

        if v_cell3 != "":
            if isinstance(v_cell3,unicode):
                str_v_cell3 = str(v_cell3)

            if isinstance(v_cell3,float):
                str_v_cell3 = str(int(v_cell3))

        if old_str_v_cell3 != str_v_cell3:
            v_cell4 = table.cell(i, 4).value
            v_cell5 = table.cell(i, 5).value
            old_str_v_cell3 = str_v_cell3
        else:
            continue;


        if isinstance(v_cell5,unicode):
            match = re.sub(ur'\w', "", v_cell5)
            keywords = jieba.analyse.extract_tags(match, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
            # # 访问提取结果
            list_g_keys = []
            for item in keywords:
                list_g_keys.append(item[0])

            g_dict[v_cell4] = list_g_keys


def readCompanyFile():
    data = xlrd.open_workbook("data/company_industry50w.xlsx")

    table = data.sheet_by_index(0)

    for i in range(0, 10000):

        v_cell1 = table.cell(i, 0).value
        v_cell2 = table.cell(i, 2).value

        if isinstance(v_cell2,unicode):
            match = re.sub(ur'[\(（\[].*[\)）\]]', "", v_cell2)
            keywords = jieba.analyse.extract_tags(match, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
            list_c_keys = []
            # 访问提取结果
            for item in keywords:
                list_c_keys.append(item[0])
            c_dict[v_cell1] = list_c_keys



def createFile(list_keys,string):
    dict_f = open('out/dict.txt', 'w+')

    list_key = {}.fromkeys(list_keys).keys()
    for key in list_key:
        dict_f.writelines(key.encode('utf-8') + ' ' + 'brn')
        dict_f.writelines('\n')

    dict_f.close()


if __name__ == "__main__":

   readInFile()

   readCompanyFile()

   for (c_k,c_v) in c_dict.items():

       for (g_k,g_v) in g_dict.items():
           r_l = list((set(c_v).union(set(g_v)))^(set(c_v)^set(g_v)))
           if len(r_l)>0:
            #print str(c_v).decode('unicode-escape'),str(g_v).decode('unicode-escape'),str(r_l).decode('unicode-escape')
            print u"公司:========"+c_k+u":===========,在国民经济行业：========"+g_k+u"：========下有关键词匹配成功能，关键词是："+str(r_l).decode('unicode-escape')





   #createFile(list_in_keys,'dict_in.txt')
   #createFile(list_co_keys, 'dict_co.txt')
   #createFile(list_keys, 'dict.txt')















