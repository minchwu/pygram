# -*- coding: utf-8 -*-
# author: Minch Wu
"""窗体程序.

为程序添加gui界面
"""

import tkinter as tk


class tkw(object):
    """定义程序窗口类.

    实现程序窗口的初始化，提供界面参数修改接口
    """

    __tkw = tk.Tk()

    def __init__(self,
                 title: str = 'TXTEX',
                 width: int = 400,
                 height=300,
                 left=17,
                 up=17):
        """__init__."""
        self.__tkw.title(title)
        self.__tkw.geometry('{}x{}+{}+{}'.format(width, height, left, up))
        self.__tkw.resizable(width=True, height=True)
        self.__tkw.mainloop()
        # tk.Label(self.__tkw,text="TXTEX",bg='blue',font=('Arial 12 bold'),width=20,height=20).pack()
