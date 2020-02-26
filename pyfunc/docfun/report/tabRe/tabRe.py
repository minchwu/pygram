# -*- coding: utf-8 -*-
# author: Minch Wu
"""tabRead.

提供数据前处理
"""

import os
import openpyxl


def preCheck(path: str):
    """preCheck."""
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("dir is okay!")


def tabFileClean(path: str):
    """tabFileClean."""
    fileList = os.listdir(path)
    for each in fileList:
        tmp = os.path.splitext(each)
        if tmp[1] == '.tab':
            os.remove(path + each)


def tabFileReadList(savepath: str, path: str):
    """tabFileReadList."""
    fileList = os.listdir(path)
    tmpList = []
    for each in fileList:
        if os.path.splitext(each)[1] == '.tab':
            tmpList.append(each)

    wb = openpyxl.Workbook()
    # ws = wb.create_sheet(tmpList[0], 0)
    with open(path + tmpList[0], 'r') as tmpData:
        data = tmpData.read()
        print(data)
    wb.save(savepath + 'vsp_comp.xlsx')
    wb.close()
