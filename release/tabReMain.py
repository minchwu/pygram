# -*- coding: utf-8 -*-
# author: Minch Wu
"""tabReMain.

提供函数调用选项
"""

import os
import pyfunc.docfun.pyreport.tabRe as tabRe

DATAPATH = './Adams/'
SAVEPATH = './VSP_Comp/'

try:
    dataPath = DATAPATH
    savePath = SAVEPATH
    enKey = input("{}({}: \"{}\", {}:\"{}\") {} {}\n".format(
        "default set is okay ?", "dataPath", DATAPATH, "savePath", SAVEPATH,
        "Yse[y]", "No, I want to set myself[n]"))
    if enKey == 'y':
        dataPath = DATAPATH
        savePath = SAVEPATH
    elif enKey == 'n':
        dataPath = input("input your dataPath: ")
        savePath = input("input your savePath: ")
    else:
        pass
except:
    os._exit(1)

while True:
    opKey = input("{}({} {} {} {})\n".format("what do you want to do ?",
                                             "precheck[p]?", "clear[c]?",
                                             "write[w]?", "exit[q]!"))
    try:
        if opKey == 'p':
            tabRe.preCheck()
            print("preCheck is Okay!")
        elif opKey == 'c':
            tabRe.tabFileClean()
            print("tabFileClean is Okay!")
        elif opKey == 'w':
            tabRe.tabFileReadList()
            print("tabFileRead is Okay!")
        elif opKey == 'q':
            print("thanks for your use!")
            break
        else:
            print("please check your input!")
    except:
        print('please check your dir or file!')
