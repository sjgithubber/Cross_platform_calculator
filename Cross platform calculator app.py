# Cross platform calculator 
# built using pyqt5
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator using PySide6")
        self.setFixedSize(350, 450)
        # self.setWindowIcon(QIcon('calculator.png')) # Optional

        # set up central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)


        # Create vertical layout to hold display and buttons
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentMargins(10, 10, 10, 10)

        # Create the display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # set font for display
        font = QFont()
        font.setPointSize(28)
        self.display.setFont(font)

        # set minimum height for display
        self.display.setMinimumHeight(70)

        # add display to main box layout
        main_layout.addWidget(self.display)

        # add grid for buttons
        buttons_layout = QGridLayout()
        buttons_layout.setSpacing(5)
        main_layout.addLayout(buttons_layout)


         # Button text and positions in the grid
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), 'C': (3, 2), '+': (3, 3),
            '=': (4, 0, 1, 4)  # This button spans 4 columns
        }

        self.buttons = {}

        # create and add buttons to the grid
        for button_text, position in buttons.items():
            button = QPushButton(button_text)
            button.setFont(QFont('Arial', 14))
            butotn.setMinimumSize(65, 65)
            button.clicked.connect(self.button_clicked)

            # make the '=' button span multiple columns
            if len(position) > 2:
                buttons_layout.addWidget(button, position[0], position[1], position[2], position[3])
            else:
                buttons_layout.addWidget(button, position[0], position[1])

            self.butotns[button_text] = button
        
        
