# -*- coding: utf-8 -*-
# author: Minch Wu
"""numcal.

数值计算库
对常见的数值算法基于python二次实现.
TODO: 高斯消元法，龙格库塔法，。。。
"""

import sympy as sp
from sympy import symbols

# sp.Symbol('t')
x, y = symbols('x, y')
print(type(x), type(y))
