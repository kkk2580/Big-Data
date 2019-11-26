#encoding=utf-8
#上面这句话看起来是注释，但其实是有用的，指明了这个脚本的字符集编码格式
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains



class taobao_clawer:
	def __init__(self,url):
	    self.url = url
	    self.options = webdriver.ChromeOptions()
	    # 不加载图片,加快访问速度
	    self.options.add_experimental_option("prefs", {"profile.mamaged_default_content_settings.images": 2})
	    # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
	    self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
	    #self.options.add_argument('--proxy-server=127.0.0.1')
	    self.browser = webdriver.Chrome(executable_path='D:\\google\\chromedriver.exe', options=self.options)
	    self.wait = WebDriverWait(self.browser, 60)
	    self.browser.get(url)



	def login(self):
	    # 等待 密码登录选项 出现
	    print('开始登陆')
	    password_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
	    time.sleep(10)
	    print('login')


	#进入购物车
	def entershop(self):
		print('进入购物车')
		shop_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mc-menu-hd')))
		shop_button.click()

		
	#全选购物车点击购买
	def selectAll(self):
		print('全选')
		select_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_SelectAll1')))
		select_button.click()
		
	def buy(self):
		self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_FloatBar > div.float-bar-wrapper > div.float-bar-right > div.btn-area'))).click()
		print("1:",time.localtime(time.time()).tm_sec)
		self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#submitOrderPC_1 > div.wrapper > a.go-btn'))).click()
		print("2:",time.localtime(time.time()).tm_sec)

if __name__ == "__main__":

	url = 'https://login.taobao.com/member/login.jhtml'
	a = taobao_clawer(url)
	a.login()
	a.entershop()
	a.selectAll()
	global flag
	flag=0
	print("start")
	print(time.localtime(time.time()).tm_min,time.localtime(time.time()).tm_sec)
	while flag==0:
		localtime = time.localtime(time.time())
		hour=localtime.tm_hour
		minutes=localtime.tm_min
		sec=localtime.tm_sec
		if hour==14 and minutes==35 and sec==0:
			print("确认点击",time.localtime(time.time()).tm_sec)
			a.buy()
			print("点击结束",time.localtime(time.time()).tm_sec)
			flag=1
			print('购买成功')
			break;