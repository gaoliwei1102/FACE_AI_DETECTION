import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from sql.tables.course import Course


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()

        self.button = QPushButton(self)
        self.button.setText("111")
        self.button.clicked.connect(self.testQMess)

    def testQMess(self):
        print(str(QMessageBox().information(self, "Information", "确定退出嘛?", QMessageBox.Yes | QMessageBox.No))

              )

        print(QMessageBox().information(self, "Information", "确定退出嘛?", QMessageBox.Yes | QMessageBox.No))


    def initUI(self):

        self.conLayout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(7)


        self.conLayout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['课程名称', '主讲老师', '班级', '开课日期', '开始时间', '结束时间', '备注'])

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

        for i in range(0,7):

            verticalHeader.append("# " + str(i+1))
            for j in range(1, 7):
                newItem = QTableWidgetItem("1")
                self.tableWidget.setItem(i, j-1, newItem)

        self.tableWidget.setVerticalHeaderLabels(verticalHeader)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    time.sleep(2)
    example.tableWidget.clear()
    sys.exit(app.exec_())