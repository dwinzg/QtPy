# https://realpython.com/python-pyqt-gui-calculator/

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(200, 200, 560, 160)
window.move(60, 15)
helloMsg = QLabel('<h1>Header!</h1>', parent=window)
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec_())