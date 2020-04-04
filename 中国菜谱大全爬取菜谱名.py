# -*- coding: utf-8 -*-
import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库
import csv
import time

res_foods = requests.get('http://www.chinacaipu.com/menu/chinacaipu/index.html')
# 获取数据
bs_foods = BeautifulSoup(res_foods.content,'html.parser')

next_span = None

print(next_span)

list_all = []

# 1. 创建文件对象
f = open('dish.csv', 'w', newline='',encoding='utf-8-sig')

# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

i=2

while((next_span is None) == True) :
    # 解析数据
    list_foods = bs_foods.find_all('a',class_='lista')
    # 查找最小父级标签

    for food in list_foods:

        name=food.string

        print(name)

        if(name.find("的做法")!=-1):
            name.replace("的做法","")

        csv_writer.writerow([name])

    res_foods = requests.get('http://www.chinacaipu.com/menu/chinacaipu/index_'+str(i)+'.html')

    # 获取数据
    bs_foods = BeautifulSoup(res_foods.content,'html.parser')
    print(bs_foods)

    next_span = bs_foods.find(class_='disabled')
    print(next_span)

    i=i+1



