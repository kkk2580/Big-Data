import random
import os
from PIL import Image,ImageDraw,ImageFont

random.seed(3)
path_img="tran/"
path_img_test="test/"

def generate_single(z):
    # 先绘制一个50*50的空图像
    im_50_blank = Image.new('RGB', (50, 50), (255, 255, 255))

    # 创建画笔
    draw = ImageDraw.Draw(im_50_blank)

    font=ImageFont.truetype('simsun.ttc', 20)

    # xy是左上角开始的位置坐标
    draw.text(xy=(8, 6),font=font,text=z, fill=(0, 0, 0))

    # 随机旋转-10-10角度
    random_angle = random.randint(-10, 10)
    im_50_rotated = im_50_blank.rotate(random_angle)

    # 图形扭曲参数
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500]

    # 创建扭曲
    im_50_transformed = im_50_rotated.transform((100, 100), Image.PERSPECTIVE, params)

    # 生成新的30*30空白图像
    im_30 = im_50_transformed.crop([7, 7, 37, 37])

    return im_30, z

def generate(n,fonts,path_img):
	for m in range(len(fonts)):
		for j in range(0,n):
			# 调用生成图像文件函数
			im, generate_num = generate_single(fonts[m])

			# 取灰度
			im_gray = im.convert('1')

			print("Generate:", path_img + str(m) + "_" + str(j) + ".png")
			# 将图像保存在指定文件夹中
			im_gray.save(path_img  + str(m) + "_" + str(j) + ".png")
	print("\n")

def readFont():
	chinese=open('Chinese.txt','r')
	font=chinese.read()
	fonts=[]
	print(len(font))
	for i in font:
		fonts.append(i)
	return fonts

#制作训练数据
fonts=readFont()
generate(300,fonts,path_img)
generate(100,fonts,path_img_test)
