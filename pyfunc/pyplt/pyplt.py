# -*- coding: utf-8 -*-
# author: Minch Wu
"""pyplt.

绘图函数接口
"""

import numpy as np
import matplotlib.pyplot as plt

def replot():
    x = np.arange(0, np.pi, 0.1 * np.pi)
    y = np.sin(x)
    plt.plot(x,y)
    plt.show()
