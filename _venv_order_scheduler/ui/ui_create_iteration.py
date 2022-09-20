# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_iteration.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QWidget)

class Ui_createIteration(object):
    def setupUi(self, createIteration):
        if not createIteration.objectName():
            createIteration.setObjectName(u"createIteration")
        createIteration.resize(351, 157)
        self.buttonBox = QDialogButtonBox(createIteration)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-10, 120, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.startDate = QDateEdit(createIteration)
        self.startDate.setObjectName(u"startDate")
        self.startDate.setGeometry(QRect(120, 20, 110, 22))
        self.endDate = QDateEdit(createIteration)
        self.endDate.setObjectName(u"endDate")
        self.endDate.setGeometry(QRect(120, 70, 110, 22))
        self.label = QLabel(createIteration)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 91, 16))
        self.label_2 = QLabel(createIteration)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 91, 16))

        self.retranslateUi(createIteration)
        self.buttonBox.accepted.connect(createIteration.accept)
        self.buttonBox.rejected.connect(createIteration.reject)

        QMetaObject.connectSlotsByName(createIteration)
    # setupUi

    def retranslateUi(self, createIteration):
        createIteration.setWindowTitle(QCoreApplication.translate("createIteration", u"\u521b\u5efa\u65b0\u7684\u8fed\u4ee3", None))
        self.label.setText(QCoreApplication.translate("createIteration", u"\u8fed\u4ee3\u5f00\u59cb\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("createIteration", u"\u8fed\u4ee3\u7ed3\u675f\u65e5\u671f", None))
    # retranslateUi

