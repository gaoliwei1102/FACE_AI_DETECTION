import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DialogDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle("Dialog 例子")
        self.resize(350, 300)

        self.btn = QPushButton(self)
        self.btn.setText("弹出对话框")
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        btn = QPushButton("ok", dialog)
        btn.move(50, 50)
        dialog.setWindowTitle("Dialog")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DialogDemo()
    demo.show()
    sys.exit(app.exec_())
