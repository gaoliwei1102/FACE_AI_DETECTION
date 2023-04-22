import sys
from PyQt5.QtWidgets import *

from sql.tables.course import Course
from sql.tables.student import Student


class MyClass(QWidget):
    def __init__(self):
        super(MyClass, self).__init__()
        self.initUI()

    def initUI(self):
        self.student = Student()
        self.data = self.student.selectAllStudents()

        self.conLayout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnCount(6)


        self.conLayout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '性别', '年龄', '所属班级', '人脸数量'])

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

        verticalHeader = []

        for i in range(0,len(self.data)):
            verticalHeader.append("# " + str(i+1))
            for j in range(1, len(self.data[i])):
                newItem = QTableWidgetItem(str(self.data[i][j]))
                self.tableWidget.setItem(i, j-1, newItem)

        self.tableWidget.setVerticalHeaderLabels(verticalHeader)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = MyClass()
    example.show()
    sys.exit(app.exec_())