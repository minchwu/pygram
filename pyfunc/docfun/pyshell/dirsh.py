# -*- coding: utf-8 -*-
# author: Minch Wu
"""dirsh.

批量文件操作
"""

import os
import shutil
import pyfunc.remath.gener as gener


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
    os.system("pause")


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
          boolCopy: bool = True,
          boolExist: bool = False):
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

    def _copyRename(item: str):
        """copyRename.

        复制重命名
        """
        shutil.copy(
            os.path.join(filePath, item),
            os.path.join(
                copyPath, "{{{0}}}{1}".format(pattern, exName).format(
                    (next(count)))))

    def _moveRename(item: str):
        """moveRename.

        移动重命名
        """
        os.rename(
            os.path.join(filePath, item),
            os.path.join(
                copyPath, "{{{0}}}{1}".format(pattern,
                                              exName).format(next(count))))

    def _boolFileExistCopy(item: str):
        """boolFileExist.

        判断文件名是否重复，并复制
        """
        tmpName = "{{{0}}}{1}".format(pattern, exName).format(next(count))
        if os.path.exists(os.path.join(copyPath, tmpName)):
            _boolFileExistCopy(item)
        else:
            shutil.copy(os.path.join(filePath, item),
                        os.path.join(copyPath, tmpName))
            pass

    def _boolFileExistMove(item: str):
        """boolFileExistMove.

        判断文件名是否重复，并移动
        """
        tmpName = "{{{0}}}{1}".format(pattern, exName).format(next(count))
        if os.path.exists(os.path.join(copyPath, tmpName)):
            _boolFileExistMove(item)
        else:
            os.rename(os.path.join(filePath, item),
                      os.path.join(copyPath, tmpName))
            pass

    # 复制及重名分支
    # 默认为复制，不考虑文件名已存在问题
    if boolCopy and not boolExist:
        for eachFile in fileList:
            # 文件扩展名判断
            if os.path.splitext(eachFile)[1] == exName:
                _copyRename(eachFile)
    # 复制，考虑文件名已存在
    elif boolCopy and boolExist:
        for eachFile in fileList:
            # 文件扩展名判断
            if os.path.splitext(eachFile)[1] == exName:
                _boolFileExistCopy(eachFile)  # 校验文件名是否已存在，重名则跳过该文件名
    # 移动，不考虑文件名
    elif not boolCopy and not boolExist:
        for eachFile in fileList:
            # 文件扩展名判断
            if os.path.splitext(eachFile)[1] == exName:
                _moveRename(eachFile)
    # 移动，考虑文件名
    elif not boolCopy and boolExist:
        for eachFile in fileList:
            if os.path.splitext(eachFile)[1] == exName:
                _boolFileExistMove(eachFile)  # 校验文件名是否已存在，重名则跳过该文件名

    exeHello('fiRna')


def fiRnaCall(exName: list = [],
              filePath: str = './',
              copyPath: str = './copy',
              pattern: str = "0:0>4",
              boolCopy: bool = True,
              boolExist: bool = True):
    """fiRnaCall.

    对fiRna进行二次封装，提供多扩展名接口
    """
    if len(exName) > 0:
        for eachItem in exName:
            fiRna(eachItem, filePath, copyPath, pattern, boolCopy, boolExist)
    else:
        exSet = set(
            [os.path.splitext(item)[1] for item in os.listdir(filePath)])
        print(exSet)
        for eachItem in exSet:
            fiRna(eachItem, filePath, copyPath, pattern, boolCopy, boolExist)

    exeHello('fiRnaCall')


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
    def _copyBase(srcPath: str, dstPath: str, fileName: str):
        shutil.copy(os.path.join(srcPath, fileName),
                    os.path.join(dstPath, fileName))

    def _strCover(fileName: str):
        return (input(
            "file({0}) already exists, cover?[y/n/q]:".format(fileName)))

    def _copyExAsk():
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
                        cover = _strCover(each)
                        if cover == 'y':
                            _copyBase(root, copyPath, each)
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
                        _copyBase(root, copyPath, each)

    def _copyNxAsk():
        """copyNxAsk.

        全部复制，询问是否覆盖文件
        """
        for root, _, files in os.walk(rootPath):
            for each in files:
                # 判断文件是否存在
                if os.path.exists(os.path.join(copyPath, each)):
                    # 询问是否覆盖文件
                    cover = _strCover(each)
                    if cover == 'y':
                        _copyBase(root, copyPath, each)
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
                    _copyBase(root, copyPath, each)

    def _copyExCover():
        """copyExCover.

        扩展名复制，覆盖已有文件
        """
        for root, _, files in os.walk(rootPath):
            for each in files:
                if os.path.splitext(each)[1] == exName:
                    _copyBase(root, copyPath, each)

    def _copyNxCover():
        """copyNxCover.

        全部复制，覆盖已有文件
        """
        for root, _, files in os.walk(rootPath):
            for each in files:
                _copyBase(root, copyPath, each)

    # 检查 copy 文件夹是否存在，否则新建
    if not os.path.exists(copyPath):
        os.mkdir(copyPath)
    # 情况划分
    if exName == 'ALL':
        if boolCover:
            _copyNxCover()
            exeHello('recurFile.copyNxCover')
        else:
            _copyNxAsk()
            exeHello('recurFile.copyNxAsk')
    else:
        if boolCover:
            _copyExCover()
            exeHello('recurFile.copyExCover')
        else:
            _copyExAsk()
            exeHello('recurFile.copyExAsk')


if __name__ == '__main__':
    # print("{0:0>4}".format(100))
    # print("{{{0}}}".format("0:0>4").format(1))
    # print(type(True))
    recurFile(rootPath='./demo_test/test_pyshell',
              copyPath='./demo/copy',
              exName='.xlsx')
    # exeHello(chDir.__name__)
    # print(chDir.__name__)
