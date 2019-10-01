#encoding:utf-8
import csv
import pandas as pd
import numpy as np

file = pd.read_csv('result.csv',encoding='gb18030',usecols=[0,1,2,3])

#清洗销量中不符合格式的数据
for i in range(len(file['销量'])):
	if '人付款' in file['销量'][i]:
		continue
	else:
		file['销量'][i]='0'


#转换销量
for i in range(len(file['销量'])):
	file['销量'][i]=file['销量'][i].replace('人付款','')
	file['销量'][i]=file['销量'][i].split('+')[0]
	if '万' in file['销量'][i]:
		number=float(file['销量'][i].split('万')[0])
		real=number*10000
		file['销量'][i]=int(real)
	else:	
		file['销量'][i]=int(file['销量'][i])


#清洗销量小于1000的数据
invalid=0
#print(len(file))
for i in range(len(file['销量'])):
	if file['销量'][i]<1000:
		invalid=invalid+1
		file.drop([i],inplace=True)


#转换价格的数据格式
data=[]
for i in file['价格']:
	if '￥' in i:
		i=i.replace('￥','')
		i=i.replace(',','')
		i=float(i)
		data.append(i)
	else:
		continue
file['价格']=data


#按销量价格降序排列
file=file.sort_values(['销量','价格'],ascending=False)


#去除重复数据
file=file.drop_duplicates()

# #形成店铺表格
# shop=file['店铺']
# shop=shop.drop_duplicates()
# print(shop)
# print(len(shop))

# shop.to_csv('shop.csv')
#file.to_csv('sort1.csv')

