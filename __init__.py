# -*- coding: utf-8 -*-
# author: Minch Wu
"""init.

添加文件搜索路径
"""

import os
import sys

# python 安装目录
pth = sys.exec_prefix
# 在 python 根目录添加.pth路径文件
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
