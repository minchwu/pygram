# -*- coding: utf-8 -*-
# author: Minch Wu
"""RECUR.PY.

define some functions in recursive process
"""


def hanoi(n: int, L=None):
    """hanoi.

    storage the move process
    """
    if L is None:
        L = []

    def move(n, a='A', b='B', c='C'):
        """move.

        move the pagoda
        """
        if n == 1:
            # print(a + '->' + c)
            L.append(a + '->' + c)
            # return (L)
        else:
            move(n - 1, a, c, b)
            # print(a + '->' + c)
            move(1, a, b, c)
            move(n - 1, b, a, c)

    move(n)
    return (L)
