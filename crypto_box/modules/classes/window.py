from PyQt5 import QtWidgets
import matplotlib
matplotlib.use('Qt5Agg')

import main_widget as mw
import styles as st
import misc_functions as mf
import style_parameters as sp


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.setStyleSheet(st.returnStyles())
        self.initialize()

    def initialize(self):

        self.createStatusBar()
#        self.createToolTip()
        self.createMenuBar()

        self.mainWidget = mw.WidgetMain()
        self.setCentralWidget(self.mainWidget)

        self.resize(1024, 576)
        self.setWindowTitle('StockBox')
        mf.centerWindow(self)

        self.showMaximized()
#        self.showFullScreen()
        self.show()

    def createStatusBar(self):
        self.statusBar().showMessage('')

    def createToolTip(self):
        self.setToolTip('StockBox')

    def createMenuBar(self):
        actSave = QtWidgets.QAction('&Save figure', self, statusTip = 'Save figure', triggered = self.saveFigure)
        actExit = QtWidgets.QAction('E&xit', self, statusTip = 'Exit application', triggered = self.exitApp)
        menuBar = self.menuBar()
        menuFile = menuBar.addMenu('&File')
        menuFile.addAction(actSave)
        menuFile.addAction(actExit)

    def saveFigure(self):
        nameFile = QtWidgets.QFileDialog.getSaveFileName()
        self.mainWidget.fig.savefig(nameFile[0], facecolor = sp.colorWindow)
        msgBox = QtWidgets.QMessageBox.information(self, 'Confirmation', 'Saved figure in ' + nameFile[0] + '.')

    def exitApp(self):
        reply = QtWidgets.QMessageBox.question(self, 'Confirm exit', 'Exit application?', \
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.QApplication.instance().quit()
        else:
            pass

    def closeEvent(self, event):
        self.exitApp()
        event.ignore()
