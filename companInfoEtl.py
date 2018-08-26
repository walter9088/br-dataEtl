#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd
import jieba

import re
import jieba.analyse






list_keys=[]

list_in_keys = []

list_co_keys = []

jieba.analyse.set_stop_words("data/stopword.txt")
jieba.load_userdict("data/dict.txt")


def readInFile():
    data = xlrd.open_workbook("data/t.xls")

    table = data.sheet_by_index(0)

    for i in range(0, 1167):

        v_cell2 = table.cell(i, 5).value
        if isinstance(v_cell2,unicode):
            match = re.sub(ur'\w', "", v_cell2)
            keywords = jieba.analyse.extract_tags(match, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
            # 访问提取结果
            for item in keywords:
                list_keys.append(item[0])
                list_in_keys.append(item[0])




def readCompanyFile():
    data = xlrd.open_workbook("data/company_industry50w.xlsx")

    table = data.sheet_by_index(0)

    for i in range(0, 10000):

        v_cell2 = table.cell(i, 2).value
        if isinstance(v_cell2,unicode):
            match = re.sub(ur'[\(（\[].*[\)）\]]', "", v_cell2)
            keywords = jieba.analyse.extract_tags(match, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
            # 访问提取结果
            for item in keywords:
                list_keys.append(item[0])
                list_co_keys.append(item[0])


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

   createFile(list_in_keys,'dict_in.txt')
   createFile(list_co_keys, 'dict_co.txt')
   createFile(list_keys, 'dict.txt')















