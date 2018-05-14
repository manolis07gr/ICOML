from PySide import QtGui
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'

import main_widget as mw
import styles as st
import misc_functions as mf
import style_parameters as sp


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

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
        actSave = QtGui.QAction('&Save figure', self, statusTip = 'Save figure', triggered = self.saveFigure)
        actExit = QtGui.QAction('E&xit', self, statusTip = 'Exit application', triggered = self.exitApp)
        menuBar = self.menuBar()
        menuFile = menuBar.addMenu('&File')
        menuFile.addAction(actSave)
        menuFile.addAction(actExit)

    def saveFigure(self):
        nameFile = QtGui.QFileDialog.getSaveFileName()
        self.mainWidget.fig.savefig(nameFile[0], facecolor = sp.colorWindow)
        msgBox = QtGui.QMessageBox.information(self, 'Confirmation', 'Saved figure in ' + nameFile[0] + '.')

    def exitApp(self):
        reply = QtGui.QMessageBox.question(self, 'Confirm exit', 'Exit application?', \
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QtGui.QApplication.instance().quit()
        else:
            pass

    def closeEvent(self, event):
        self.exitApp()
        event.ignore()
