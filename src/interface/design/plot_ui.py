# Form implementation generated from reading ui file 'c:\Users\Icarl\Documents\GitHub\Kraken\src\interface\design\plot.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SimplePlotWindow(object):
    def setupUi(self, SimplePlotWindow):
        SimplePlotWindow.setObjectName("SimplePlotWindow")
        SimplePlotWindow.resize(670, 634)
        SimplePlotWindow.setMinimumSize(QtCore.QSize(670, 530))
        SimplePlotWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Icarl\\Documents\\GitHub\\Kraken\\src\\interface\\design\\../../../../Documents/GitHub/Kraken/src/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        SimplePlotWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=SimplePlotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.titleFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.titleFrame.setMaximumSize(QtCore.QSize(16777215, 90))
        self.titleFrame.setAutoFillBackground(False)
        self.titleFrame.setStyleSheet("")
        self.titleFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.titleFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(parent=self.titleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.gridLayout.addWidget(self.titleFrame, 0, 0, 1, 2)
        self.selectFileGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.selectFileGroupBox.setMaximumSize(QtCore.QSize(16777215, 152))
        self.selectFileGroupBox.setFlat(False)
        self.selectFileGroupBox.setCheckable(False)
        self.selectFileGroupBox.setObjectName("selectFileGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.selectFileGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.selectFileGroupBox)
        self.label_2.setMouseTracking(True)
        self.label_2.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.xlsxRadioButton = QtWidgets.QRadioButton(parent=self.selectFileGroupBox)
        self.xlsxRadioButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xlsxRadioButton.setFont(font)
        self.xlsxRadioButton.setObjectName("xlsxRadioButton")
        self.fileButtonGroup = QtWidgets.QButtonGroup(SimplePlotWindow)
        self.fileButtonGroup.setObjectName("fileButtonGroup")
        self.fileButtonGroup.addButton(self.xlsxRadioButton)
        self.gridLayout_2.addWidget(self.xlsxRadioButton, 1, 3, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(parent=self.selectFileGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.selectFileComboBox = QtWidgets.QComboBox(parent=self.selectFileGroupBox)
        self.selectFileComboBox.setObjectName("selectFileComboBox")
        self.gridLayout_2.addWidget(self.selectFileComboBox, 0, 1, 1, 3)
        self.txtRadioButton = QtWidgets.QRadioButton(parent=self.selectFileGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtRadioButton.setFont(font)
        self.txtRadioButton.setObjectName("txtRadioButton")
        self.fileButtonGroup.addButton(self.txtRadioButton)
        self.gridLayout_2.addWidget(self.txtRadioButton, 1, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.csvRadioButton = QtWidgets.QRadioButton(parent=self.selectFileGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.csvRadioButton.setFont(font)
        self.csvRadioButton.setObjectName("csvRadioButton")
        self.fileButtonGroup.addButton(self.csvRadioButton)
        self.gridLayout_2.addWidget(self.csvRadioButton, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addWidget(self.selectFileGroupBox, 2, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=self.groupBox_5)
        self.groupBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.inputProfMin = QtWidgets.QLineEdit(parent=self.groupBox)
        self.inputProfMin.setObjectName("inputProfMin")
        self.gridLayout_4.addWidget(self.inputProfMin, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.inputProfMax = QtWidgets.QLineEdit(parent=self.groupBox)
        self.inputProfMax.setObjectName("inputProfMax")
        self.gridLayout_4.addWidget(self.inputProfMax, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.groupBox_5)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)
        self.inputPlotYAxis = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.inputPlotYAxis.setObjectName("inputPlotYAxis")
        self.gridLayout_5.addWidget(self.inputPlotYAxis, 2, 1, 1, 4)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.inputPlotXAxis = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.inputPlotXAxis.setObjectName("inputPlotXAxis")
        self.gridLayout_5.addWidget(self.inputPlotXAxis, 1, 1, 1, 4)
        self.inputPlotTitle = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.inputPlotTitle.setMaximumSize(QtCore.QSize(150, 16777215))
        self.inputPlotTitle.setObjectName("inputPlotTitle")
        self.gridLayout_5.addWidget(self.inputPlotTitle, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)
        self.lineColorComboBox = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.lineColorComboBox.setObjectName("lineColorComboBox")
        self.gridLayout_5.addWidget(self.lineColorComboBox, 0, 3, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_5)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.groupBox_5, 3, 0, 1, 2)
        self.cotaRadioBtnGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cotaRadioBtnGroupBox.setFont(font)
        self.cotaRadioBtnGroupBox.setObjectName("cotaRadioBtnGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cotaRadioBtnGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.headerNao = QtWidgets.QRadioButton(parent=self.cotaRadioBtnGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.headerNao.setFont(font)
        self.headerNao.setObjectName("headerNao")
        self.headerButtonGroup = QtWidgets.QButtonGroup(SimplePlotWindow)
        self.headerButtonGroup.setObjectName("headerButtonGroup")
        self.headerButtonGroup.addButton(self.headerNao)
        self.gridLayout_3.addWidget(self.headerNao, 2, 2, 1, 1)
        self.labelHeaderLines = QtWidgets.QLabel(parent=self.cotaRadioBtnGroupBox)
        self.labelHeaderLines.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelHeaderLines.setFont(font)
        self.labelHeaderLines.setMouseTracking(True)
        self.labelHeaderLines.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.labelHeaderLines.setObjectName("labelHeaderLines")
        self.gridLayout_3.addWidget(self.labelHeaderLines, 3, 0, 1, 1)
        self.inputHeaderLines = QtWidgets.QLineEdit(parent=self.cotaRadioBtnGroupBox)
        self.inputHeaderLines.setEnabled(False)
        self.inputHeaderLines.setObjectName("inputHeaderLines")
        self.gridLayout_3.addWidget(self.inputHeaderLines, 3, 1, 1, 2)
        self.cotaProfSim = QtWidgets.QRadioButton(parent=self.cotaRadioBtnGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cotaProfSim.setFont(font)
        self.cotaProfSim.setObjectName("cotaProfSim")
        self.cotaButtonGroup = QtWidgets.QButtonGroup(SimplePlotWindow)
        self.cotaButtonGroup.setObjectName("cotaButtonGroup")
        self.cotaButtonGroup.addButton(self.cotaProfSim)
        self.gridLayout_3.addWidget(self.cotaProfSim, 0, 1, 1, 1)
        self.cotaProfNao = QtWidgets.QRadioButton(parent=self.cotaRadioBtnGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cotaProfNao.setFont(font)
        self.cotaProfNao.setObjectName("cotaProfNao")
        self.cotaButtonGroup.addButton(self.cotaProfNao)
        self.gridLayout_3.addWidget(self.cotaProfNao, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.cotaRadioBtnGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(True)
        self.label_4.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.labelMesaRotativa = QtWidgets.QLabel(parent=self.cotaRadioBtnGroupBox)
        self.labelMesaRotativa.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelMesaRotativa.setFont(font)
        self.labelMesaRotativa.setMouseTracking(True)
        self.labelMesaRotativa.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.labelMesaRotativa.setObjectName("labelMesaRotativa")
        self.gridLayout_3.addWidget(self.labelMesaRotativa, 1, 0, 1, 1)
        self.inputMesaRotativa = QtWidgets.QLineEdit(parent=self.cotaRadioBtnGroupBox)
        self.inputMesaRotativa.setEnabled(False)
        self.inputMesaRotativa.setObjectName("inputMesaRotativa")
        self.gridLayout_3.addWidget(self.inputMesaRotativa, 1, 1, 1, 2)
        self.headerSim = QtWidgets.QRadioButton(parent=self.cotaRadioBtnGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.headerSim.setFont(font)
        self.headerSim.setObjectName("headerSim")
        self.headerButtonGroup.addButton(self.headerSim)
        self.gridLayout_3.addWidget(self.headerSim, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.cotaRadioBtnGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(True)
        self.label_5.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout.addWidget(self.cotaRadioBtnGroupBox, 2, 1, 1, 1)
        self.simplePlotBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simplePlotBtn.sizePolicy().hasHeightForWidth())
        self.simplePlotBtn.setSizePolicy(sizePolicy)
        self.simplePlotBtn.setMinimumSize(QtCore.QSize(200, 25))
        self.simplePlotBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.simplePlotBtn.setObjectName("simplePlotBtn")
        self.gridLayout.addWidget(self.simplePlotBtn, 6, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 2)
        SimplePlotWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=SimplePlotWindow)
        self.statusbar.setObjectName("statusbar")
        SimplePlotWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=SimplePlotWindow)
        self.toolBar.setObjectName("toolBar")
        SimplePlotWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(SimplePlotWindow)
        QtCore.QMetaObject.connectSlotsByName(SimplePlotWindow)
        SimplePlotWindow.setTabOrder(self.selectFileComboBox, self.csvRadioButton)
        SimplePlotWindow.setTabOrder(self.csvRadioButton, self.txtRadioButton)
        SimplePlotWindow.setTabOrder(self.txtRadioButton, self.xlsxRadioButton)
        SimplePlotWindow.setTabOrder(self.xlsxRadioButton, self.cotaProfSim)
        SimplePlotWindow.setTabOrder(self.cotaProfSim, self.cotaProfNao)
        SimplePlotWindow.setTabOrder(self.cotaProfNao, self.inputMesaRotativa)
        SimplePlotWindow.setTabOrder(self.inputMesaRotativa, self.headerSim)
        SimplePlotWindow.setTabOrder(self.headerSim, self.headerNao)
        SimplePlotWindow.setTabOrder(self.headerNao, self.inputHeaderLines)
        SimplePlotWindow.setTabOrder(self.inputHeaderLines, self.inputProfMin)
        SimplePlotWindow.setTabOrder(self.inputProfMin, self.inputProfMax)
        SimplePlotWindow.setTabOrder(self.inputProfMax, self.inputPlotTitle)
        SimplePlotWindow.setTabOrder(self.inputPlotTitle, self.lineColorComboBox)
        SimplePlotWindow.setTabOrder(self.lineColorComboBox, self.inputPlotXAxis)
        SimplePlotWindow.setTabOrder(self.inputPlotXAxis, self.inputPlotYAxis)
        SimplePlotWindow.setTabOrder(self.inputPlotYAxis, self.simplePlotBtn)

    def retranslateUi(self, SimplePlotWindow):
        _translate = QtCore.QCoreApplication.translate
        SimplePlotWindow.setWindowTitle(_translate("SimplePlotWindow", "MainWindow"))
        self.label.setText(_translate("SimplePlotWindow", "Simple Plot"))
        self.selectFileGroupBox.setTitle(_translate("SimplePlotWindow", "File"))
        self.label_2.setText(_translate("SimplePlotWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Select the file:</span></p></body></html>"))
        self.xlsxRadioButton.setText(_translate("SimplePlotWindow", "xlsx"))
        self.label_3.setText(_translate("SimplePlotWindow", "<html><head/><body><p align=\"right\">File type:</p></body></html>"))
        self.txtRadioButton.setText(_translate("SimplePlotWindow", "txt"))
        self.csvRadioButton.setText(_translate("SimplePlotWindow", "csv"))
        self.groupBox_5.setTitle(_translate("SimplePlotWindow", "Plot Settings"))
        self.groupBox.setTitle(_translate("SimplePlotWindow", "Depth limit"))
        self.label_6.setText(_translate("SimplePlotWindow", "Minimum Depth:"))
        self.label_7.setText(_translate("SimplePlotWindow", "Maximum Depth:"))
        self.groupBox_2.setTitle(_translate("SimplePlotWindow", "Title and Axis"))
        self.label_12.setText(_translate("SimplePlotWindow", "Line color"))
        self.label_10.setText(_translate("SimplePlotWindow", "Y axis:"))
        self.label_8.setText(_translate("SimplePlotWindow", "Title:"))
        self.label_9.setText(_translate("SimplePlotWindow", "X axis:"))
        self.cotaRadioBtnGroupBox.setTitle(_translate("SimplePlotWindow", "File Settings"))
        self.headerNao.setText(_translate("SimplePlotWindow", "No"))
        self.labelHeaderLines.setStatusTip(_translate("SimplePlotWindow", "Se houver cabeçalho, quantas linhas pular?"))
        self.labelHeaderLines.setText(_translate("SimplePlotWindow", "<html><head/><body><p align=\"right\">How many lines?:</p></body></html>"))
        self.cotaProfSim.setText(_translate("SimplePlotWindow", "Yes"))
        self.cotaProfNao.setText(_translate("SimplePlotWindow", "No"))
        self.label_4.setStatusTip(_translate("SimplePlotWindow", "Profundidade em cota é igual a mesa rotativa menos a profundidade medida."))
        self.label_4.setText(_translate("SimplePlotWindow", "<html><head/><body><p align=\"right\">TVDSS?*:</p></body></html>"))
        self.labelMesaRotativa.setStatusTip(_translate("SimplePlotWindow", "Mesa rotativa é a altura da plataforma até a superfície do mar/superfície terrestre."))
        self.labelMesaRotativa.setText(_translate("SimplePlotWindow", "<html><head/><body><p align=\"right\">Rotary table:</p></body></html>"))
        self.headerSim.setText(_translate("SimplePlotWindow", "Yes"))
        self.label_5.setStatusTip(_translate("SimplePlotWindow", "Se o arquivo possui cabeçalho. Comum em arquivos las e csv."))
        self.label_5.setText(_translate("SimplePlotWindow", "<html><head/><body><p align=\"right\">Header?:</p></body></html>"))
        self.simplePlotBtn.setText(_translate("SimplePlotWindow", "Plot"))
        self.toolBar.setWindowTitle(_translate("SimplePlotWindow", "toolBar"))
