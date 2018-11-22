from math import log


def createDataSet():
	dataSet = [[0, 0, 0, 0, 'no'],  # 数据集
	           [0, 0, 0, 1, 'no'],
	           [0, 1, 0, 1, 'yes'],
	           [0, 1, 1, 0, 'yes'],
	           [0, 0, 0, 0, 'no'],
	           [1, 0, 0, 0, 'no'],
	           [1, 0, 0, 1, 'no'],
	           [1, 1, 1, 1, 'yes'],
	           [1, 0, 1, 2, 'yes'],
	           [1, 0, 1, 2, 'yes'],
	           [2, 0, 1, 2, 'yes'],
	           [2, 0, 1, 1, 'yes'],
	           [2, 1, 0, 1, 'yes'],
	           [2, 1, 0, 2, 'yes'],
	           [2, 0, 0, 0, 'no']]
	labels = ['年龄', '有工作', '有自己的房子', '信贷情况']  # 分类属性

	return dataSet, labels  # 返回数据集和分类属性


def calcShannonEnt(dataSet):
	numEntires = len(dataSet)
	# 返回数据集的⾏数
	labelCounts = {}
	# 保存每个标签(Label)出现次数的字典
	for featVec in dataSet:
		# 对每组特征向量进⾏统计
		currentLabel = featVec[-1]
		# 提取标签(Label)信息
		if currentLabel not in labelCounts.keys():
			# 如果标签(Label)没有放⼊统计次数的字典,添加进去
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	# Label计数
	shannonEnt = 0.0
	# 经验熵(香农熵)
	for key in labelCounts:
		# 计算香农熵
		prob = float(labelCounts[key]) / numEntires
		# 选择该标签(Label)的概率
		shannonEnt -= prob * log(prob, 2)
	# 利⽤公式计算
	return shannonEnt


def splitDataSet(data_set, axis, value):
	ret_data_set = []
	# 创建返回的数据集列表
	for featVec in data_set:
		# 遍历数据集
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			# 去掉axis特征
			reducedFeatVec.extend(featVec[axis + 1:])
			# 将符合条件的添加到返回的数据集
			ret_data_set.append(reducedFeatVec)
	return ret_data_set


def chooseBestFeatureToSplit(data_set):
	num_features = len(data_set[0]) - 1
	# 特征数量
	base_entropy = calcShannonEnt(data_set)
	# 计算数据集的⾹农熵
	best_info_gain = 0.0
	# 信息增益
	best_feature = -1
	# 最优特征的索引值
	for i in range(num_features):
		# 遍历所有特征
		# 获取dataSet的第i个所有特征
		feat_list = [example[i] for example in data_set]
		unique_vals = set(feat_list)
		# 创建set集合{},元素不可重复
		new_entropy = 0.0
		# 经验条件熵
		for value in unique_vals:
			# 计算信息增益
			sub_data_set = splitDataSet(data_set, i, value)
			# subDataSet划分后的⼦集
			prob = len(sub_data_set) / float(len(data_set))
			# 计算⼦集的概率
			new_entropy += prob * calcShannonEnt(sub_data_set)
		# 根据公式计算经验条件熵
		info_gain = base_entropy - new_entropy
		# 信息增益
		print("第%d个特征的增益为%.3f" % (i, info_gain))
		# 打印每个特征的信息增益
		if info_gain > best_info_gain:
			# 计算信息增益
			best_info_gain = info_gain
			# 更新信息增益，找到最⼤的信息增益
			best_feature = i
	# 记录信息增益最⼤的特征的索引值
	return best_feature


# 返回信息增益最⼤的特征的索引值
# dataSet, features = createDataSet()
# print("最优特征索引值:" + str(chooseBestFeatureToSplit(dataSet)))

"""======================================================"""
"""代码构建决策树
函数说明:统计classList中出现此处最多的元素(类标签)
Parameters:
 classList - 类标签列表
Returns:
 sortedClassCount[0][0] - 出现此处最多的元素(类标签)
"""

def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		# 统计classList中每个元素出现的次数
		if vote not in classCount.keys(): classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	# 根据字典的值降序排序
	return sortedClassCount[0][0]
	# 返回classList中出现次数最多的元素



"""
函数说明:创建决策树
Parameters:
 dataSet - 训练数据集
 labels - 分类属性标签
 featLabels - 存储选择的最优特征标签
Returns:
 myTree - 决策树
"""
def createTree(dataSet, labels, featLabels):
	classList = [example[-1] for example in dataSet]
	# 取分类标签(是否放贷: yes or no)

	if classList.count(classList[0]) == len(classList):
		# 如果类别完全相同则停⽌继续划分
		return classList[0]

	if len(dataSet[0]) == 1:
		# 遍历完所有特征时返回出现次数最多的类标签
		return majorityCnt(classList)

	bestFeat = chooseBestFeatureToSplit(dataSet)
	# 选择最优特征
	bestFeatLabel = labels[bestFeat]
	# 最优特征的标签
	featLabels.append(bestFeatLabel)
	myTree = {bestFeatLabel: {}}
	# 根据最优特征的标签⽣成树
	del (labels[bestFeat])
	# 删除已经使⽤特征标签
	featValues = [example[bestFeat] for example in dataSet]
	# 得到训练集中所有最优特征的属性值
	uniqueVals = set(featValues)
	# 去掉重复的属性值
	for value in uniqueVals:
		# 遍历特征，创建决策树。
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), labels, featLabels)
	return myTree


dataSet, labels = createDataSet()
featLabels = []
myTree = createTree(dataSet, labels, featLabels)
print(myTree)

"""========================================================="""
"""使用决策树执行分类
函数说明:使用决策树分类
Parameters:
 inputTree - 已经生成的决策树
 featLabels - 存储选择的最优特征标签
 testVec - 测试数据列表，顺序对应最优特征标签
Returns:
 classLabel - 分类结果
"""


def classify(inputTree, featLabels, testVec):
	firstStr = next(iter(inputTree))
	# 获取决策树结点
	secondDict = inputTree[firstStr]
	#下⼀个字典
	featIndex = featLabels.index(firstStr)
	for key in secondDict.keys():
		if testVec[featIndex] == key:
			if type(secondDict[key]).__name__ == 'dict':
				classLabel = classify(secondDict[key], featLabels, testVec)
			else:
				classLabel = secondDict[key]
	return classLabel


dataSet, labels = createDataSet()
featLabels = []
myTree = createTree(dataSet, labels, featLabels)
testVec = [0,1] #测试数据
result = classify(myTree, featLabels, testVec)
if result == 'yes':
	print('放贷')
if result == 'no':
	print('不放贷')


"""===================================="""
"""决策树的存储

函数说明:存储决策树
Parameters:
 inputTree - 已经生成的决策树
 filename - 决策树的存储文件名
Returns:
 ⽆
"""
import pickle


def storeTree(inputTree, filename):
	with open(filename, 'wb') as fw:
		pickle.dump(inputTree, fw)


myTree = {'有自己的房子': {0: {'有工作': {0: 'no', 1: 'yes'}}, 1: 'yes'}}
storeTree(myTree, 'classifierStorage.txt')


"""函数说明:读取决策树
Parameters:
 filename - 决策树的存储⽂件名
Returns:
 pickle.load(fr) - 决策树字典
"""
def grabTree(filename):
	fr = open(filename, 'rb')
	return pickle.load(fr)


myTree = grabTree('classifierStorage.txt')
print(myTree)


if __name__ == '__main__':
	# dataSet, features = createDataSet()
	# print(dataSet)
	# print(calcShannonEnt(dataSet))
	pass