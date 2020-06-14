# -*- coding: utf-8 -*-
# author: Mingchun Wu
"""pyplot.

python绘图二次封装
基于matplotlib等常用绘图库，实现绘图函数类与显示配置分类，方便科学绘图调用

关于绘图函数接口
# ## matplotlib
# matplotlib 提供了较为完整的matlab式绘图API，这种绘图代码简洁；
#
# 一般语法为plt.func
#
# 对于复杂绘图的支持，matplotlib 可以用面向对象的API接口实现
#
# 通过图层一步步搭建图形 figure->axes->axis，对于子图的设置为axes.set_prop
"""

import os
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
import mpl_toolkits.mplot3d as plt3
import json
'''布局设置.
全局固定设置'''

# 屈居布局参数设置
plt.rcParams.update({
    'font.size': 18,
    'font.family': 'Serif',
    'text.usetex': False
})
# 中文显示设置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 格式设置.科学计数
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
# formatter.set_powerlimits((-1,2))
# x和y轴 坐标轴数字与轴的距离
plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5
'''加载默认绘图配置.
实现属性与数据分离'''
with open("./config.json", "r") as f:
    KARGS = json.load(f)

while True:
    key_function_or_data = input(
        "function-plot[f] or data-plot[d] or just exit[x]?\n")
    if key_function_or_data == 'f':
        dataX = input('please input your x list func:\n')
        dataY = input('please input your y list func:\n')
        exec("dataX = {}".format(dataX))
        exec("dataY = {}".format(dataY))
        exec("plt.plot(dataX, dataY, **KARGS['plot'])")
        exec("plt.show()")
    elif key_function_or_data == 'd':
        data = pd.read_csv("./src.csv")
        plt.plot(data['x'], data['y'], **KARGS['plot'])
        plt.show()
    elif key_function_or_data == 'x':
        os._exit(0)
