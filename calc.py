# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kalkulator(object):
    def setupUi(self, Kalkulator):
        Kalkulator.setObjectName("Kalkulator")
        Kalkulator.resize(927, 613)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Kalkulator.sizePolicy().hasHeightForWidth())
        Kalkulator.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Kalkulator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QWidget(self.centralwidget)
        self.top.setMinimumSize(QtCore.QSize(0, 100))
        self.top.setObjectName("top")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.top)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.text = QtWidgets.QLabel(self.top)
        self.text.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text.setObjectName("text")
        self.verticalLayout_5.addWidget(self.text)
        self.verticalLayout.addWidget(self.top)
        self.button = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setObjectName("button")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.button)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.persent = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.persent.sizePolicy().hasHeightForWidth())
        self.persent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.persent.setFont(font)
        self.persent.setObjectName("persent")
        self.verticalLayout_23.addWidget(self.persent)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_10 = QtWidgets.QWidget(self.widget)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_30 = QtWidgets.QWidget(self.widget_10)
        self.widget_30.setObjectName("widget_30")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Left_s = QtWidgets.QPushButton(self.widget_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Left_s.sizePolicy().hasHeightForWidth())
        self.Left_s.setSizePolicy(sizePolicy)
        self.Left_s.setObjectName("Left_s")
        self.horizontalLayout_4.addWidget(self.Left_s)
        self.Right_s = QtWidgets.QPushButton(self.widget_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Right_s.sizePolicy().hasHeightForWidth())
        self.Right_s.setSizePolicy(sizePolicy)
        self.Right_s.setObjectName("Right_s")
        self.horizontalLayout_4.addWidget(self.Right_s)
        self.horizontalLayout_3.addWidget(self.widget_30)
        self.verticalLayout_2.addWidget(self.widget_10)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.num7 = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num7.sizePolicy().hasHeightForWidth())
        self.num7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num7.setFont(font)
        self.num7.setObjectName("num7")
        self.verticalLayout_25.addWidget(self.num7)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.num4 = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num4.sizePolicy().hasHeightForWidth())
        self.num4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num4.setFont(font)
        self.num4.setObjectName("num4")
        self.verticalLayout_26.addWidget(self.num4)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.num1 = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num1.sizePolicy().hasHeightForWidth())
        self.num1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num1.setFont(font)
        self.num1.setObjectName("num1")
        self.verticalLayout_27.addWidget(self.num1)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.plus_minus = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus_minus.sizePolicy().hasHeightForWidth())
        self.plus_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.plus_minus.setFont(font)
        self.plus_minus.setObjectName("plus_minus")
        self.verticalLayout_28.addWidget(self.plus_minus)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.button)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_11 = QtWidgets.QWidget(self.widget_2)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.sqrt = QtWidgets.QPushButton(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqrt.sizePolicy().hasHeightForWidth())
        self.sqrt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sqrt.setFont(font)
        self.sqrt.setObjectName("sqrt")
        self.verticalLayout_22.addWidget(self.sqrt)
        self.verticalLayout_3.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_2)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.clear = QtWidgets.QPushButton(self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.verticalLayout_21.addWidget(self.clear)
        self.verticalLayout_3.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.widget_2)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.num8 = QtWidgets.QPushButton(self.widget_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num8.sizePolicy().hasHeightForWidth())
        self.num8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num8.setFont(font)
        self.num8.setObjectName("num8")
        self.verticalLayout_20.addWidget(self.num8)
        self.verticalLayout_3.addWidget(self.widget_13)
        self.widget_14 = QtWidgets.QWidget(self.widget_2)
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.num5 = QtWidgets.QPushButton(self.widget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num5.sizePolicy().hasHeightForWidth())
        self.num5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num5.setFont(font)
        self.num5.setObjectName("num5")
        self.verticalLayout_19.addWidget(self.num5)
        self.verticalLayout_3.addWidget(self.widget_14)
        self.widget_15 = QtWidgets.QWidget(self.widget_2)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.num2 = QtWidgets.QPushButton(self.widget_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num2.sizePolicy().hasHeightForWidth())
        self.num2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num2.setFont(font)
        self.num2.setObjectName("num2")
        self.verticalLayout_18.addWidget(self.num2)
        self.verticalLayout_3.addWidget(self.widget_15)
        self.widget_16 = QtWidgets.QWidget(self.widget_2)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.num0 = QtWidgets.QPushButton(self.widget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num0.sizePolicy().hasHeightForWidth())
        self.num0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num0.setFont(font)
        self.num0.setObjectName("num0")
        self.verticalLayout_17.addWidget(self.num0)
        self.verticalLayout_3.addWidget(self.widget_16)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.button)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_20 = QtWidgets.QWidget(self.widget_3)
        self.widget_20.setObjectName("widget_20")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.widget_20)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.pow = QtWidgets.QPushButton(self.widget_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pow.sizePolicy().hasHeightForWidth())
        self.pow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pow.setFont(font)
        self.pow.setObjectName("pow")
        self.verticalLayout_29.addWidget(self.pow)
        self.verticalLayout_4.addWidget(self.widget_20)
        self.widget_21 = QtWidgets.QWidget(self.widget_3)
        self.widget_21.setObjectName("widget_21")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_21)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.back = QtWidgets.QPushButton(self.widget_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.verticalLayout_16.addWidget(self.back)
        self.verticalLayout_4.addWidget(self.widget_21)
        self.widget_17 = QtWidgets.QWidget(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.widget_17.setFont(font)
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_17)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.num9 = QtWidgets.QPushButton(self.widget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num9.sizePolicy().hasHeightForWidth())
        self.num9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num9.setFont(font)
        self.num9.setObjectName("num9")
        self.verticalLayout_15.addWidget(self.num9)
        self.verticalLayout_4.addWidget(self.widget_17)
        self.widget_18 = QtWidgets.QWidget(self.widget_3)
        self.widget_18.setMouseTracking(False)
        self.widget_18.setTabletTracking(False)
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_18)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.num6 = QtWidgets.QPushButton(self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num6.sizePolicy().hasHeightForWidth())
        self.num6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num6.setFont(font)
        self.num6.setObjectName("num6")
        self.verticalLayout_14.addWidget(self.num6)
        self.verticalLayout_4.addWidget(self.widget_18)
        self.widget_22 = QtWidgets.QWidget(self.widget_3)
        self.widget_22.setObjectName("widget_22")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_22)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.num3 = QtWidgets.QPushButton(self.widget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num3.sizePolicy().hasHeightForWidth())
        self.num3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num3.setFont(font)
        self.num3.setObjectName("num3")
        self.verticalLayout_13.addWidget(self.num3)
        self.verticalLayout_4.addWidget(self.widget_22)
        self.widget_19 = QtWidgets.QWidget(self.widget_3)
        self.widget_19.setObjectName("widget_19")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_19)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.coma = QtWidgets.QPushButton(self.widget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coma.sizePolicy().hasHeightForWidth())
        self.coma.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.coma.setFont(font)
        self.coma.setObjectName("coma")
        self.verticalLayout_12.addWidget(self.coma)
        self.verticalLayout_4.addWidget(self.widget_19)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.button)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_23 = QtWidgets.QWidget(self.widget_4)
        self.widget_23.setObjectName("widget_23")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_23)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.x_1 = QtWidgets.QPushButton(self.widget_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_1.sizePolicy().hasHeightForWidth())
        self.x_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.x_1.setFont(font)
        self.x_1.setObjectName("x_1")
        self.verticalLayout_11.addWidget(self.x_1)
        self.verticalLayout_6.addWidget(self.widget_23)
        self.widget_24 = QtWidgets.QWidget(self.widget_4)
        self.widget_24.setObjectName("widget_24")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_24)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.devide = QtWidgets.QPushButton(self.widget_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.devide.sizePolicy().hasHeightForWidth())
        self.devide.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.devide.setFont(font)
        self.devide.setObjectName("devide")
        self.verticalLayout_10.addWidget(self.devide)
        self.verticalLayout_6.addWidget(self.widget_24)
        self.widget_25 = QtWidgets.QWidget(self.widget_4)
        self.widget_25.setObjectName("widget_25")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_25)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.multyply = QtWidgets.QPushButton(self.widget_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multyply.sizePolicy().hasHeightForWidth())
        self.multyply.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.multyply.setFont(font)
        self.multyply.setObjectName("multyply")
        self.verticalLayout_9.addWidget(self.multyply)
        self.verticalLayout_6.addWidget(self.widget_25)
        self.widget_26 = QtWidgets.QWidget(self.widget_4)
        self.widget_26.setObjectName("widget_26")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_26)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.minus = QtWidgets.QPushButton(self.widget_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus.sizePolicy().hasHeightForWidth())
        self.minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.minus.setFont(font)
        self.minus.setObjectName("minus")
        self.verticalLayout_8.addWidget(self.minus)
        self.verticalLayout_6.addWidget(self.widget_26)
        self.widget_28 = QtWidgets.QWidget(self.widget_4)
        self.widget_28.setObjectName("widget_28")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_28)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plus = QtWidgets.QPushButton(self.widget_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus.sizePolicy().hasHeightForWidth())
        self.plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.plus.setFont(font)
        self.plus.setObjectName("plus")
        self.horizontalLayout_2.addWidget(self.plus)
        self.verticalLayout_6.addWidget(self.widget_28)
        self.widget_27 = QtWidgets.QWidget(self.widget_4)
        self.widget_27.setObjectName("widget_27")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_27)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.equal = QtWidgets.QPushButton(self.widget_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equal.sizePolicy().hasHeightForWidth())
        self.equal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.equal.setFont(font)
        self.equal.setObjectName("equal")
        self.verticalLayout_7.addWidget(self.equal)
        self.verticalLayout_6.addWidget(self.widget_27)
        self.horizontalLayout.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.button)
        Kalkulator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Kalkulator)
        QtCore.QMetaObject.connectSlotsByName(Kalkulator)

    def retranslateUi(self, Kalkulator):
        _translate = QtCore.QCoreApplication.translate
        Kalkulator.setWindowTitle(_translate("Kalkulator", "Kalkulator"))
        self.text.setText(_translate("Kalkulator", "TextLabel"))
        self.persent.setText(_translate("Kalkulator", "%"))
        self.Left_s.setText(_translate("Kalkulator", "("))
        self.Right_s.setText(_translate("Kalkulator", ")"))
        self.num7.setText(_translate("Kalkulator", "7"))
        self.num4.setText(_translate("Kalkulator", "4"))
        self.num1.setText(_translate("Kalkulator", "1"))
        self.plus_minus.setText(_translate("Kalkulator", "+-"))
        self.sqrt.setText(_translate("Kalkulator", "SQRT"))
        self.clear.setText(_translate("Kalkulator", "C"))
        self.num8.setText(_translate("Kalkulator", "8"))
        self.num5.setText(_translate("Kalkulator", "5"))
        self.num2.setText(_translate("Kalkulator", "2"))
        self.num0.setText(_translate("Kalkulator", "0"))
        self.pow.setText(_translate("Kalkulator", "POW"))
        self.back.setText(_translate("Kalkulator", "Back"))
        self.num9.setText(_translate("Kalkulator", "9"))
        self.num6.setText(_translate("Kalkulator", "6"))
        self.num3.setText(_translate("Kalkulator", "3"))
        self.coma.setText(_translate("Kalkulator", ","))
        self.x_1.setText(_translate("Kalkulator", "1/x"))
        self.devide.setText(_translate("Kalkulator", "/"))
        self.multyply.setText(_translate("Kalkulator", "*"))
        self.minus.setText(_translate("Kalkulator", "-"))
        self.plus.setText(_translate("Kalkulator", "+"))
        self.equal.setText(_translate("Kalkulator", "="))