import sys
import PySide6
from PySide6.QtWidgets  import QApplication,QMainWindow,QDialog
from PySide6.QtCore import QFile
#sys.path.append(".\\ui\\")
from ui.ui_order_edit import Ui_orderEdit
from ui.ui_order_result import Ui_orderResult
from ui.ui_create_order import Ui_createOrder
from ui.ui_create_test_order import Ui_createTestOrder
from ui.ui_create_iteration import Ui_createIteration

#主窗口
class OrderEdit_Window(Ui_orderEdit,QMainWindow):
    def __init__(self) -> None:
        super(Ui_orderEdit,self).__init__()
        self.setupUi(self)
        #定义子窗体变量
        self.resultWin=OrderResult_Window()
        self.createOrderWin=CreateOrder_Window()
        self.createNewTestOrderWin=CreateTestOrder_Window()
        self.createNewIterationWin=CreateIteration_Window()
        #按钮绑定
        self.saveAndArrangeBtn.clicked.connect(self.resultWin.show)
        self.createNewOrderBtn.clicked.connect(self.createOrderWin.show)
        self.createNewTestOrderBtn.clicked.connect(self.createNewTestOrderWin.show)
        self.createNewIterationBtn.clicked.connect(self.createNewIterationWin.show)
#排期结果窗口
class OrderResult_Window(Ui_orderResult,QDialog):
    def __init__(self) -> None:
        super(Ui_orderResult,self).__init__()
        self.setupUi(self)
#创建工单窗口        
class CreateOrder_Window(Ui_createOrder,QDialog):
    def __init__(self) -> None:
        super(Ui_createOrder,self).__init__()
        self.setupUi(self)
#快速创建测试工单窗口        
class CreateTestOrder_Window(Ui_createTestOrder,QDialog):
    def __init__(self) -> None:
        super(Ui_createTestOrder,self).__init__()
        self.setupUi(self)
class CreateIteration_Window(Ui_createIteration,QDialog):
    def __init__(self) -> None:
        super(Ui_createIteration,self).__init__()
        self.setupUi(self)
if __name__== "__main__":
    app=QApplication(sys.argv)
    orderEdit=OrderEdit_Window()
    orderEdit.show()
    sys.exit(app.exec_())