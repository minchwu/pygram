# -*- coding: utf-8 -*-
# author: Mingchun Wu
"""pyfem.

FEM 0->1
1) Node-Grid to Struct-Mesh
2) Cal-Method
"""
import numpy as np
import matplotlib.pyplot as plt


def slash(RS='-', N=70):
    """slash."""
    print(RS * N)


class GeomGrid:
    """GeomGrid.

    Generate plane grid
    """

    geomCount = 0
    dictNode = {}
    dictCoord = {}

    def __init__(self, x, y):
        if not (x, y) in GeomGrid.dictCoord.keys():
            self.geomID = GeomGrid.geomCount
            self.coord = (x, y)
            GeomGrid.dictCoord[(x, y)] = self.geomID
            GeomGrid.dictNode[self.geomID] = (x, y)
            GeomGrid.geomCount += 1
        else:
            slash()
            print(
                "One node coords must be only, your geomgrid will not be updated!"
            )
            slash()
            self.geomID = GeomGrid.dictCoord[(x, y)]
            self.coord = (x, y)

    def grid(self):
        """grid."""
        pass

    def msgOutInstance(self):
        """msgOutInstance."""
        slash()
        print("geomID\tNode\n{0:>6}\t{1}".format(self.geomID, self.coord))
        slash()

    def msgOutClass():
        """msgOutClass."""
        slash()
        print("GeomCount\t%6d\nGeomID\tNodeCoord" % GeomGrid.geomCount)
        for key in range(GeomGrid.geomCount):
            print("{0:>6}\t{1}".format(key, GeomGrid.dictNode[key]))
        slash()


if __name__ == '__main__':
    g1 = GeomGrid(0, 0)
    g2 = GeomGrid(1, 1)
    g1.msgOutInstance()
    g2.msgOutInstance()