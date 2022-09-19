import sys
from typing import OrderedDict
import PySide6
from PySide6.QtWidgets  import QApplication,QMainWindow,QDialog
from PySide6.QtCore import QFile
#sys.path.append(".\\ui\\")
from ui.ui_order_edit import Ui_orderEdit
from ui.ui_order_result import Ui_orderResult
from ui.ui_create_order import Ui_createOrder
from ui.ui_create_test_order import Ui_createTestOrder


class OrderEdit_Window(Ui_orderEdit,QMainWindow):
    def __init__(self) -> None:
        super(Ui_orderEdit,self).__init__()
        self.setupUi(self)
    def openResult(self):
        self.result=Ui_orderResult()
        self.result.show(self)
class OrderResult_Window(Ui_orderResult,QDialog):
    def __init__(self) -> None:
        super(Ui_orderResult,self).__init__()
        self.setupUi(self)
class CreateOrder_Window(Ui_createOrder,QDialog):
    def __init__(self) -> None:
        super(Ui_createOrder,self).__init__()
        self.setupUi(self)
class CreateTestOrder_Window(Ui_createTestOrder,QMainWindow):
    def __init__(self) -> None:
        super(Ui_createTestOrder,self).__init__()
        self.setupUi(self)
if __name__== "__main__":
    app=QApplication(sys.argv)
    orderEdit=OrderEdit_Window()
    orderResult=OrderResult_Window
    createOrder=CreateOrder_Window
    createTestOrder=CreateTestOrder_Window
    
    orderEdit.show()
    orderEdit.createNewOrderBtn.clicked.connect(createOrder.show)
    #orderEdit.saveAndArrangeBtn.clicked.connect(orderResult.show(orderEdit))
    sys.exit(app.exec_())