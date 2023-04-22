import sys

from PyQt5.QtWidgets import QApplication

from commons import share
from view.py.login import LoginWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    share.loginWindow = LoginWindow()
    share.loginWindow.show()

    sys.exit(app.exec_())
