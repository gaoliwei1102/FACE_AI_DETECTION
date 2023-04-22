import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from commons.utils import getCurrentDay
from sql.tables.course import Course


class Ui_MyCourse(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1047, 600)
        self.refreshBtn = QtWidgets.QPushButton(Form)
        self.refreshBtn.setGeometry(QtCore.QRect(910, 10, 111, 41))
        self.refreshBtn.setObjectName("refreshBtn")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 1001, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(820, 510, 211, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.searchBtn = QtWidgets.QPushButton(Form)
        self.searchBtn.setGeometry(QtCore.QRect(260, 10, 101, 41))
        self.searchBtn.setObjectName("searchBtn")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 231, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.refreshBtn.setText(_translate("Form", "刷新(Refresh)"))
        self.searchBtn.setText(_translate("Form", "Search"))



class Table(QWidget, Ui_MyCourse):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.course = Course()

        self.lineEdit.setPlaceholderText("请输入课程名称......")
        self.refreshBtn.clicked.connect(self.selectMyAllCourses)
        self.searchBtn.clicked.connect(self.selectMyAllCoursesByName)


        # 设置表头可伸缩模式
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置表格为只读模式
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选中
        # tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        # # 隐藏水平方向的表头
        # tableWidget.verticalHeader().setVisible(False)
        # # 隐藏垂直方向表头
        # tableWidget.horizontalHeader().setVisible(False)

        self.selectMyAllCourses()

    def selectMyAllCourses(self):
        self.data = self.course.selectMyAllCourses()
        self.setData()
        self.lineEdit.setText("")

    def selectMyAllCoursesByName(self):
        name = self.lineEdit.text()
        self.data = self.course.selectMyAllCoursesByName(name)
        self.setData()

    def setData(self):

        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['课程名称', '主讲老师', '班级', '开课日期', '开始时间', '结束时间', '备注'])

        verticalHeader = []

        background = ""
        for i in range(0, len(self.data)):

            if self.data[i][4] > getCurrentDay():
                background = "blue"
            elif self.data[i][4] == getCurrentDay():
                background = "green"
            else:
                background = "gray"

            verticalHeader.append("# " + str(i + 1))
            for j in range(1, len(self.data[i])):
                newItem = QTableWidgetItem(self.data[i][j])
                if background == "blue":
                    newItem.setBackground(QBrush(QColor(115, 185, 255)))
                elif background == "green":
                    newItem.setBackground(QBrush(QColor(0, 255, 0)))
                elif background == "gray":
                    newItem.setBackground(QBrush(QColor(192, 192, 192)))
                self.tableWidget.setItem(i, j - 1, newItem)

        self.tableWidget.setVerticalHeaderLabels(verticalHeader)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())