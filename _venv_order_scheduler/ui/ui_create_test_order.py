# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_test_order.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_createTestOrder(object):
    def setupUi(self, createTestOrder):
        if not createTestOrder.objectName():
            createTestOrder.setObjectName(u"createTestOrder")
        createTestOrder.resize(400, 300)
        self.buttonBox = QDialogButtonBox(createTestOrder)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.comboBox = QComboBox(createTestOrder)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(230, 60, 81, 22))
        self.dateEdit = QDateEdit(createTestOrder)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(260, 190, 110, 22))
        self.label_2 = QLabel(createTestOrder)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 30, 53, 16))
        self.label = QLabel(createTestOrder)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 53, 16))
        self.label_3 = QLabel(createTestOrder)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 30, 53, 16))
        self.lineEdit = QLineEdit(createTestOrder)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 60, 191, 21))
        self.lineEdit_2 = QLineEdit(createTestOrder)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(320, 60, 51, 21))
        self.comboBox_2 = QComboBox(createTestOrder)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(230, 90, 81, 22))
        self.lineEdit_3 = QLineEdit(createTestOrder)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(320, 90, 51, 21))
        self.lineEdit_4 = QLineEdit(createTestOrder)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 90, 191, 21))
        self.lineEdit_5 = QLineEdit(createTestOrder)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 120, 191, 21))
        self.lineEdit_6 = QLineEdit(createTestOrder)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(320, 120, 51, 21))
        self.comboBox_3 = QComboBox(createTestOrder)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(230, 120, 81, 22))
        self.label_4 = QLabel(createTestOrder)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 190, 91, 16))

        self.retranslateUi(createTestOrder)
        self.buttonBox.accepted.connect(createTestOrder.accept)
        self.buttonBox.rejected.connect(createTestOrder.reject)

        QMetaObject.connectSlotsByName(createTestOrder)
    # setupUi

    def retranslateUi(self, createTestOrder):
        createTestOrder.setWindowTitle(QCoreApplication.translate("createTestOrder", u"\u5feb\u901f\u521b\u5efa\u6d4b\u8bd5\u4efb\u52a1\u7684\u5de5\u5355", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("createTestOrder", u"\u6d4b\u8bd5\u8bbe\u8ba1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("createTestOrder", u"\u6d4b\u8bd5\u7528\u4f8b", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("createTestOrder", u"\u7528\u4f8b\u8bc4\u5ba1", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("createTestOrder", u"\u6d4b\u8bd5\u6267\u884c", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("createTestOrder", u"\u7f16\u5199\u6d4b\u8bd5\u62a5\u544a", None))

        self.label_2.setText(QCoreApplication.translate("createTestOrder", u"\u5de5\u5355\u7c7b\u578b", None))
        self.label.setText(QCoreApplication.translate("createTestOrder", u"\u5de5\u5355\u5185\u5bb9", None))
        self.label_3.setText(QCoreApplication.translate("createTestOrder", u"\u9884\u8ba1\u5de5\u65f6", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("createTestOrder", u"\u6d4b\u8bd5\u8bbe\u8ba1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("createTestOrder", u"\u6d4b\u8bd5\u7528\u4f8b", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("createTestOrder", u"\u7528\u4f8b\u8bc4\u5ba1", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("createTestOrder", u"\u6d4b\u8bd5\u6267\u884c", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("createTestOrder", u"\u7f16\u5199\u6d4b\u8bd5\u62a5\u544a", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("createTestOrder", u"\u6d4b\u8bd5\u8bbe\u8ba1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("createTestOrder", u"\u6d4b\u8bd5\u7528\u4f8b", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("createTestOrder", u"\u7528\u4f8b\u8bc4\u5ba1", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("createTestOrder", u"\u6d4b\u8bd5\u6267\u884c", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("createTestOrder", u"\u7f16\u5199\u6d4b\u8bd5\u62a5\u544a", None))

        self.label_4.setText(QCoreApplication.translate("createTestOrder", u"\u9884\u8ba1\u63d0\u6d4b\u65f6\u95f4", None))
    # retranslateUi

