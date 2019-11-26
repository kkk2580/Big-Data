# coding=utf-8
import os
from selenium import webdriver
import datetime
import time
from os import path
 
#此处chromedriver改为自己下载的路径
options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
driver = webdriver.Chrome("D:\\google\\chromedriver.exe",chrome_options=options)
# driver.create_options().add_argument('--log-level=3')
#driver.maximize_window()
 
def login():
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(60)
        driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    now = datetime.datetime.now()
    print("login success:", now.strftime("%Y-%m-%d %H:%M:%S"))
 
def buy(buytime,flag):
   while flag==0:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > times:
            # 点击结算按钮
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
            while True:
                try:
                    if driver.find_element_by_link_text("结 算"):
                        driver.find_element_by_link_text("结 算").click()
                        print(f"结算成功，准备提交订单",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                        break
                except:
                    pass
            # 点击提交订单按钮
            while True:
                try:
                    if driver.find_element_by_link_text('提交订单'):
                        driver.find_element_by_link_text('提交订单').click()
                        print("抢购成功，请尽快付款",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                        flag=1
                        break
                except:
                    print("再次尝试提交订单")
            time.sleep(0.01)
 
if __name__ == "__main__":
    times ="2019-11-11 00:00:00"
    login()
    flag=0
    buy(times,flag)