from PySide import QtGui

import style_parameters as sprm


def returnStyles():
    strStyles = []
    strStyles.append('QMainWindow')
    strStyles.append('{background-color:' + sprm.colorWindow + ';}')

    strStyles.append('QLabel')
    strStyles.append('{color:' + sprm.colorText + ';}')

    strStyles.append('QPushButton')
    strStyles.append('{background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 ' \
        + sprm.colorBackground + ', stop: 1 ' + sprm.colorWindow + ');')
    strStyles.append(' color:' + sprm.colorText + ';')
    strStyles.append(' border: 1px solid ' + sprm.colorBorderButton + ';')
    strStyles.append(' border-radius: 5px;')
    strStyles.append(' min-width: 90px; min-height: 22px;')
    strStyles.append(' margin: 0px 3px 0px 3px;}')
    strStyles.append('QPushButton:focus')
    strStyles.append('{outline: none;')
    strStyles.append(' background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 ' \
        + sprm.colorBackgroundFocus + ', stop: 1 ' + sprm.colorWindowFocus + ');')
    strStyles.append(' color:' + sprm.colorTextFocus + ';}')
    strStyles.append('QPushButton:hover')
    strStyles.append('{background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 ' \
        + sprm.colorBackgroundFocus + ', stop: 1 ' + sprm.colorWindowFocus + ');')
    strStyles.append(' color:' + sprm.colorTextFocus + ';}')
    strStyles.append('QPushButton:Pressed')
    strStyles.append('{background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 ' \
        + sprm.colorBackgroundPressed + ', stop: 1 ' + sprm.colorWindowPressed + ');')
    strStyles.append(' color:' + sprm.colorText + ';}')

    strStyles.append('QMessageBox')
    strStyles.append('{background-color: ' + sprm.colorWindow + ';}')

    strStyles.append('QCheckBox')
    strStyles.append('{color: ' + sprm.colorText + ';}')
    strStyles.append('QCheckBox::indicator:unchecked')
    strStyles.append('{background: ' + sprm.colorWindow + ';')
    strStyles.append(' width: 12px; height: 12px;')
    strStyles.append(' border: 1px solid ' + sprm.colorBorderWidget + ';')
    strStyles.append(' border-radius: 5px;')
    strStyles.append(' margin: 0px 3px 0px 3px;}')
    strStyles.append('QCheckBox::indicator:checked')
    strStyles.append('{background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 ' \
        + sprm.colorCheck + ', stop: 1 ' + sprm.colorBackground + ');')
    strStyles.append(' width: 12px; height: 12px;')
    strStyles.append(' border: 1px solid ' + sprm.colorBorderWidget + ';')
    strStyles.append(' border-radius: 5px;}')
    strStyles.append('QCheckBox:focus')
    strStyles.append('{outline: none;}')

    strStyles.append('QSlider')
    strStyles.append('{background: ' + sprm.colorWindow + ';}')
    strStyles.append('QSlider::handle:horizontal')
    strStyles.append('{background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 ' \
        + sprm.colorCheck + ', stop: 1 ' + sprm.colorBackground + ');')
    strStyles.append(' border: 1px solid ' + sprm.colorBorderWidget + ';')
    strStyles.append(' border-radius: 5px;')
    strStyles.append(' margin: 0px 3px 0px 3px;}')
    strStyles.append('QSlider::horizontal:focus')
    strStyles.append('{outline: none;}')
    strStyles.append('QSlider::add-page:horizontal')
    strStyles.append('{background: ' + sprm.colorBackground + ';')
    strStyles.append(' border: 1px solid ' + sprm.colorBorderWidget + ';')
    strStyles.append(' border-radius: 3px;}')
    strStyles.append('QSlider::sub-page:horizontal')
    strStyles.append('{background: ' + sprm.colorBackground + ';')
    strStyles.append(' border: 1px solid ' + sprm.colorBorderWidget + ';')
    strStyles.append(' border-radius: 3px;}')

    strStyles.append('QListWidget')
    strStyles.append('{background-color: ' + sprm.colorListBackground + ';')
    strStyles.append(' alternate-background-color:' + sprm.colorListAlternate + ';')
    strStyles.append(' selection-color:' + sprm.colorTextSelection + ';')
    strStyles.append(' selection-background-color:' + sprm.colorBackgroundSelect + ';')
    strStyles.append(' color: ' + sprm.colorText + ';')
    strStyles.append(' border: 1px solid ' + sprm.colorBorderWidget + ';')
    strStyles.append(' border-radius: 3px;')
    strStyles.append(' margin: 0px 3px 0px 3px;}')

    strStyles.append('QLineEdit')
    strStyles.append('{max-width: 120px;')
    strStyles.append(' background-color: ' + sprm.colorListBackground + ';')
    strStyles.append(' color: ' + sprm.colorText + ';')
    strStyles.append(' selection-color:' + sprm.colorTextSelection + ';')
    strStyles.append(' selection-background-color:' + sprm.colorBackgroundSelect + ';')
    strStyles.append(' border: 1px solid ' + sprm.colorBorderWidget + ';')
    strStyles.append(' border-radius: 3px;')
    strStyles.append(' margin: 0px 3px 0px 3px;}')

    strStyles.append('QStatusBar')
    strStyles.append('{background: ' + sprm.colorWindow + ';')
    strStyles.append(' color: ' + sprm.colorTextFocus + ';')
    strStyles.append(' font: italic;}')

    strStyles.append('QScrollBar:horizontal')
    strStyles.append('{background: ' + sprm.colorWindow + ';}')
    strStyles.append('QScrollBar:vertical')
    strStyles.append('{background: ' + sprm.colorBackgroundFocus + ';}')
    strStyles.append('QScrollBar:handle')
    strStyles.append('{background: ' + sprm.colorBackgroundFocus + ';}')
    strStyles.append('QScrollBar:down-arrow')
    strStyles.append('{background: ' + sprm.colorBackgroundFocus + ';}')
    strStyles.append('QScrollBar:up-arrow')
    strStyles.append('{background: ' + sprm.colorBackgroundFocus + ';}')
    strStyles.append('QScrollBar:left-arrow')
    strStyles.append('{background: ' + sprm.colorBackgroundFocus + ';}')
    strStyles.append('QScrollBar:right-arrow')
    strStyles.append('{background: ' + sprm.colorBackgroundFocus + ';}')

    strStylesAll = ''.join(strStyles)
    return strStylesAll
