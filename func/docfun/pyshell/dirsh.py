# -*- coding: utf-8 -*-
# author: Minch Wu
"""dirsh.

批量文件操作
"""

import os
import shutil
import func.remath.gener as gener


def chDir(filePath: str = './', copyPath: str = './copy', exName: str = 'ALL'):
    """chDir.

    批量提取复制文件
    传入文件夹路径，默认为当前文件夹
    """
    # 提取文件夹下所有文件
    fileList = os.listdir(filePath)

    # 检查 copy 文件夹是否存在，否则新建
    if not os.path.exists(copyPath):
        os.mkdir(copyPath)

    # 文件扩展名判断
    # 默认不指定扩展名
    if exName == 'ALL':
        for eachFile in fileList:
            shutil.copy(os.path.join(filePath, eachFile),
                        os.path.join(copyPath, eachFile))
    else:
        for eachFile in fileList:
            # 复制指定扩展名的文件
            if os.path.splitext(eachFile)[1] == exName:
                shutil.copy(os.path.join(filePath, eachFile),
                            os.path.join(copyPath, eachFile))


def fiRna(exName: str,
          filePath: str = './',
          copyPath: str = './copy',
          pattern: str = "0:0>4",
          boolCopy: bool = True):
    """fiRna.

    批量重命名
    传入扩展名，文件路径及复制路径
    """
    # 命名模式，整数生成
    count = gener.num(initN=1, p=1)

    # 提取文件夹下所有文件
    fileList = os.listdir(filePath)

    # 检查 目标文件夹是否存在，否则新建
    if not os.path.exists(copyPath):
        os.mkdir(copyPath)

    # 复制选项分支
    if not boolCopy:
        for eachFile in fileList:
            # 文件扩展名判断
            if os.path.splitext(eachFile)[1] == exName:
                os.rename(
                    os.path.join(filePath, eachFile),
                    os.path.join(
                        copyPath,
                        "{{{0}}}{1}".format(pattern,
                                            exName).format(next(count))))
    else:
        for eachFile in fileList:
            # 文件扩展名判断
            if os.path.splitext(eachFile)[1] == exName:
                shutil.copy(
                    os.path.join(filePath, eachFile),
                    os.path.join(
                        copyPath,
                        "{{{0}}}{1}".format(pattern,
                                            exName).format(next(count))))


if __name__ == '__main__':
    print("{0:0>4}".format(100))
    print("{{{0}}}".format("0:0>4").format(1))
    print(type(True))
