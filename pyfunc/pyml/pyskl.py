# -*- coding: utf-8 -*-
# author: Minch Wu
"""pyskl.

基于sk-learn的函数接口
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

rng = np.random.RandomState(0)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
# plt.scatter(x, y)
# plt.show()

# 1. 实例化模型
model = LinearRegression(fit_intercept=True)
# 2. 整理数据，抽取特征矩阵和目标数组
X = x[:, np.newaxis]
# 3. 拟合数据
model.fit(X, y)
[a, b] = model.coef_, model.intercept_
xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)
plt.scatter(X, y)
plt.plot(Xfit, yfit)
plt.show()
