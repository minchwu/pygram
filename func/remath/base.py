# -*- coding: utf-8 -*-
# author: Minch Wu
"""BASE.

functions of base module
"""

import os


def abs(x):
    """abs.

    return the absolute value of x
    """
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    else:
        return ([x, -x][x < 0])


def power(x, n: int = 2):
    """power.

    return the power value of x
    """
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return (s)


def sum(*X):
    """sum.

    return sum x**x of a list or tuple
    """
    s = 0
    for i in X:
        s += i**i
    return (s)


def dir(path: str = './', fix=None):
    """dir.

    return the file names of the path,
    args:
        fix: choice the suffix filename of file
    """
    if os.path.exists(path):
        if fix is None:
            return ([
                file for file in os.listdir(path)
                if os.path.splitext(file)[1] == fix
            ])
        else:
            return ([file for file in os.listdir(path)])
    else:
        print("The path <{}> is not exit!".format(path))
