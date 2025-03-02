import sys
from PyQt6.QtGui import QKeySequence
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QTextEdit,
    QMessageBox)


class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centeral_widget = QWidget()
        self.setCentralWidget(self.centeral_widget)
        self.setWindowTitle('Binary finder')
        self.setFixedSize(1000, 500)

        self.TextArea = QTextEdit()
        self.TextArea.setPlaceholderText(
            'Find binary value')

        self.result = QTextEdit()
        self.result.setReadOnly(True)

        self.button = QPushButton()
        self.button.setText('Enter')
        self.button.setShortcut(QKeySequence('Enter'))
        self.button.clicked.connect(self.print_huhuuhh)

        layout = QVBoxLayout()
        layout.addWidget(self.TextArea)
        layout.addWidget(self.result)
        layout.addWidget(self.button)

        self.centeral_widget.setLayout(layout)

    def print_huhuuhh(self):
        try:

            text = self.TextArea.toPlainText().strip()

            if text.isdigit():
                find_bin = bin(int(text))[2:]
                self.result.setText(find_bin)
            else:
                raise TypeError(
                    'Please enter valid integer value')
        except TypeError as e:
            self.error = QMessageBox()
            self.error.setWindowTitle('Oops!')
            self.error.setText(f'An TypeError occurred: {e}')
            self.error.setIcon(QMessageBox.Icon.Critical)
            self.error.setStandardButtons(QMessageBox.StandardButton.Cancel)
            self.error.exec()


def load_qss_file(app, filename):
    with open(filename, 'r') as qssfile:
        app.setStyleSheet(qssfile.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    load_qss_file(app, 'style.qss')
    window = win()
    window.show()
    app.exec()
