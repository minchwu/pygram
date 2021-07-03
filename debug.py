import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from pyfem.pyfem import GeomGrid


x = np.arange(10)
y = np.sin(x)
g1 = GeomGrid(0, x, y)
# g1.msgOutIDNode()
# g1.gridConnectLine(0)


point = (0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)
conLine = ((1, 0, 1), (2, 1, 2), (3, 2, 3), (4, 3, 0),
           (5, 0, 4), (6, 1, 4), (7, 2, 4), (8, 3, 4))
g2 = GeomGrid(1, *point)
# g2.msgOutIDNode()
# g2.gridConnectLine(0, *conLine)


g3 = GeomGrid(2, './inputNode.csv')
g3.msgOutIDNode()
g3.gridConnectLine(0)
