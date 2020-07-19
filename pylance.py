# coding: utf-8 -*-
# author: Mingchun Wu

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 361)
y = np.exp(np.sin(x))
z = np.sin(np.exp(x))
with plt.style.context(['science', 'no-latex']):
    fig = plt.figure(num=1, figsize=(8, 6), dpi=100)
    fig.suptitle("$x-y-z$")
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.5])
    ax.plot(x, y, linewidth=2, color='r', label='$exp(sinx)$')
    ax.legend(frameon=True, shadow=True, loc=3)
    ax.set_xlabel('x')
    ax.grid(b=True, color='c')
    ax.autoscale(tight=True)
    bx = fig.add_axes([0.1, 0.7, 0.4, 0.2])
    bx.plot(x, z, linewidth=1, color='b', label='$sin(exp(x))$')
    bx.legend(frameon=True, shadow=True, fontsize=7, loc=3)
    cx = fig.add_axes([0.6, 0.7, 0.3, 0.2])
    cx.plot(y, z, linewidth=1, color='k', label='$y-z$')
    cx.legend(frameon=True, shadow=True, fontsize=7, loc=3)
    plt.show(fig)
