#encoding:utf-8
import csv
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

# #合并两张表格
# file = pd.read_csv('sort1.csv',encoding='utf-8')
# shop=pd.read_csv('shop.csv',encoding='gb18030')
# file['店铺信誉分']=None

# for i in range(len(shop)):
# 	number=shop['分数'][i]
# 	name=shop['店铺'][i]
# 	print(name)
# 	for j in range(len(file)):
# 		print(file['销量'][j])
# 		if file['店铺'][j]==name:
# 			print(number)
# 			file['店铺信誉分'][j]=number


# file.to_csv('sort2.csv')
# print("end")

#划分样本集和测试集
file = pd.read_csv('sort2.csv',encoding='gb18030')
file = file.sample(frac=1.0)  # 全部打乱
cut_idx = int(round(0.1 * file.shape[0]))
file_test, file_train = file.iloc[:cut_idx], file.iloc[cut_idx:]
file_test.to_csv('测试集.csv')
file_train.to_csv('训练集.csv')