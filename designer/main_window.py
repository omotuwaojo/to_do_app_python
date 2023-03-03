# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 701, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.main_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.main_label.setFont(font)
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.verticalLayout_3.addWidget(self.main_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.new_task = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.new_task.setFont(font)
        self.new_task.setObjectName("new_task")
        self.horizontalLayout_3.addWidget(self.new_task)
        self.newTaskbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.newTaskbutton.setObjectName("newTaskbutton")
        self.horizontalLayout_3.addWidget(self.newTaskbutton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.finished_task = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.finished_task.setFont(font)
        self.finished_task.setObjectName("finished_task")
        self.verticalLayout.addWidget(self.finished_task)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.finished_list = QtWidgets.QListWidget(self.layoutWidget)
        self.finished_list.setObjectName("finished_list")
        self.horizontalLayout.addWidget(self.finished_list)
        self.UndoneBotton = QtWidgets.QPushButton(self.layoutWidget)
        self.UndoneBotton.setObjectName("UndoneBotton")
        self.horizontalLayout.addWidget(self.UndoneBotton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.remainig_task = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.remainig_task.setFont(font)
        self.remainig_task.setObjectName("remainig_task")
        self.verticalLayout_2.addWidget(self.remainig_task)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.remainig_list = QtWidgets.QListWidget(self.layoutWidget)
        self.remainig_list.setObjectName("remainig_list")
        self.horizontalLayout_2.addWidget(self.remainig_list)
        self.doneButton = QtWidgets.QPushButton(self.layoutWidget)
        self.doneButton.setObjectName("doneButton")
        self.horizontalLayout_2.addWidget(self.doneButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_label.setText(_translate("MainWindow", "My To Do List"))
        self.new_task.setText(_translate("MainWindow", "New Task"))
        self.newTaskbutton.setText(_translate("MainWindow", "New_Task"))
        self.finished_task.setText(_translate("MainWindow", "Finished_Task"))
        self.UndoneBotton.setText(_translate("MainWindow", "Undone"))
        self.remainig_task.setText(_translate("MainWindow", "Remainig_Task"))
        self.doneButton.setText(_translate("MainWindow", "Done"))
