# -*- coding: utf-8 -*-
# author: Minch Wu
"""init.

添加文件搜索路径
更改python安装源
pkg 依赖包批量安装
"""

import os
import sys
import platform


def exeHello(funName: str):
    """exeHello.

    程序结束运行报告
    """
    print("This is <{0}>, everything is done!".format(funName))


def pkgPath():
    """pkgPath.

    在 python 根目录添加.pth路径文件
    """
    # 获取python安装目录
    pth = sys.exec_prefix
    pkg = os.path.join(pth, 'pkg.pth')
    ''' 读写区分
    if not os.path.exists(pkg):
        with open(pkg, 'w', encoding='utf-8') as pkh:
            pkh.write(os.getcwd())
    else:
        with open(pkg, 'r+', encoding='utf-8') as pkh:
            pkh.write(os.getcwd())
    '''

    # 作为临时工作目录修改
    with open(pkg, 'w', encoding='utf-8') as pkh:
        # 将当前工作目录，即顶层目录写入路径文件
        pkh.write(os.getcwd())
        print("path: \"{0}\" is added to \"{1}\"".format(os.getcwd(), pkg))

    exeHello('pkgPath')


def pipy():
    """pipy.

    检测平台，更改pip安装源
    """
    plat = platform.system()
    pipPathW = os.path.join(os.path.expandvars('$HOME'), 'pip')
    # 函数测试
    # pipPathW = './demo/pip'
    pipPathL = os.path.join(os.path.expandvars('$HOME'), '.pip')
    pipSource = "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple"

    if plat == 'Windows':
        print("Your system is {0}!".format(plat))
        if not os.path.exists(pipPathW):
            os.mkdir(pipPathW)
            with open(os.path.join(pipPathW, 'pip.ini'), 'w',
                      encoding='utf-8') as p:
                p.write(pipSource)
        elif not os.path.exists(os.path.join(pipPathW, 'pip.ini')):
            with open(os.path.join(pipPathW, 'pip.ini'), 'w',
                      encoding='utf-8') as p:
                p.write(pipSource)
        else:
            print("{0} already exists!".format("pip.ini"))

    elif plat == 'Linux':
        print("Your system is {0}!".format(plat))
        if not os.path.exists(pipPathL):
            os.mkdir(pipPathL)
            with open(os.path.join(pipPathL, 'pip.conf'),
                      'w',
                      encoding='utf-8') as p:
                p.write(pipSource)
        elif not os.path.exists(os.path.join(pipPathL, 'pip.conf')):
            with open(os.path.join(pipPathL, 'pip.conf'),
                      'w',
                      encoding='utf-8') as p:
                p.write(pipSource)
        else:
            print("{0} already exists!".format("pip.ini"))

    exeHello('pipy')


def pipInstall():
    """pipInstall.

    自动处理依赖项
    """
    # 配置pip源为清华源
    os.system(
        'pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple'
    )
    return 0
    # 更新pip>=10.0.0
    os.system('pip install pip -U')
    # 第三方库列表
    depList = [
        'numpy',
        'pandas',
        'scipy',
        'sympy',
        'matplotlib',
        'ggplot',
        'plotly',
        'pillow',
        'jupyter',
        'ipython',
        'openpyxl',
        'xlwt',
        'xlrd',
        'pyqt5',
        'wxpython',
        'sklearn',
        'keras',
        'tensorflow',
        'request',
        'tablib',
    ]
    for each in depList:
        os.system('pip install {0}'.format(each))
    exeHello('pipInstall')


if __name__ == '__main__':
    # pkgPath()
    # pipy()
    pipInstall()
    pass
