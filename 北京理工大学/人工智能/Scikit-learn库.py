#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/19 18:04
# @File : Scikit-learn库.py
# 导入Scikit-learn库和相关模块
# 导入Scikit-learn库和相关模块
from sklearn.linear_model import LinearRegression
import numpy as np

# 构造样本数据
x = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])
y = np.array([245000, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000])

# 将样本数据reshape为二维数组
x = x.reshape((-1, 1))

# 创建线性回归模型
model = LinearRegression()

# 将模型拟合到样本数据上
model.fit(x, y)

# 使用模型进行预测
x_test = np.array([2000]).reshape((-1, 1))
y_pred = model.predict(x_test)

# 输出预测结果
print("预测房价为：", y_pred)