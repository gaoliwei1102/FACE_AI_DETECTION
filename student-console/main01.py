import sys

from PyQt5.QtWidgets import QWidget, QStackedLayout, QApplication
#
# from main import Ui_Main
# from page1 import Ui_Page01
# from page2 import Ui_Page02
#
#
# class Page01(QWidget, Ui_Page01):
#
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
#
# class Page02(QWidget, Ui_Page02):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
#
# class MainWindow(QWidget, Ui_Main):
#
    # def __init__(self):
    #     super().__init__()
    #     self.setupUi(self)
    #
    #     # 实例化一个堆叠布局
    #     self.qsl = QStackedLayout(self.frame)
    #
    #     # 实例化分页面
    #     self.page01 = Page01()
    #     self.page02 = Page02()
    #
    #     # 加入到布局中
    #     self.qsl.addWidget(self.page01)
    #     self.qsl.addWidget(self.page02)
    #
    #     # 控制函数
    #     self.controller()
    #
    # def controller(self):
    #     self.pushButton.clicked.connect(self.switch)
    #     self.pushButton_2.clicked.connect(self.switch)
    #
    # def switch(self):
    #     sender = self.sender().objectName()
    #
    #     index = {
    #         "pushButton": 0,
    #         "pushButton_2": 1,
    #     }
    #
    #     self.qsl.setCurrentIndex(index[sender])
#
from commons import share
from view.main import MainWindow
from view.py.login import LoginWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)

    share.loginWindow = LoginWindow()
    share.loginWindow.show()

    sys.exit(app.exec_())

