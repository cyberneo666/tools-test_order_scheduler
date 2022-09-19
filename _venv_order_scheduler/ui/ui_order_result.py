# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_result.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_orderResult(object):
    def setupUi(self, orderResult):
        if not orderResult.objectName():
            orderResult.setObjectName(u"orderResult")
        orderResult.resize(779, 523)
        self.tableView = QTableView(orderResult)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 781, 471))
        self.pushButton_3 = QPushButton(orderResult)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(650, 480, 121, 41))

        self.retranslateUi(orderResult)

        QMetaObject.connectSlotsByName(orderResult)
    # setupUi

    def retranslateUi(self, orderResult):
        orderResult.setWindowTitle(QCoreApplication.translate("orderResult", u"\u6392\u671f\u7ed3\u679c", None))
        self.pushButton_3.setText(QCoreApplication.translate("orderResult", u"\u786e\u5b9a", None))
    # retranslateUi

