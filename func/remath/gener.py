# -*- coding: utf-8 -*-
# author: Minch Wu
"""生成器.

构建常用的生成器
"""

import numpy.lib.scimath as sp


def num(initN: int = 1, p: int = 1):
    """num.

    整数生成器
    """
    n = initN
    while True:
        yield (sp.power(n, p))
        n = n + 1


def fib():
    """Fib Number.

    斐波那契数列生成器
    """
    a, b = 0, 1
    while True:
        yield (b)
        a, b = b, a + b


# 模块测试
if __name__ == "__main__":
    num1 = num(1)
    for i in range(100):
        print(next(num1))
        # print(next(num(i)))
