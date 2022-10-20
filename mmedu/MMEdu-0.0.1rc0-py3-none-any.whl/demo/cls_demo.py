# from base import *
from MMEdu import MMClassification as cls

# 使用预训练的模型对图片进行推理，需要知道模型的名称和权重文件位置
def only_infer_demo():
	# 指定一张图片
	# img='car_plate.png'
	# img = '/home/user/桌面/pip测试4/dataset/cls/hand_gray/test_set/scissors/testscissors02-09.png'
	# img = 'testrock01-02.png'
	img = 'testIM/'
	# img = '5.gif'
	# img ='testIM/testIM/testrock01-02.png'
	# 实例化模型，网络名称为'LeNet'
	model = cls(backbone='LeNet')
	# 指定权重文件的路径
	# checkpoint = '/home/user/桌面/pip测试/cls/CLS1 (2)/CLS1/CLS/checkpoints/cls_model/cats_dogs/latest-res18.pth'
	checkpoint = '../checkpoints/cls_model/hand_gray_LeNet/latest.pth'
	# 指定训练集的路径，代表训练集中所包含的所有类别
	class_path = '../dataset/cls/hand_gray/classes.txt' 
	# class_path = '../dataset/cls/cats_dogs_dataset/classes.txt'
	# 推理，“show=True”表示不弹出识别结果窗口
	result = model.inference( image=img, show=False, class_path=class_path,checkpoint = checkpoint, device='cuda')
	# 输出结果，将inference函数输出的结果修饰后输出具体信息
	cn_result = model.print_result(result)
	import json
	with open("result.json",'w',encoding='utf-8') as f:
	    json.dump(result, f,ensure_ascii=False)

# 在预训练基础上继续训练
def continue_train_demo():
	# 实例化模型，网络名称为'LeNet'
	model = cls(backbone='LeNet')
	# 指定图片的类别数量
	model.num_classes = 3
		# model = cls(backbone='LeNet', num_classes = 3)
	# 指定数据集的路径
	model.load_dataset(path='../dataset/cls/hand_gray')
	# 指定新训练模型的保存路径
	model.save_fold = '../checkpoints/cls_model/hand_gray_continue'
	# 指定预训练模型的权重文件
	checkpoint = '../checkpoints/cls_model/hand_gray/latest.ph'
	# 在预训练权重文件的基础上继续训练，“validate=True”表示每轮训练后，在验证集上测试一次准确率
	model.train(epochs=5, validate=True, checkpoint=checkpoint)

# 从零开始训练模型
def normal_train_demo():
	# 实例化模型，网络名称为'LeNet'
	model = cls(backbone='LeNet')
	# 指定图片的类别数量
	model.num_classes = 3
	# 指定数据集的路径
	model.load_dataset(path='../dataset/cls/hand_gray')
	# model.load_dataset(path=223)

	# 指定保存模型配置文件和权重文件的路径
	model.save_fold = '../checkpoints/cls_model/hand_gray_LeNet'
	# 开始训练，轮次为10，“validate=True”表示每轮训练后，在验证集上测试一次准确率
	import time
	# a = time.time()
	model.train(epochs=2, validate=True, optimizer='Adagrad', device='cuda')
	# print("执行时间：",time.time() - a)
	# 训练结束后，可以用“model.inference”进行推理，看看效果。

def fast_infer_demo():
	# 指定一张图片
	# img='car_plate.png'
	img = '/home/user/桌面/pip测试4/dataset/cls/hand_gray/test_set/scissors/testscissors02-09.png'
	# img = 'testrock01-02.png'
	# img = 'cat3.jpeg'
	# 实例化模型，网络名称为'LeNet'
	model = cls(backbone='ResNet18')
	# 指定权重文件的路径
	# checkpoint = '/home/user/桌面/pip测试/cls/CLS1 (2)/CLS1/CLS/checkpoints/cls_model/cats_dogs/latest-res18.pth'
	checkpoint = '../checkpoints/cls_model/cats_dogs/latest-res18.pth'
	# 指定训练集的路径，代表训练集中所包含的所有类别
	class_path = '../dataset/cls/cats_dogs_dataset/classes.txt' 
	# class_path = '../dataset/cls/cats_dogs_dataset/classes.txt'
	# 推理，“show=True”表示不弹出识别结果窗口
	model.load_checkpoint(checkpoint=checkpoint, class_path=class_path,device='cpu')
	import time
	begin = time.time()
	for i in range(100):
		result = model.fast_inference(image=img)
		# 输出结果，将inference函数输出的结果修饰后输出具体信息
		# model.print_result(result)
	print(time.time() - begin)

if __name__ == "__main__":
	# 请按照次序逐一调用函数，训练模型要耗费较长时间。MMEdu的文档，可以获得更多帮助。
	# only_infer_demo()
	# continue_train_demo()
	# normal_train_demo()
	fast_infer_demo()