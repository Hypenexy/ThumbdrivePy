import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QWidget

from layout_colorwidget import Color

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        self.setMinimumSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(button)
        
        self.setWindowTitle("My App")

        layout = QHBoxLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("orange"))
        layout.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
