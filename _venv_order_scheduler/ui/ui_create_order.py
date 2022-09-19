# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_order.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDialog, QDialogButtonBox, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_createOrder(object):
    def setupUi(self, createOrder):
        if not createOrder.objectName():
            createOrder.setObjectName(u"createOrder")
        createOrder.resize(400, 299)
        self.buttonBox = QDialogButtonBox(createOrder)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 250, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(createOrder)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 53, 16))
        self.label_2 = QLabel(createOrder)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 53, 16))
        self.comboBox = QComboBox(createOrder)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 100, 261, 22))
        self.dateEdit = QDateEdit(createOrder)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(200, 210, 110, 22))
        self.checkBox = QCheckBox(createOrder)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(100, 210, 80, 20))
        self.lineEdit = QLineEdit(createOrder)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 40, 291, 21))
        self.label_3 = QLabel(createOrder)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 160, 61, 16))
        self.lineEdit_2 = QLineEdit(createOrder)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 160, 71, 21))

        self.retranslateUi(createOrder)
        self.buttonBox.accepted.connect(createOrder.accept)
        self.buttonBox.rejected.connect(createOrder.reject)

        QMetaObject.connectSlotsByName(createOrder)
    # setupUi

    def retranslateUi(self, createOrder):
        createOrder.setWindowTitle(QCoreApplication.translate("createOrder", u"\u521b\u5efa\u5de5\u5355", None))
        self.label.setText(QCoreApplication.translate("createOrder", u"\u5de5\u5355\u5185\u5bb9", None))
        self.label_2.setText(QCoreApplication.translate("createOrder", u"\u5de5\u5355\u7c7b\u578b", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("createOrder", u"\u6d4b\u8bd5\u8bbe\u8ba1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("createOrder", u"\u6d4b\u8bd5\u7528\u4f8b", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("createOrder", u"\u7528\u4f8b\u8bc4\u5ba1", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("createOrder", u"\u6d4b\u8bd5\u6267\u884c", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("createOrder", u"\u7f16\u5199\u6d4b\u8bd5\u62a5\u544a", None))

        self.checkBox.setText(QCoreApplication.translate("createOrder", u"\u6307\u5b9a\u65e5\u671f\u5b8c\u6210", None))
        self.label_3.setText(QCoreApplication.translate("createOrder", u"\u9884\u8ba1\u5de5\u65f6/h", None))
    # retranslateUi

