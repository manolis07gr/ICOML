import sys
sys.path.append('./modules/symbol_widgets')
sys.path.append('./modules/timeseries_widgets')
sys.path.append('./modules/histogram_widgets')
sys.path.append('./modules/risk_return_widgets')
sys.path.append('./modules/classes')
from PyQt5 import QtGui, QtWidgets
import window as win


application = QtWidgets.QApplication(sys.argv)
pixmap = QtGui.QPixmap('splash.png')
splash = QtWidgets.QSplashScreen(pixmap)
splash.show()
window = win.MainWindow()
splash.finish(window)
sys.exit(application.exec_())
