# -*- coding: utf-8 -*-
"""pre.

主程序依赖项预处理
"""
import os

PKG = ['numpy', 'coolprop', 'matplotlib', 'sko']


def prerunning():
    """prerunning."""
    os.system(
        'pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple'
    )
    os.system('pip install pip -U')
    for each in PKG:
        os.system('pip install -U {0}'.format(each))


if __name__ == '__main__':
    prerunning()
    pass
