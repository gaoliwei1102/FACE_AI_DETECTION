import sys
from PyQt5.QtWidgets import *

from sql.tables.course import Course
from sql.tables.student import Student
from sql.tables.violate import Violate


class MyViolates(QWidget):
    def __init__(self):
        super(MyViolates, self).__init__()
        self.initUI()

    def initUI(self):
        self.violate = Violate()
        self.data = self.violate.selectMyAllViolates()

        self.conLayout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnCount(9)


        self.conLayout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['违规ID', '违规类型', '违规课程', '记录老师', '课程日期',
                                                    '开始时间', '结束时间', '备注', '创建时间'])

        # 设置表头可伸缩模式
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #设置表格为只读模式
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #整行选中
        # tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        # # 隐藏水平方向的表头
        # tableWidget.verticalHeader().setVisible(False)
        # # 隐藏垂直方向表头
        # tableWidget.horizontalHeader().setVisible(False)

        self.setLayout(self.conLayout)
        self.setData()

    def setData(self):

        #0----->违规ID
        #1----->违规类型
        #2----->违规课程
        #3----->违规学生
        #4----->备注
        #5----->创建时间

        course = Course()

        self.courses = []

        for i in range(0, len(self.data)):
            self.courses.append(course.selectCourseById(self.data[i][2])[0])

        verticalHeader = []

        for i in range(0,len(self.data)):
            verticalHeader.append("# " + str(i + 1))

            newItem00 = QTableWidgetItem(self.data[i][0])
            self.tableWidget.setItem(i, 0, newItem00)

            newItem01 = QTableWidgetItem(self.data[i][1])
            self.tableWidget.setItem(i, 1, newItem01)

            newItem02 = QTableWidgetItem(self.courses[i][1])
            self.tableWidget.setItem(i, 2, newItem02)

            newItem03 = QTableWidgetItem(self.courses[i][2])
            self.tableWidget.setItem(i, 3, newItem03)

            newItem04 = QTableWidgetItem(self.courses[i][4])
            self.tableWidget.setItem(i, 4, newItem04)

            newItem05 = QTableWidgetItem(self.courses[i][5])
            self.tableWidget.setItem(i, 5, newItem05)

            newItem06 = QTableWidgetItem(self.courses[i][6])
            self.tableWidget.setItem(i, 6, newItem06)

            newItem07 = QTableWidgetItem(self.data[i][4])
            self.tableWidget.setItem(i, 7, newItem07)

            newItem08 = QTableWidgetItem(self.data[i][5])
            self.tableWidget.setItem(i, 8, newItem08)

        self.tableWidget.setVerticalHeaderLabels(verticalHeader)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = MyViolates()
    example.show()
    sys.exit(app.exec_())