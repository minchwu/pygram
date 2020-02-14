# -*- coding: utf-8 -*-
# author: Minch Wu
"""dirsh.

批量文件操作
"""

import os
import shutil
import func.remath.gener as gener


def pathCheck(path: str):
    """pathCheck.

    文件路径检查，如果不存在则报错退出
    """
    if not os.path.exists(path):
        print("Please check your file path!")
        exit(0)


def exeHello(funName: str):
    """exeHello.

    程序结束运行报告
    """
    print("This is <{0}>, everything is done!".format(funName))


def chDir(filePath: str = './', copyPath: str = './copy', exName: str = 'ALL'):
    """chDir.

    批量提取复制文件
    传入文件夹路径，默认为当前文件夹
    """
    # 检查 filePath 文件夹是否存在，否则报错退出
    pathCheck(filePath)
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
    exeHello('chDir')


def fiRna(exName: str,
          filePath: str = './',
          copyPath: str = './copy',
          pattern: str = "0:0>4",
          boolCopy: bool = True):
    """fiRna.

    批量重命名
    传入扩展名，文件路径及复制路径
    """
    # 检查 filePath 文件夹是否存在，否则报错退出
    pathCheck(filePath)
    # 提取文件夹下所有文件
    fileList = os.listdir(filePath)

    # 命名模式，整数生成
    count = gener.num(initN=1, p=1)

    # 检查 目标文件夹是否存在，否则新建
    if not os.path.exists(copyPath):
        os.mkdir(copyPath)

    # 复制选项分支
    # 如果不复制，则为移动
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
    # 否则为复制，保留原文件
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
    exeHello('fiRna')


def recurFile(rootPath: str = './',
              copyPath: str = './copy',
              exName: str = 'ALL',
              boolCover: bool = True):
    """recurFile.

    基于os.walk递归提取文件或重命名
    """
    # 检查 filePath 文件夹是否存在，否则报错退出
    pathCheck(rootPath)

    # 子函数定义
    def copyBase(srcPath: str, dstPath: str, fileName: str):
        shutil.copy(os.path.join(srcPath, fileName),
                    os.path.join(dstPath, fileName))

    def strCover(fileName: str):
        return (input(
            "file({0}) already exists, cover?[y/n/q]:".format(fileName)))

    def copyExAsk():
        """copyExAsk.

        扩展名复制，询问是否覆盖文件
        """
        for root, _, files in os.walk(rootPath):
            for each in files:
                # 判断文件扩展名
                if os.path.splitext(each)[1] == exName:
                    # 判断文件是否已经存在
                    if os.path.exists((os.path.join(copyPath, each))):
                        # 询问是否覆盖文件
                        cover = strCover(each)
                        if cover == 'y':
                            copyBase(root, copyPath, each)
                        # 不覆盖则跳过此文件
                        elif cover == 'n':
                            continue
                        # 提供终止选项
                        elif cover == 'q':
                            exit(0)
                        # 禁止非法输入
                        else:
                            print("please check your input!")
                    else:
                        copyBase(root, copyPath, each)

    def copyNxAsk():
        """copyNxAsk.

        全部复制，询问是否覆盖文件
        """
        for root, _, files in os.walk(rootPath):
            for each in files:
                # 判断文件是否存在
                if os.path.exists(os.path.join(copyPath, each)):
                    # 询问是否覆盖文件
                    cover = strCover(each)
                    if cover == 'y':
                        copyBase(root, copyPath, each)
                    # 不覆盖则跳过此文件
                    elif cover == 'n':
                        continue
                    # 提供终止选项
                    elif cover == 'q':
                        exit(0)
                    # 禁止非法输入
                    else:
                        print("please check your input!")
                else:
                    copyBase(root, copyPath, each)

    def copyExCover():
        """copyExCover.

        扩展名复制，覆盖已有文件
        """
        for root, _, files in os.walk(rootPath):
            for each in files:
                if os.path.splitext(each)[1] == exName:
                    copyBase(root, copyPath, each)

    def copyNxCover():
        """copyNxCover.

        全部复制，覆盖已有文件
        """
        for root, _, files in os.walk(rootPath):
            for each in files:
                copyBase(root, copyPath, each)

    # 检查 copy 文件夹是否存在，否则新建
    if not os.path.exists(copyPath):
        os.mkdir(copyPath)
    # 情况划分
    if exName == 'ALL':
        if boolCover:
            copyNxCover()
            exeHello('recurFile.copyNxCover')
        else:
            copyNxAsk()
            exeHello('recurFile.copyNxAsk')
    else:
        if boolCover:
            copyExCover()
            exeHello('recurFile.copyExCover')
        else:
            copyExAsk()
            exeHello('recurFile.copyExAsk')


if __name__ == '__main__':
    # print("{0:0>4}".format(100))
    # print("{{{0}}}".format("0:0>4").format(1))
    # print(type(True))
    recurFile(rootPath='./demo_test/test_pyshell',
              exName='.xlsx')
