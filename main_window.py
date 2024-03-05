# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GradPress_MainWindow(object):
    def setupUi(self, GradPress_MainWindow):
        GradPress_MainWindow.setObjectName("GradPress_MainWindow")
        GradPress_MainWindow.resize(886, 629)
        self.centralwidget = QtWidgets.QWidget(GradPress_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(-10, 0, 231, 551))
        self.treeView.setObjectName("treeView")
        GradPress_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GradPress_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_file = QtWidgets.QMenu(self.menuFile)
        self.menuExport_file.setObjectName("menuExport_file")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        GradPress_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GradPress_MainWindow)
        self.statusbar.setObjectName("statusbar")
        GradPress_MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(GradPress_MainWindow)
        self.toolBar.setObjectName("toolBar")
        GradPress_MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Project = QtWidgets.QAction(GradPress_MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionSave_Project = QtWidgets.QAction(GradPress_MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionImport_file = QtWidgets.QAction(GradPress_MainWindow)
        self.actionImport_file.setObjectName("actionImport_file")
        self.actionExport_as_csv = QtWidgets.QAction(GradPress_MainWindow)
        self.actionExport_as_csv.setObjectName("actionExport_as_csv")
        self.actionExport_as_txt = QtWidgets.QAction(GradPress_MainWindow)
        self.actionExport_as_txt.setObjectName("actionExport_as_txt")
        self.actionLoad_file = QtWidgets.QAction(GradPress_MainWindow)
        self.actionLoad_file.setObjectName("actionLoad_file")
        self.actionOpen_PandaGUI = QtWidgets.QAction(GradPress_MainWindow)
        self.actionOpen_PandaGUI.setObjectName("actionOpen_PandaGUI")
        self.actionPreferences = QtWidgets.QAction(GradPress_MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout_GradPress = QtWidgets.QAction(GradPress_MainWindow)
        self.actionAbout_GradPress.setObjectName("actionAbout_GradPress")
        self.actionManage_Files = QtWidgets.QAction(GradPress_MainWindow)
        self.actionManage_Files.setObjectName("actionManage_Files")
        self.actionUndo = QtWidgets.QAction(GradPress_MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(GradPress_MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtWidgets.QAction(GradPress_MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(GradPress_MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtWidgets.QAction(GradPress_MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionNew_file_icon = QtWidgets.QAction(GradPress_MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/add_FILL1_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_file_icon.setIcon(icon)
        self.actionNew_file_icon.setObjectName("actionNew_file_icon")
        self.actionOpenFolder = QtWidgets.QAction(GradPress_MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/folder_open_FILL1_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenFolder.setIcon(icon1)
        self.actionOpenFolder.setObjectName("actionOpenFolder")
        self.actionSaveFile = QtWidgets.QAction(GradPress_MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/save_FILL1_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveFile.setIcon(icon2)
        self.actionSaveFile.setObjectName("actionSaveFile")
        self.menuExport_file.addAction(self.actionExport_as_csv)
        self.menuExport_file.addAction(self.actionExport_as_txt)
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionLoad_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_file)
        self.menuFile.addAction(self.menuExport_file.menuAction())
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionOpen_PandaGUI)
        self.menuEdit.addAction(self.actionManage_Files)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout_GradPress)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew_file_icon)
        self.toolBar.addAction(self.actionOpenFolder)
        self.toolBar.addAction(self.actionSaveFile)
        self.toolBar.addSeparator()

        self.retranslateUi(GradPress_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(GradPress_MainWindow)

    def retranslateUi(self, GradPress_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        GradPress_MainWindow.setWindowTitle(_translate("GradPress_MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("GradPress_MainWindow", "File"))
        self.menuExport_file.setStatusTip(_translate("GradPress_MainWindow", "Exports the current file/project"))
        self.menuExport_file.setTitle(_translate("GradPress_MainWindow", "Export file"))
        self.menuEdit.setTitle(_translate("GradPress_MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("GradPress_MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("GradPress_MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("GradPress_MainWindow", "toolBar"))
        self.actionNew_Project.setText(_translate("GradPress_MainWindow", "New Project"))
        self.actionNew_Project.setStatusTip(_translate("GradPress_MainWindow", "Starts a new project"))
        self.actionNew_Project.setShortcut(_translate("GradPress_MainWindow", "Ctrl+N"))
        self.actionSave_Project.setText(_translate("GradPress_MainWindow", "Save Project"))
        self.actionSave_Project.setStatusTip(_translate("GradPress_MainWindow", "Saves a project"))
        self.actionSave_Project.setShortcut(_translate("GradPress_MainWindow", "Ctrl+S"))
        self.actionImport_file.setText(_translate("GradPress_MainWindow", "Import file"))
        self.actionImport_file.setStatusTip(_translate("GradPress_MainWindow", "Import a .csv or .txt file"))
        self.actionExport_as_csv.setText(_translate("GradPress_MainWindow", "Export as csv"))
        self.actionExport_as_csv.setStatusTip(_translate("GradPress_MainWindow", "Export the current file as a comma separated values file type (.csv)"))
        self.actionExport_as_txt.setText(_translate("GradPress_MainWindow", "Export as txt"))
        self.actionExport_as_txt.setStatusTip(_translate("GradPress_MainWindow", "Export the current file as a text file (.txt)"))
        self.actionLoad_file.setText(_translate("GradPress_MainWindow", "Load file"))
        self.actionOpen_PandaGUI.setText(_translate("GradPress_MainWindow", "Open PandaGUI"))
        self.actionOpen_PandaGUI.setStatusTip(_translate("GradPress_MainWindow", "Opens pandagui for manipulation of data"))
        self.actionPreferences.setText(_translate("GradPress_MainWindow", "Preferences"))
        self.actionAbout_GradPress.setText(_translate("GradPress_MainWindow", "About GradPress"))
        self.actionManage_Files.setText(_translate("GradPress_MainWindow", "Manage Files"))
        self.actionUndo.setText(_translate("GradPress_MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("GradPress_MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("GradPress_MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("GradPress_MainWindow", "Ctrl+Shift+Z"))
        self.actionCopy.setText(_translate("GradPress_MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("GradPress_MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("GradPress_MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("GradPress_MainWindow", "Ctrl+V"))
        self.actionCut.setText(_translate("GradPress_MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("GradPress_MainWindow", "Ctrl+X"))
        self.actionNew_file_icon.setText(_translate("GradPress_MainWindow", "New file"))
        self.actionNew_file_icon.setShortcut(_translate("GradPress_MainWindow", "Ctrl+N"))
        self.actionOpenFolder.setText(_translate("GradPress_MainWindow", "Open"))
        self.actionSaveFile.setText(_translate("GradPress_MainWindow", "Save"))

