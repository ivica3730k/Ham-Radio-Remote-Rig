# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 299)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(100, 10, 100, 40))
        self.startButton.setObjectName("startButton")
        self.nodeSelect = QtWidgets.QComboBox(self.centralwidget)
        self.nodeSelect.setGeometry(QtCore.QRect(10, 10, 80, 40))
        self.nodeSelect.setObjectName("nodeSelect")
        self.nodeSelect.addItem("")
        self.nodeSelect.addItem("")
        self.node1_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.node1_ip.setGeometry(QtCore.QRect(10, 60, 191, 31))
        self.node1_ip.setObjectName("node1_ip")
        self.node1_port = QtWidgets.QTextEdit(self.centralwidget)
        self.node1_port.setGeometry(QtCore.QRect(10, 100, 191, 31))
        self.node1_port.setObjectName("node1_port")
        self.node2_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.node2_ip.setGeometry(QtCore.QRect(10, 140, 191, 31))
        self.node2_ip.setObjectName("node2_ip")
        self.node2_port = QtWidgets.QTextEdit(self.centralwidget)
        self.node2_port.setGeometry(QtCore.QRect(10, 180, 191, 31))
        self.node2_port.setObjectName("node2_port")
        self.autostart = QtWidgets.QCheckBox(self.centralwidget)
        self.autostart.setGeometry(QtCore.QRect(210, 10, 92, 23))
        self.autostart.setObjectName("autostart")
        self.node1_ip_label = QtWidgets.QLabel(self.centralwidget)
        self.node1_ip_label.setGeometry(QtCore.QRect(210, 70, 67, 17))
        self.node1_ip_label.setObjectName("node1_ip_label")
        self.node2_ip_label = QtWidgets.QLabel(self.centralwidget)
        self.node2_ip_label.setGeometry(QtCore.QRect(210, 150, 67, 17))
        self.node2_ip_label.setObjectName("node2_ip_label")
        self.node1_port_label = QtWidgets.QLabel(self.centralwidget)
        self.node1_port_label.setGeometry(QtCore.QRect(210, 110, 91, 17))
        self.node1_port_label.setObjectName("node1_port_label")
        self.node2_port_label = QtWidgets.QLabel(self.centralwidget)
        self.node2_port_label.setGeometry(QtCore.QRect(210, 190, 91, 17))
        self.node2_port_label.setObjectName("node2_port_label")
        self.squelch = QtWidgets.QCheckBox(self.centralwidget)
        self.squelch.setGeometry(QtCore.QRect(210, 30, 92, 23))
        self.squelch.setObjectName("squelch")
        self.saveConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveConfigButton.setGeometry(QtCore.QRect(10, 220, 281, 40))
        self.saveConfigButton.setObjectName("saveConfigButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start Audio"))
        self.nodeSelect.setItemText(0, _translate("MainWindow", "Node 1"))
        self.nodeSelect.setItemText(1, _translate("MainWindow", "Node 2"))
        self.autostart.setText(_translate("MainWindow", "Autostart"))
        self.node1_ip_label.setText(_translate("MainWindow", "Node 1 IP"))
        self.node2_ip_label.setText(_translate("MainWindow", "Node 2 IP"))
        self.node1_port_label.setText(_translate("MainWindow", "Node 1 Port"))
        self.node2_port_label.setText(_translate("MainWindow", "Node 2 Port"))
        self.squelch.setText(_translate("MainWindow", "Squelch"))
        self.saveConfigButton.setText(_translate("MainWindow", "Save Config For Next Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
