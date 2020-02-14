# -*- coding: utf-8 -*-
# author: Minch Wu
"""notePDF.

针对文献管理软件EndNote，调用recurFile提取PDF文件夹下PDF文件
"""

import sys
import func.docfun.pyshell.dirsh as dirsh

if __name__ == '__main__':

    dirsh.recurFile(*sys.argv[1:])
