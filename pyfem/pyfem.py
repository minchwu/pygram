# -*- coding: utf-8 -*-
# author: Mingchun Wu
"""pyfem.

FEM 0->1
1) Node-Grid to Struct-Mesh
2) Cal-Method
"""
from os import read
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from numpy.core.numeric import convolve


DIM_PLANE = 2


def slash(Notes: str = "", RS='-', N=70):
    """slash."""
    print('\n'+RS * N)
    print(Notes)
    print(RS * N)


class GeomGrid:
    """GeomGrid.

    Generate plane grid
    """

    def __init__(self, PoIN=0, *Coord):
        self.nodeID = []
        self.dictIDNode = {}
        self.dictNodeID = {}

        if PoIN == 0:
            # if 0, Coord are provided in x/y List
            if len(Coord) == DIM_PLANE:
                if len(Coord[0]) == len(Coord[1]):
                    self.CoordX = Coord[0]
                    self.CoordY = Coord[1]
                    for each in zip(self.CoordX, self.CoordY):
                        if not each in self.dictNodeID.keys():
                            self.nodeID.append(0)
                            self.dictNodeID[each] = self.nodeID[-1]
                            self.dictIDNode[self.nodeID[-1]] = each
                            self.nodeID.append(self.nodeID[-1]+1)
                        else:
                            slash(
                                "One node coord must be only, your geomgrid will not be updated!")
                    pass
                else:
                    slash("The coord of points must be couple!")
            else:
                slash("The analysis is for 2D plane!")
        elif PoIN == 1:
            # if 1, Coord are provided in point one by one
            self.CoordX = []
            self.CoordY = []
            [self.CoordX.append(each[0]) for each in Coord]
            [self.CoordY.append(each[1]) for each in Coord]
            for each in zip(self.CoordX, self.CoordY):
                if not each in self.dictNodeID.keys():
                    self.dictNodeID[each] = self.nodeID
                    self.dictIDNode[self.nodeID[-1]] = each
                    self.nodeID.append(self.nodeID[-1]+1)
                else:
                    slash(
                        "One node coord must be only, your geomgrid will not be updated!")
        elif PoIN == 2:
            with open(Coord[0], 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                try:
                    self.CoordX = []
                    self.CoordY = []
                    while True:
                        temp = next(reader)
                        tmp = [[]+int(each) for each in temp]
                        self.nodeID.append(tmp[0])
                        self.CoordX.append(tmp[1])
                        self.CoordY.append(tmp[2])
                        self.dictNodeID[tuple(tmp[1:])] = tmp[0]
                        self.dictIDNode[tmp[0]] = tuple(tmp[1:])
                        print(temp)
                        print(tmp)
                except:
                    pass

    def gridScatter(self):
        """gridScatter."""
        plt.figure('GeomGrid-Scatter')
        plt.scatter(self.CoordX, self.CoordY, s=100, c='r')
        plt.show()
        pass

    def gridConnectLine(self, CN=1, *ConLine):
        """gridConnectLine."""
        if CN == 0:
            # if 0, continus
            plt.figure('GeomGrid-ConnectLine')
            plt.scatter(self.CoordX, self.CoordY, s=100, c='r')
            plt.plot(self.CoordX, self.CoordY, linewidth=3, color='k')
            plt.show()
        elif CN == 1:
            # if 1, tuple statement
            plt.figure('GeomGrid-ConnectLine')
            plt.scatter(self.CoordX, self.CoordY, s=100, c='r')
            self.dictIDLine = {}
            for each in ConLine:
                LN = each[0]
                p1 = each[1]
                p2 = each[2]
                if p1 <= self.nodeID and p2 <= self.nodeID:
                    self.dictIDLine[LN] = plt.plot((self.dictIDNode[p1][0],
                                                    self.dictIDNode[p2][0]),
                                                   (self.dictIDNode[p1][1],
                                                    self.dictIDNode[p2][1]),
                                                   linewidth=3, color='k')
            plt.show()
        elif CN == 2:
            with open(ConLine[0], 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                try:
                    self.CoordX = []
                    self.CoordY = []
                    while True:
                        tmp = [[]+int(each) for each in next(reader)]
                        self.dictNodeID[tuple(tmp[1:])] = tmp[0]
                        self.dictIDNode[tmp[0]] = tuple(tmp[1:])
                except:
                    pass
            plt.figure('GeomGrid-ConnectLine')
            plt.scatter(self.CoordX, self.CoordY, s=100, c='r')
            self.dictIDLine = {}
            for each in ConLine:
                LN = each[0]
                p1 = each[1]
                p2 = each[2]
                if p1 <= self.nodeID and p2 <= self.nodeID:
                    self.dictIDLine[LN] = plt.plot((self.dictIDNode[p1][0],
                                                    self.dictIDNode[p2][0]),
                                                   (self.dictIDNode[p1][1],
                                                    self.dictIDNode[p2][1]),
                                                   linewidth=3, color='k')
            plt.show()

        else:
            pass

    def msgOutIDNode(self):
        """msgOutIDNode."""
        slash("NodeID\tNodeCoord")
        for key in self.nodeID:
            print("{0:>6}\t{1}".format(key, self.dictIDNode[key]))


if __name__ == '__main__':
    pass
