# Form implementation generated from reading ui file 'src/Interface/crud.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ManageFilesWindow(object):
    def setupUi(self, ManageFilesWindow):
        ManageFilesWindow.setObjectName("ManageFilesWindow")
        ManageFilesWindow.resize(650, 500)
        ManageFilesWindow.setMinimumSize(QtCore.QSize(650, 500))
        ManageFilesWindow.setMaximumSize(QtCore.QSize(650, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("src/Interface/../icon.ico"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        ManageFilesWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=ManageFilesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 10, 651, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.manageFilesLabel = QtWidgets.QLabel(parent=self.frame)
        self.manageFilesLabel.setGeometry(QtCore.QRect(0, 10, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.manageFilesLabel.setFont(font)
        self.manageFilesLabel.setObjectName("manageFilesLabel")
        self.manageFilesLabel_2 = QtWidgets.QLabel(parent=self.frame)
        self.manageFilesLabel_2.setGeometry(QtCore.QRect(0, 50, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.manageFilesLabel_2.setFont(font)
        self.manageFilesLabel_2.setObjectName("manageFilesLabel_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(70, 110, 521, 301))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.manageFilesTreeView = QtWidgets.QTreeView(parent=self.frame_2)
        self.manageFilesTreeView.setGeometry(QtCore.QRect(0, 0, 521, 301))
        self.manageFilesTreeView.setObjectName("manageFilesTreeView")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(70, 430, 521, 41))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.splitter = QtWidgets.QSplitter(parent=self.frame_3)
        self.splitter.setGeometry(QtCore.QRect(0, 10, 521, 21))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.addFileBtn = QtWidgets.QPushButton(parent=self.splitter)
        self.addFileBtn.setObjectName("addFileBtn")
        self.renameFileBtn = QtWidgets.QPushButton(parent=self.splitter)
        self.renameFileBtn.setObjectName("renameFileBtn")
        self.deleteFileBtn = QtWidgets.QPushButton(parent=self.splitter)
        self.deleteFileBtn.setObjectName("deleteFileBtn")
        self.exitManageFilesBtn = QtWidgets.QPushButton(parent=self.splitter)
        self.exitManageFilesBtn.setObjectName("exitManageFilesBtn")
        ManageFilesWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=ManageFilesWindow)
        self.statusbar.setObjectName("statusbar")
        ManageFilesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ManageFilesWindow)
        QtCore.QMetaObject.connectSlotsByName(ManageFilesWindow)

    def retranslateUi(self, ManageFilesWindow):
        _translate = QtCore.QCoreApplication.translate
        ManageFilesWindow.setWindowTitle(_translate("ManageFilesWindow", "MainWindow"))
        self.manageFilesLabel.setText(
            _translate(
                "ManageFilesWindow",
                '<html><head/><body><p align="center"><span style="font-weight:600;">Manage Files</span></p></body></html>',
            )
        )
        self.manageFilesLabel_2.setText(
            _translate(
                "ManageFilesWindow",
                '<html><head/><body><p align="center"><span style="font-size:14pt;">Manage the loaded files here</span></p></body></html>',
            )
        )
        self.addFileBtn.setText(_translate("ManageFilesWindow", "Add"))
        self.renameFileBtn.setText(_translate("ManageFilesWindow", "Rename"))
        self.deleteFileBtn.setText(_translate("ManageFilesWindow", "Delete"))
        self.exitManageFilesBtn.setText(_translate("ManageFilesWindow", "Back"))
