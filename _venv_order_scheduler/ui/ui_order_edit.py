# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_edit.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QTableView, QWidget)

class Ui_orderEdit(object):
    def setupUi(self, orderEdit):
        if not orderEdit.objectName():
            orderEdit.setObjectName(u"orderEdit")
        orderEdit.resize(808, 593)
        self.action2 = QAction(orderEdit)
        self.action2.setObjectName(u"action2")
        self.action3 = QAction(orderEdit)
        self.action3.setObjectName(u"action3")
        self.centralwidget = QWidget(orderEdit)
        self.centralwidget.setObjectName(u"centralwidget")
        self.createNewIterationBtn = QPushButton(self.centralwidget)
        self.createNewIterationBtn.setObjectName(u"createNewIterationBtn")
        self.createNewIterationBtn.setGeometry(QRect(570, 10, 91, 24))
        self.viewHisIterationBtn = QPushButton(self.centralwidget)
        self.viewHisIterationBtn.setObjectName(u"viewHisIterationBtn")
        self.viewHisIterationBtn.setGeometry(QRect(690, 10, 91, 24))
        self.saveBtn = QPushButton(self.centralwidget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(550, 500, 121, 51))
        self.saveAndArrangeBtn = QPushButton(self.centralwidget)
        self.saveAndArrangeBtn.setObjectName(u"saveAndArrangeBtn")
        self.saveAndArrangeBtn.setGeometry(QRect(680, 500, 121, 51))
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 100, 801, 391))
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 10, 262, 21))
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.dateEdit = QDateEdit(self.splitter)
        self.dateEdit.setObjectName(u"dateEdit")
        self.splitter.addWidget(self.dateEdit)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        self.splitter.addWidget(self.label_2)
        self.dateEdit_2 = QDateEdit(self.splitter)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.splitter.addWidget(self.dateEdit_2)
        self.createNewOrderBtn = QPushButton(self.centralwidget)
        self.createNewOrderBtn.setObjectName(u"createNewOrderBtn")
        self.createNewOrderBtn.setGeometry(QRect(20, 50, 91, 31))
        self.createNewTestOrderBtn = QPushButton(self.centralwidget)
        self.createNewTestOrderBtn.setObjectName(u"createNewTestOrderBtn")
        self.createNewTestOrderBtn.setGeometry(QRect(130, 50, 161, 31))
        orderEdit.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(orderEdit)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 808, 22))
        orderEdit.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(orderEdit)
        self.statusbar.setObjectName(u"statusbar")
        orderEdit.setStatusBar(self.statusbar)

        self.retranslateUi(orderEdit)

        QMetaObject.connectSlotsByName(orderEdit)
    # setupUi

    def retranslateUi(self, orderEdit):
        orderEdit.setWindowTitle(QCoreApplication.translate("orderEdit", u"OrderScheduler", None))
        self.action2.setText(QCoreApplication.translate("orderEdit", u"\u521b\u5efa\u65b0\u7684\u8fed\u4ee3", None))
        self.action3.setText(QCoreApplication.translate("orderEdit", u"\u67e5\u770b\u5386\u53f2\u8fed\u4ee3", None))
        self.createNewIterationBtn.setText(QCoreApplication.translate("orderEdit", u"\u521b\u5efa\u65b0\u7684\u8fed\u4ee3", None))
        self.viewHisIterationBtn.setText(QCoreApplication.translate("orderEdit", u"\u67e5\u770b\u5386\u53f2\u8fed\u4ee3", None))
        self.saveBtn.setText(QCoreApplication.translate("orderEdit", u"\u4ec5\u4fdd\u5b58", None))
        self.saveAndArrangeBtn.setText(QCoreApplication.translate("orderEdit", u"\u4fdd\u5b58\u5e76\u6392\u671f", None))
        self.label.setText(QCoreApplication.translate("orderEdit", u"\u5f53\u524d\u8fed\u4ee3\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("orderEdit", u"\u2014\u2014", None))
        self.createNewOrderBtn.setText(QCoreApplication.translate("orderEdit", u"\u521b\u5efa\u5de5\u5355", None))
        self.createNewTestOrderBtn.setText(QCoreApplication.translate("orderEdit", u"\u5feb\u901f\u521b\u5efa\u6d4b\u8bd5\u4efb\u52a1\u5de5\u5355", None))
    # retranslateUi

