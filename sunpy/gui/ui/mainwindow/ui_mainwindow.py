# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/matt/programming/sunpy/sunpy/gui/ui/mainwindow/mainwindow.ui'
#
# Created: Tue Sep 13 14:13:09 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(662, 615)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SunPy PlotMan", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.fileToolBar = QtGui.QToolBar(MainWindow)
        self.fileToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.fileToolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fileToolBar.setIconSize(QtCore.QSize(22, 22))
        self.fileToolBar.setObjectName(_fromUtf8("fileToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.fileToolBar)
        self.colorOptionsDockWidget = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorOptionsDockWidget.sizePolicy().hasHeightForWidth())
        self.colorOptionsDockWidget.setSizePolicy(sizePolicy)
        self.colorOptionsDockWidget.setFloating(False)
        self.colorOptionsDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.colorOptionsDockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Color options", None, QtGui.QApplication.UnicodeUTF8))
        self.colorOptionsDockWidget.setObjectName(_fromUtf8("colorOptionsDockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cmListWidget = QtGui.QListWidget(self.dockWidgetContents)
        self.cmListWidget.setObjectName(_fromUtf8("cmListWidget"))
        self.verticalLayout.addWidget(self.cmListWidget)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Clip values:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.clipMinDoubleSpinBox = QtGui.QDoubleSpinBox(self.dockWidgetContents)
        self.clipMinDoubleSpinBox.setDecimals(2)
        self.clipMinDoubleSpinBox.setMinimum(0.01)
        self.clipMinDoubleSpinBox.setMaximum(2000.0)
        self.clipMinDoubleSpinBox.setSingleStep(0.01)
        self.clipMinDoubleSpinBox.setObjectName(_fromUtf8("clipMinDoubleSpinBox"))
        self.horizontalLayout_5.addWidget(self.clipMinDoubleSpinBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.clipMaxDoubleSpinBox = QtGui.QDoubleSpinBox(self.dockWidgetContents)
        self.clipMaxDoubleSpinBox.setMinimum(0.01)
        self.clipMaxDoubleSpinBox.setMaximum(2000.0)
        self.clipMaxDoubleSpinBox.setObjectName(_fromUtf8("clipMaxDoubleSpinBox"))
        self.horizontalLayout_6.addWidget(self.clipMaxDoubleSpinBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_4 = QtGui.QLabel(self.dockWidgetContents)
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Scaling:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.scalingComboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.scalingComboBox.setObjectName(_fromUtf8("scalingComboBox"))
        self.scalingComboBox.addItem(_fromUtf8(""))
        self.scalingComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Linear", None, QtGui.QApplication.UnicodeUTF8))
        self.scalingComboBox.addItem(_fromUtf8(""))
        self.scalingComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Logarithmic", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_7.addWidget(self.scalingComboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_5 = QtGui.QLabel(self.dockWidgetContents)
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Gamma:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_8.addWidget(self.label_5)
        self.gammaSlider = QtGui.QSlider(self.dockWidgetContents)
        self.gammaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gammaSlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.gammaSlider.setObjectName(_fromUtf8("gammaSlider"))
        self.horizontalLayout_8.addWidget(self.gammaSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.colorOptionsDockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.colorOptionsDockWidget)
        self.actionOpen_file = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/open_plot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_file.setIcon(icon1)
        self.actionOpen_file.setText(QtGui.QApplication.translate("MainWindow", "Open file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_file.setToolTip(QtGui.QApplication.translate("MainWindow", "Open a FITS file for plotting...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_file.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open a FITS file for plotting...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_file.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_file.setObjectName(_fromUtf8("actionOpen_file"))
        self.actionExit_PlotMan = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit_PlotMan.setIcon(icon2)
        self.actionExit_PlotMan.setText(QtGui.QApplication.translate("MainWindow", "Exit PlotMan", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit_PlotMan.setToolTip(QtGui.QApplication.translate("MainWindow", "Close the application.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit_PlotMan.setStatusTip(QtGui.QApplication.translate("MainWindow", "Close the application.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit_PlotMan.setObjectName(_fromUtf8("actionExit_PlotMan"))
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionExit_PlotMan)
        self.menubar.addAction(self.menuFile.menuAction())
        self.fileToolBar.addAction(self.actionOpen_file)
        self.fileToolBar.addAction(self.actionExit_PlotMan)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QObject.connect(self.actionExit_PlotMan, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

from resources import qrc_resources
