import math
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from calc import *



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Kalkulator()
        self.ui.setupUi(self)
        self.ui.text.setText("")
        self.ui.num1.clicked.connect(self.num_1)
        self.ui.num2.clicked.connect(self.num_2)
        self.ui.num3.clicked.connect(self.num_3)
        self.ui.num4.clicked.connect(self.num_4)
        self.ui.num5.clicked.connect(self.num_5)
        self.ui.num6.clicked.connect(self.num_6)
        self.ui.num7.clicked.connect(self.num_7)
        self.ui.num8.clicked.connect(self.num_8)
        self.ui.num9.clicked.connect(self.num_9)
        self.ui.num0.clicked.connect(self.num_0)
        self.ui.plus.clicked.connect(self.plus)
        self.ui.devide.clicked.connect(self.devide)
        self.ui.multyply.clicked.connect(self.multuply)
        self.ui.minus.clicked.connect(self.minus)
        self.ui.equal.clicked.connect(self.equal)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.sqrt.clicked.connect(self.sqrt_click)
        self.ui.pow.clicked.connect(self.pow_click)
        self.ui.x_1.clicked.connect(self.x_1)
        self.ui.coma.clicked.connect(self.coma)
        self.ui.plus_minus.clicked.connect(self.plus_minus)
        self.ui.Left_s.clicked.connect(self.Left_s)
        self.ui.Right_s.clicked.connect(self.Right_s)
        self.ui.back.clicked.connect(self.back_click)
        self.ui.persent.clicked.connect(self.persent)

    def num_1(self):
        self.ui.text.setText(self.ui.text.text() + "1")

    def num_2(self):
        self.ui.text.setText(self.ui.text.text() + "2")

    def num_3(self):
        self.ui.text.setText(self.ui.text.text() + "3")

    def num_4(self):
        self.ui.text.setText(self.ui.text.text() + "4")

    def num_5(self):
        self.ui.text.setText(self.ui.text.text() + "5")

    def num_6(self):
        self.ui.text.setText(self.ui.text.text() + "6")

    def num_7(self):
        self.ui.text.setText(self.ui.text.text() + "7")

    def num_8(self):
        self.ui.text.setText(self.ui.text.text() + "8")

    def num_9(self):
        self.ui.text.setText(self.ui.text.text() + "9")

    def num_0(self):
        self.ui.text.setText(self.ui.text.text() + "0")

    def plus(self):
        self.ui.text.setText(self.ui.text.text() + "+")

    def minus(self):
        self.ui.text.setText(self.ui.text.text() + "-")

    def Left_s(self):
        self.ui.text.setText(self.ui.text.text() + "(")

    def Right_s(self):
        self.ui.text.setText(self.ui.text.text() + ")")

    def devide(self):
        self.ui.text.setText(self.ui.text.text() + "/")

    def multuply(self):
        self.ui.text.setText(self.ui.text.text() + "*")

    def clear(self):
        self.ui.text.setText(self.ui.text.setText(""))

    def sqrt_click(self):
        self.ui.text.setText(str(math.sqrt(eval(self.ui.text.text()))))

    def pow_click(self):
        self.ui.text.setText(str(eval(self.ui.text.text()) ** 2))

    def coma(self):
        self.ui.text.setText(self.ui.text.text() + ".")

    def x_1(self):
        self.ui.text.setText(str(1 / eval(self.ui.text.text())))

    def equal(self):
        self.ui.text.setText(str(eval(self.ui.text.text())))

    def plus_minus(self):
        self.ui.text.setText(self.ui.text.text() + "-")

    def back_click(self):
        str1 = self.ui.text.text()
        str1 = str1[0:-1]
        self.ui.text.setText(str1)

    def persent(self):
        str1 = self.ui.text.text()
        if "+" in str1:
            list1 = str1.split("+")
            l1=int(list1[0])
            l2=int(list1[1])
            res=l1*l2/100+l1
        elif "-" in str1:
            list1 = str1.split("-")
            l1 = int(list1[0])
            l2 = int(list1[1])
            res =l1 - l1 * l2 / 100
        self.ui.text.setText(str(res))


import sys
app = QtWidgets.QApplication(sys.argv)
application = Window()
application.show()
sys.exit(app.exec())

