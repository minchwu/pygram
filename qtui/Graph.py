# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Graph.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraphUI(object):
    def setupUi(self, GraphUI):
        GraphUI.setObjectName("GraphUI")
        GraphUI.setEnabled(True)
        GraphUI.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(GraphUI)
        self.centralwidget.setObjectName("centralwidget")
        self.GraphView = QtWidgets.QGraphicsView(self.centralwidget)
        self.GraphView.setGeometry(QtCore.QRect(10, 10, 360, 270))
        self.GraphView.setObjectName("GraphView")
        self.Plot = QtWidgets.QPushButton(self.centralwidget)
        self.Plot.setGeometry(QtCore.QRect(25, 300, 50, 30))
        self.Plot.setObjectName("Plot")
        GraphUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GraphUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setGeometry(QtCore.QRect(270, 125, 135, 115))
        self.menuMenu.setObjectName("menuMenu")
        GraphUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GraphUI)
        self.statusbar.setObjectName("statusbar")
        GraphUI.setStatusBar(self.statusbar)
        self.actionFiles = QtWidgets.QAction(GraphUI)
        self.actionFiles.setObjectName("actionFiles")
        self.actionSave = QtWidgets.QAction(GraphUI)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(GraphUI)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionFiles)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(GraphUI)
        QtCore.QMetaObject.connectSlotsByName(GraphUI)

    def retranslateUi(self, GraphUI):
        _translate = QtCore.QCoreApplication.translate
        GraphUI.setWindowTitle(_translate("GraphUI", "MainWindow"))
        self.Plot.setText(_translate("GraphUI", "Plot"))
        self.menuMenu.setTitle(_translate("GraphUI", "Menu"))
        self.actionFiles.setText(_translate("GraphUI", "Files"))
        self.actionSave.setText(_translate("GraphUI", "Save"))
        self.actionExit.setText(_translate("GraphUI", "Exit(X)"))
