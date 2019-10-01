from selenium import webdriver
import csv
import time
import pandas as pd

file = pd.read_csv('shop.csv',encoding='gb18030')
name=file['店铺']

chromedriver_path="D:\\google\\chromedriver.exe"#驱动链接
options = webdriver.ChromeOptions()
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
options = webdriver.ChromeOptions()
# 不加载图片,加快访问速度
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 

url='https://taodaxiang.com/score/index/init'

driver.get(url)

search=driver.find_element_by_id("ww")
score=[]
for i in name:
	search.clear()
	search.send_keys(i)
	time.sleep(3)
	button = driver.find_element_by_xpath("//*[@id='score_form']/div[1]/input")
	button.click()
	time.sleep(5)
	num=driver.find_element_by_id("item_score")
	score.append(num.text)

file['分数']=score

file.to_csv('shop.csv')