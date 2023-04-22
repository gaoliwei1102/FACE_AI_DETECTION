from PyQt5.QtWidgets import QWidget, QMainWindow, QStackedLayout

from commons import share
from view.py.editMyself import EditMyselfPage
from view.py.enterDetection import EnterDetectionPage
from view.py.faceDelete import FaceDeletePage
from view.py.faceRegister import FaceRegisterPage
from view.py.main import Ui_MainWindow
from view.py.myClass import MyClass
from view.py.myCourse import Table
from view.py.myViolates import MyViolates
from view.py.testDetection import TestDetectionPage


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print(share.currentUser)
        # 实例化一个堆叠布局
        self.qsl = QStackedLayout(self.frame)

        # 实例化分页面
        self.testDetectionPage = TestDetectionPage()
        self.editMyselfPage = EditMyselfPage()
        self.testTable = Table()
        self.myClass = MyClass()
        self.faceRegisterPage = FaceRegisterPage()
        self.faceDeletePage = FaceDeletePage()
        self.enterDetectionPage = EnterDetectionPage()
        self.myViolates = MyViolates()

        # 加入到布局中
        self.qsl.addWidget(self.testDetectionPage)
        self.qsl.addWidget(self.editMyselfPage)
        self.qsl.addWidget(self.testTable)
        self.qsl.addWidget(self.myClass)
        self.qsl.addWidget(self.faceRegisterPage)
        self.qsl.addWidget(self.faceDeletePage)
        self.qsl.addWidget(self.enterDetectionPage)
        self.qsl.addWidget(self.myViolates)


        # 控制函数
        self.controller()

    def controller(self):
        self.testDetectionBtn.clicked.connect(self.switch)
        self.editSelfBtn.clicked.connect(self.switch)
        self.myCoursesBtn.clicked.connect(self.switch)
        self.myClassesBtn.clicked.connect(self.switch)
        self.updateFaceBtn.clicked.connect(self.switch)
        self.deleteFaceBtn.clicked.connect(self.switch)
        self.enterDetectionBtn.clicked.connect(self.switch)
        self.searchViolateBtn.clicked.connect(self.switch)

    def switch(self):
        sender = self.sender().objectName()

        index = {
            "testDetectionBtn": 0,
            "editSelfBtn": 1,
            "myCoursesBtn": 2,
            "myClassesBtn": 3,
            "updateFaceBtn": 4,
            "deleteFaceBtn": 5,
            "enterDetectionBtn":6,
            "searchViolateBtn":7,
        }

        self.qsl.setCurrentIndex(index[sender])