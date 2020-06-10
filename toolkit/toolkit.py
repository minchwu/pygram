# -*- coding: utf-8 -*-
# author: Mingchun Wu
"""toolkit.

工具集
"""

import qtui.Graph as Graph
import sys
# import numpy as np
# import matplotlib.pyplot as plt
from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


appGraph = QApplication(sys.argv)
graph_ui = Graph.Ui_GraphUI()
qMainW = QMainWindow()
graph_ui.setupUi(qMainW)
qMainW.setWindowIcon(QIcon('./icon/favicon.ico'))
qMainW.show()
sys.exit(appGraph.exec_())
