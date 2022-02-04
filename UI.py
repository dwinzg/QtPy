# https://realpython.com/python-pyqt-gui-calculator/

## Can use this for template structure

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QWidget




## Creates a window with a heading
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Window Title') # Window Title
# window.setGeometry(200, 200, 560, 160)
# window.move(60, 15)
# helloMsg = QLabel('<h1>Header!</h1>', parent=window)
# helloMsg.move(60, 15)
#
# window.show()
#
# sys.exit(app.exec_())


## This creates a 3 buttons on Left/Center/Right (with no functionality)
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle('QHBoxLayout')
# layout = QHBoxLayout() ## This changes the layout of the pop up
# layout.addWidget(QPushButton('Left'))
# layout.addWidget(QPushButton('Center'))
# layout.addWidget(QPushButton('Right'))
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec_())

## Creates a 3x3 grid layout
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle('QGridLayout')
# layout = QGridLayout()
# layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
# layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
# layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
# layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
# layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
# layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
# layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
# layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec_())

## Creates a dialog box with 4 variables and 2 buttons on the bottom
# class Dialog(QDialog):
#     """Dialog."""
#     def __init__(self, parent=None):
#         """Initializer."""
#         super().__init__(parent)
#         self.setWindowTitle('QDialog')
#         dlgLayout = QVBoxLayout()
#         formLayout = QFormLayout()
#         formLayout.addRow('Name:', QLineEdit())
#         formLayout.addRow('Age:', QLineEdit())
#         formLayout.addRow('Job:', QLineEdit())
#         formLayout.addRow('Hobbies:', QLineEdit())
#         dlgLayout.addLayout(formLayout)
#         btns = QDialogButtonBox()
#         btns.setStandardButtons(
#             QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
#         dlgLayout.addWidget(btns)
#         self.setLayout(dlgLayout)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dlg = Dialog()
#     dlg.show()
#     sys.exit(app.exec_())


## Creates a button with functionality when pressed Greet -> Hello World
# def greeting():
#     """Slot function."""
#     if msg.text():
#         msg.setText("")
#     else:
#         msg.setText("Hello World!")
#
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle('Signals and slots')
# layout = QVBoxLayout()
#
# btn = QPushButton('Greet')
# btn.clicked.connect(greeting)  # Connect clicked to greeting()
#
# layout.addWidget(btn)
# msg = QLabel('')
# layout.addWidget(msg)
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec_())