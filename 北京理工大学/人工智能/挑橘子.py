#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/22 18:07
# @File : 挑橘子.py
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 定义训练数据
X_train = np.array([[1.2, 3.5], [1.4, 3.2], [1.3, 3.6], [1.5, 3.9], [1.7, 3.6], [1.8, 3.2]])
y_train = np.array(['Orange', 'Orange', 'Orange', 'Orange', 'Orange', 'Orange'])

# 定义测试数据
X_test = np.array([[1.6, 3.4], [1.5, 3.5], [1.3, 3.3], [1.2, 3.7], [1.7, 3.4]])

# 定义KNN分类器
knn = KNeighborsClassifier(n_neighbors=3)

# 拟合数据
knn.fit(X_train, y_train)

# 预测测试数据
y_pred = knn.predict(X_test)

# 打印预测结果
print(y_pred)