from PyQt5 import QtWidgets
import datetime as dt


def centerWindow(widget):
    geomWindow = widget.frameGeometry()
    centerScreen = QtWidgets.QDesktopWidget().availableGeometry().center()
    geomWindow.moveCenter(centerScreen)
    widget.move(geomWindow.bottomLeft())


def findLastWeekday(date):
    if dt.date.weekday(date) == 5:
        date -= dt.timedelta(days = 1)
    elif dt.date.weekday(date) == 6:
        date -= dt.timedelta(days = 2)
    return date


def openFile(nameFile):
    try:
        data = open(nameFile, 'r', encoding='utf-8')
        return data
    except:
        errorMessage('Error: Unable to find ' + nameFile + '.')


def countLinesFile(nameFile):
    try:
        lines = open(nameFile, 'r', encoding='utf-8')
        nLines = sum(1 for line in lines)
        lines.close()
        return nLines-1
    except:
        errorMessage('Error: Unable to find ' + nameFile + '.')


def errorMessage(string):
    QtWidgets.QMessageBox.critical(None, 'Error!', string, QtWidgets.QMessageBox.Ok)


def quitApp():
    errorMessage('Quitting...')
    quit()
