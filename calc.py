from PyQt5.QtWidgets import * #QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QVBoxLayout, QLineWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Calculadora")
        self.setFixedSize(385,380)
        font = QFont("Century Gothic")
        self.setStyleSheet(
            """            
            background-color: #464860;
            """
        )
        layout = QVBoxLayout()

        self.display =  QLineEdit("")
        self.display.setFixedHeight(50)
        self.display.setFont(font)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(
            """
            background-color: #212338;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            color: white;
            """
        )
        self.display.setAlignment(Qt.AlignRight)
        layout.addWidget(self.display)

        self.buttonLayout = QGridLayout()

        self.buttonNames = {
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "DEL": "DEL",
            "four": "4",
            "five": "5",
            "six": "6",
            "add": "+",
            "one": "1",
            "two": "2",
            "three": "3",
            "sub": "-",
            "deci": ".",
            "zero": "0",
            "div": "/",
            "mul": "*",
            "reset": "RESET",
            "equal": "="
        }        

        for i in self.buttonNames.keys():
            if i not in ["DEL", "reset", "equal"]:
                index = list(self.buttonNames.keys()).index(i)
                btn = QPushButton(self.buttonNames[i])
                btn.setFixedHeight(45)
                btn.pressed.connect(lambda n = self.buttonNames[i]: self.display.setText(self.display.text() + n))
                # i.setFixedSize(50, 40)
                btn.setCursor(Qt.PointingHandCursor)
                btn.setFont(font)
                btn.setStyleSheet(
                    """
                    *{color: black;
                    background-color: white;
                    border-radius: 3px;
                    font-size: 16px;}
                    *:hover{
                        background-color: "Light grey";
                    }
                    """
                )
                self.buttonLayout.addWidget(btn, int(index)//4 , int(index)%4 , 1, 1)

            elif i == "DEL":
                btn = QPushButton(self.buttonNames[i])
                btn.setFixedHeight(45)
                btn.pressed.connect(lambda : self.display.setText(self.display.text()[:-1]))
                btn.setFont(font)
                btn.setCursor(Qt.PointingHandCursor)
                btn.setStyleSheet(
                    """
                    *{background: #464863;
                    color: white;
                    font-size: 16px;}
                    *:hover{
                        background-color: #212330;
                    }
                    """
                )
                self.buttonLayout.addWidget(btn, 0, 3, 1, 1)
            elif i == "reset":
                btn = QPushButton(self.buttonNames[i])
                btn.setFixedHeight(45)
                btn.pressed.connect(lambda n = "": self.display.setText(n))
                btn.setCursor(Qt.PointingHandCursor)
                btn.setFont(font)
                btn.setStyleSheet(
                    """
                    *{background: #464863;
                    color: white;
                    font-size: 16px;}
                    *:hover{
                        background-color: #212330;
                    }
                    """
                )
                self.buttonLayout.addWidget(btn, 4, 0, 1, 2)
            elif i == "equal":
                btn = QPushButton(self.buttonNames[i])
                btn.setFixedHeight(45)
                btn.pressed.connect(self.calc)
                btn.setCursor(Qt.PointingHandCursor)
                btn.setFont(font)
                btn.setStyleSheet(
                    """
                    *{background-color: red;
                    color: white;
                    font-size: 16px;}
                    *:hover{
                        background-color: "Dark red";
                    }
        
                    """
                )
                self.buttonLayout.addWidget(btn, 4, 2, 1, 2)

        btnWidget = QWidget()
        btnWidget.setLayout(self.buttonLayout)
        btnWidget.setStyleSheet("Background-color: #212338; border-radius: 5px;")
        layout.addWidget(btnWidget)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # Callback functions
    def calc(self):
        if self.display.text() == "":
            pass
        else:
            try:
                result = eval(self.display.text())
                self.display.setText(str(eval(self.display.text())))
            except :
                self.display.setText("Error! Check your input")
    
app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()