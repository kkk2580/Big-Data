from __future__ import print_function
import numpy
import PIL.Image 
import csv
csv_file_tran=open("x.csv","w",encoding='utf-8',newline='')
writer_tran=csv.writer(csv_file_tran)
csv_file_test=open("y.csv","w",encoding='utf-8',newline='')
writer_test=csv.writer(csv_file_test)
file_tran='tran/'
file_test='test/'
def image_to_array(self,a,b,writer,file):
	"""
	将图片转化为数组并存为二进制文件
	"""
	print("开始将图片转化为数组")
	for i in range(0,a):
		for j in range(0,b):
			result=[]
			image = PIL.Image.open(file+str(i)+'_'+str(j)+'.png')
			out=image.convert("L")
			img=numpy.array(out)
			result.append(i)
			for m in range(0,30):
				for n in range(0,30):
					result.append(255-img[m][n])
			print(i)
			writer.writerow(result)
images1=[]
image_to_array(images1,500,300,writer_tran,file_tran)
csv_file_tran.close()
images2=[]
image_to_array(images2,500,100,writer_test,file_test)
csv_file_test.close()