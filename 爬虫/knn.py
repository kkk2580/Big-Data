#encoding:utf-8
import csv
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from math import sqrt
import operator as opt

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = np.zeros((np.shape(dataSet)))
	m = dataSet.shape[0]   #数据行数，也就是数据条目数
	normDataSet = dataSet - np.tile(minVals, (m, 1))
	normDataSet = normDataSet / np.tile(ranges, (m, 1))
	return normDataSet, ranges, minVals

def deal(filename):
	file = pd.read_csv(filename,encoding='gb18030')
	matrix_tran=[]
	for i in range(len(file)):
		line=[]
		line.append(file['价格'][i])
		line.append(file['销量'][i])
		line.append(file['店铺信誉分'][i])
		matrix_tran.append(line)
		level_tran.append(file['等级'][i])
	matrix_tran=DataFrame(matrix_tran)
	return matrix_tran

def level(filename):
	file = pd.read_csv(filename,encoding='gb18030')
	level_tran=[]
	for i in range(len(file)):
		level_tran.append(file['等级'][i])
	return level_tran


def kNN(dataSet, labels, testData, k):
	distSquareMat = (dataSet - testData) ** 2 # 计算差值的平方

	distSquareSums = distSquareMat.sum(axis=1) # 求每一行的差值平方和
	distances = distSquareSums ** 0.5 # 开根号，得出每个样本到测试点的距离
	sortedIndices = distances.argsort() # 排序，得到排序后的下标
	indices = sortedIndices[:k] # 取最小的k个
	labelCount = {} # 存储每个label的出现次数
	for i in indices:
		label = labels[i]
		labelCount[label] = labelCount.get(label, 0) + 1 # 次数加一
	sortedCount = sorted(labelCount.items(), key=opt.itemgetter(1), reverse=True) # 对label出现的次数从大到小进行排序
	return sortedCount[0][0] # 返回出现次数最大的label

	

if __name__ == "__main__":
	level_tran=level('训练集.csv')
	level_test=level('测试集.csv')
	matrix_tran=deal('训练集.csv')
	matrix_test=deal('测试集.csv')
	normDataSet, ranges, minVals=autoNorm(matrix_tran)
	result=[]
	for i in range(len(matrix_test)):
		normTestData = (matrix_test.iloc[i] - minVals) / ranges
		result.append(kNN(normDataSet, level_tran, normTestData, 5))
	mis=0
	print('预测结果：',result)
	print('标记结果：',level_test)
	for j in range(len(result)):
		if level_test[j]!=result[j]:
			mis=mis+1
	rat=mis/len(result)
	print("错误率:",rat)
