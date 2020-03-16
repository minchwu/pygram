# -*- coding: utf-8 -*-
# author: Minch Wu
"""pypic.

图片处理库PIL，二次接口开发
"""
# TODO: 加强截取功能（增加矩形框比例参数）

import os
from pyfunc.docfun.pyshell.dirsh import pathCheck
from pyfunc.docfun.pyshell.dirsh import exeHello
from PIL import Image


def piCrop(filePath: str = './',
           copyPath: str = './copy',
           box: tuple = (0, 0, 1, 1)):
    """piCrop.

    批量修剪图片
    """
    pathCheck(filePath)

    # 检查复制文件夹是否存在，否则新建
    if not os.path.exists(copyPath):
        os.mkdir(copyPath)
    for each in os.listdir(filePath):
        im = Image.open(os.path.join(filePath, each), "r")
        region = im.crop(box)
        region.save(os.path.join(copyPath, each))

    exeHello("piCrop")


# 图片截取框大小试取
if __name__ == "__main__":
    # zoom 讲义
    # im = Image.open("./001.png", "r")
    # print(im.size)
    # w = 0
    # h = 70
    # box = (w, h, 1600, 985)
    # region = im.crop(box)
    # region.show()
    # region.save("./0002.png")

    # 矩阵分析作业拍照
    im = Image.open("./1001.jpg", "r")
    print(im.size)
    box = (0, 300, 4000, 2000)
    region = im.crop(box)
    region.show()
