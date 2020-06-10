# -*- coding: utf-8 -*-
# author: Wu Mingchun
"""抽签.

对N成员序列进行随机抽签模拟
"""

import pyfunc.remath.gener as gener
import pyfunc.docfun.pyshell.dirsh as dirsh

# 输入成员数
N = int(input("Please input your number of members:\t"))
# 构建 N 成员抽签生成器
ch = gener.draw(N)

try:
    for each in range(N):
        print(next(ch))
    dirsh.exeHello("draw")
except StopIteration:
    dirsh.exeHello("StopInteration")
