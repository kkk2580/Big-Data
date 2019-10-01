import numpy
import scipy.special
import matplotlib.pyplot as plt
import random

class neuralNetwork:

    # 初始化函数，设定输入层节点，隐藏层节点和输出层节点数量
    def __init__(self,inputNodes,hiddenNodes,outputNodes,learningRate):
        self.iNodes = inputNodes
        self.hNodes = hiddenNodes
        self.oNodes = outputNodes

        self.lr = learningRate

        # 正态分布的随机初始化权重矩阵
        self.weights_ih = numpy.random.normal(0.0,pow(self.hNodes, -0.5),(self.hNodes,self.iNodes))
        self.weights_ho = numpy.random.normal(0.0,pow(self.oNodes, -0.5),(self.oNodes,self.hNodes))

        # 定义激活函数（S函数）
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    # 网络训练函数，学习给定训练集样本后，优化权重
    def train(self,inputs_list,targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list,ndmin=2).T

        hidden_inputs = numpy.dot(self.weights_ih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.weights_ho, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.weights_ho.T,output_errors)

        self.weights_ho += self.lr * numpy.dot((output_errors * final_outputs * (1 - final_outputs)),numpy.transpose(hidden_outputs))
        self.weights_ih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1 - hidden_outputs)),numpy.transpose(inputs))

        pass

    # 查询函数，给定输入，从输出节点给出答案
    def query(self,inputs_list):

        inputs = numpy.array(inputs_list,ndmin=2).T

        hidden_inputs = numpy.dot(self.weights_ih,inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.weights_ho,hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

def readFont():
    chinese=open('Chinese.txt','r')
    font=chinese.read()
    fonts=[]
    for i in font:
        fonts.append(i)
    return fonts

fonts=readFont()
input_nodes = 900
hidden_nodes = 350
output_nodes = 500
learning_rate =0.2
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)

# 训练神经网络
# 读取训练数据文件中的数据，并保存到列表中
training_data_file = open("x.csv",'r')
training_data_list = training_data_file.readlines()
training_data_file.close()
random.shuffle(training_data_list)
q=0
for records in training_data_list:
    all_values = records.split(',')
    inputs = (numpy.asfarray(all_values[1:]) / 255 * 0.99) + 0.01
    targets = numpy.zeros(output_nodes) + 0.01
    targets[int(all_values[0])] = 0.99
    # 训练
    n.train(inputs, targets)
    q=q+1
    print(q)
# 读取测试数据
test_data_file = open("y.csv",'r')
test_data_list = test_data_file.readlines()
test_data_file.close()
correct_label=[]
random.shuffle(test_data_list)
label=[]
for data in test_data_list:
    all_values = data.split(',')
    correct_label.append(all_values[0])
    inputs = (numpy.asfarray(all_values[1:]) / 255 * 0.99) + 0.01
    outputs = n.query(inputs)
    label.append(numpy.argmax(outputs))
# print("correct_label",correct_label)
# print("label:",label)
acc=0
for i in range(len(correct_label)):
    if correct_label[i]==str(label[i]):
        acc=acc+1
print("准确率：",acc/len(correct_label)*100,'%')


# 单个实例与图片对比
x = test_data_list[600].split(',')
correct_label = x[0]
print("该文字为:",fonts[int(correct_label)])
inputs = (numpy.asfarray(x[1:]) / 255 * 0.99) +0.01
outputs = n.query(inputs)
label = numpy.argmax(outputs)
print("识别的文字是：",fonts[label])
#绘制手写汉字的图像
image_array = numpy.asfarray(x[1:]).reshape(30,30)
plt.imshow(image_array,cmap='Greys',interpolation='None')
plt.show()
