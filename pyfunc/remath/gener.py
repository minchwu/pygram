# -*- coding: utf-8 -*-
# author: Minch Wu
"""生成器.

构建常用的生成器
"""

import numpy.random as random
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


def draw(N: int):
    """draw lots.

    抽签函数
    对N序列随机排序并逐个弹出
    """
    List = list(range(1, N + 1))
    while len(List) > 0:
        choice = List[random.randint(len(List))]
        yield("Num: {0},   Your order is {1}".format(N-len(List)+1, choice))
        List.remove(choice)
    pass


# 模块测试
if __name__ == "__main__":
    # num 测试
    # num1 = num(1)
    # for i in range(100):
    #     print(next(num1))
    #     # print(next(num(i)))

    # draw 测试
    ch = draw(6)
    for i in range(7):
        try:
            print(next(ch))
        except StopIteration:
            print("draw may be small for your choice")

    pass

