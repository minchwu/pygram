# -*- coding: utf-8 -*-
# author: Minch Wu
"""pyplt.

绘图函数接口
# ## matplotlib
# matplotlib 提供了较为完整的matlab式绘图API，这种绘图代码简洁；
#
# 一般语法为plt.func
#
# 对于复杂绘图的支持，matplotlib 可以用面向对象的API接口实现
#
# 通过图层一步步搭建图形 figure->axes->axis，对于子图的设置为axes.set_prop

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import mpl_toolkits.mplot3d as plt3

# 全局布局参数设置
plt.rcParams.update({
    'font.size': 18,
    'font.family': 'Serif',
    'text.usetex': False
})
# 中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 格式设置
# 科学计数
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1, 2))
# x和y轴的距离和坐标轴上的数字
plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5

x1 = np.arange(0, np.pi, 0.01 * np.pi)
y1 = x1**np.sin(x1)
fig, ax = plt.subplots(figsize=(9, 6), num=1)
ax.plot(x1, y1, 'r')
plt.title("$y = x^{sin(x)}$", fontsize=21)
plt.legend(labels=["$x^{sin(x)}$"], loc="best", fontsize=21)
plt.xlim(0, np.pi + 0.1)
plt.ylim(0.3, 2.1)
xtick = ["0", "1/4π", "1/2π", "3/4π", "π"]
plt.xticks(ticks=np.arange(0, np.pi + 0.1, 0.25 * np.pi),
           labels=xtick,
           fontsize=17)
plt.yticks(ticks=np.arange(0.5, 2.1, 0.5),
           labels=["0.5", "1", "1.5", "2"],
           fontsize=17)
plt.box(False)
plt.grid(True, color="c", which="major", axis="both")

x = np.linspace(0, np.pi, 101)
y = np.exp(-1 / (np.power(x, 2) + 1))
# plt.figure(num=1,figsize=(8,6),dpi=80)
fig, ax = plt.subplots(ncols=1, nrows=1, num=2, figsize=(8, 6), dpi=80)
fig.suptitle("figure", fontsize=21)
ax.plot(x, y, color="#000FFF", lw=1.5, ls="-", label=r"$e^{-\frac{1}{x^2+1}}$")
ax.legend(loc="best", fontsize=21)
ax.grid(b=True, which="both", color="c", ls="-.")
ax.grid(b=False)
plt.xlabel(xlabel="X", fontsize=17)
plt.ylabel(ylabel="Y", fontsize=17)
plt.xlim(0, np.pi)
plt.ylim(0.3, 1)
plt.xticks(np.linspace(0, np.pi, 5), ["0", "1/4π", "1/2π", "3/4π", "π"],
           fontsize=17)
plt.yticks(np.linspace(0.3, 1, 8), fontsize=17)
# fig.add_axes((0.7,0.7,0.3,0.3))
plt.show(fig)

x = np.linspace(0, 2 * np.pi, 101)
y = np.sin(x)
plt.figure(figsize=(8, 6), num=3)
plt.plot(x, y, color="r", ls="--", lw=1.5, marker="o")
plt.axis([0, 2 * np.pi, -1, 1])
plt.xlabel("x 轴", fontsize=17)
plt.ylabel("y 轴", fontsize=17)
plt.title("正弦函数", fontsize=21)
plt.grid(True, color="c", ls="-.")
plt.annotate(":我是(π,0)",
             xy=(np.pi, 0),
             xytext=(3 / 2 * np.pi, 0.5),
             fontsize=13,
             arrowprops=dict(facecolor="b", shrink=0.1))
plt.show()

θ = np.linspace(0, 2 * np.pi, 361)
ρ = np.sin(θ)**2 + np.cos(θ)**2
fig, ax = plt.subplots(num=4)
plt.polar(θ, ρ)
plt.show()

x = np.linspace(0, 10 * np.pi, 370)
y = x**2
fig = plt.figure(num=5, figsize=(8, 6), dpi=80)
fig.suptitle(t="OOP", x=0.5, y=0.9, fontsize=21)
ax1 = fig.add_axes([0.1, 0.1, 0.6, 0.6])  # 左侧间距，底部间距，宽度，高度([0,1])，为fig图框的比例值
ax1.plot(x,
         y,
         color='r',
         ls='-',
         marker='.',
         markerfacecolor='blue',
         markersize=0.5,
         markeredgewidth=2,
         markeredgecolor='black',
         label="$x^2$")
ax1.set_xscale('log')
ax1.yaxis.set_major_formatter(formatter)
ax1.set_xlabel("x")
ax1.set_ylabel("Y")
# 坐标轴标签和坐标轴数字的距离
ax1.xaxis.labelpad = -5
ax1.yaxis.labelpad = -5
ax1.set_title("$x^2$", fontsize=17)
ax1.grid(b=True, color='c', ls='--', alpha=1, lw=1.5)
ax1.legend(loc=0, fontsize=17)

ax2 = fig.add_axes([0.7, 0.7, 0.2, 0.2])
ax2.plot(x, np.sin(x))
ax2.set_xlabel("x")
ax2.set_ylabel("Y")
ax2.set_title("$sin(x)$")
ax2.grid(b=True, color='c')

# fig.tight_layout()
# fig.show()   # 可用于绘图后端GUI
# plt.show(fig)
# fig.savefig("OOP.png")
# plt.savefig("OOP.tiff")

# 坐标轴独立设置

x = np.linspace(0, 2 * np.pi, 101)
y = np.exp(-x**2)
fig, ax = plt.subplots(num=6)
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('blue')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()

# 多轴绘图
x = np.linspace(0, 2 * np.pi, 101)
y = 1 / (np.log(np.sqrt(x) + 1) + 1) * np.sin(x)

fig, ax1 = plt.subplots(num=7)
ax1.plot(x, y)
ax1.set_xlim([0, 2 * np.pi])
ax1.set_ylim(ymin=-1 / 2, ymax=1)
ax1.set_ylabel(r"$\frac{sin(x)}{ln(\sqrt{x}+1)+1)}$", fontsize=17)
ax2 = ax1.twinx()
ax2.plot(
    x,
    y * np.sin(x),
    color='r',
)
ax2.set_ylabel(r"$\frac{sin^2(x)}{ln(\sqrt{x}+1)+1)}$", fontsize=17)
# ax3 = ax2.twinx()

x = np.linspace(0, 2 * np.pi, 101)
y = np.cos(x)
fig, ax = plt.subplots(num=8)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('axes',0.5))
ax.spines['bottom'].set_position(('data', -1))
# ax.spines['left'].set_position(('axes',0.5))
ax.spines['left'].set_position(('data', 0))
ax.plot(x, y)
# fig.show()

# ## **kargs 调用
# 通过关键字参数的解析调用，可以将绘图参数集中到字典中，统一处理，可以用于GUI编程中的可选参数调节

x = np.linspace(0, 2 * np.pi, 361)
y = np.sin(x)
fig, ax = plt.subplots(num=9)
kargs = {'color': '#BB00CC', 'linewidth': 1.5}
plt.plot(x, y, **kargs)

# ## 3D 绘图

fig = plt.figure(num=10)
ax3 = plt3.Axes3D(fig)

x = np.linspace(-np.pi, np.pi, 361)
y = np.linspace(-np.pi, np.pi, 361)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2)) + np.exp((X**2 + Y**2) / (2 * np.pi**2))
ax3.plot_surface(X, Y, Z, cmap='rainbow')
