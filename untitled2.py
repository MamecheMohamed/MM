# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import img
class Ui_emotions(object):
    def setupUi(self, emotions):
        emotions.setObjectName("emotions")
        emotions.resize(761, 432)
        self.centralwidget = QtWidgets.QWidget(emotions)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 761, 411))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("position: absolute;\n"
"width: 644px;\n"
"height: 513px;\n"
"\n"
"background: #FFFFFF;\n"
"backdrop-filter: blur(4px);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 761, 41))
        self.widget.setStyleSheet("position: absolute;\n"
"width: 644px;\n"
"height: 31px;\n"
"left: 0px;\n"
"top: 30px;\n"
"\n"
"background: #2B5B8B;")
        self.widget.setObjectName("widget")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 51, 41))
        self.toolButton.setStyleSheet("border:none;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-list-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(25, 25))
        self.toolButton.setObjectName("toolButton")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(0, 309, 51, 101))
        self.widget_2.setStyleSheet("position: absolute;\n"
"width: 45px;\n"
"height: 110px;\n"
"left: 0px;\n"
"top: 403px;\n"
"\n"
"background: #031B34;\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setGeometry(QtCore.QRect(0, 40, 51, 271))
        self.widget_3.setStyleSheet("position: absolute;\n"
"width: 45px;\n"
"height: 452px;\n"
"left: 0px;\n"
"top: 61px;\n"
"\n"
"background: #063667;")
        self.widget_3.setObjectName("widget_3")
        self.toolButton_2 = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_2.setGeometry(QtCore.QRect(0, 20, 51, 31))
        self.toolButton_2.setStyleSheet("border:none;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("56440222_308193143158283_1138451021052248064_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_3.setGeometry(QtCore.QRect(0, 60, 51, 31))
        self.toolButton_3.setStyleSheet("border:none;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("56408500_1076002912607597_6883167661480476672_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_4.setGeometry(QtCore.QRect(0, 100, 51, 31))
        self.toolButton_4.setStyleSheet("border:none;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("56178502_2285227635098872_8815854441614802944_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_5.setGeometry(QtCore.QRect(0, 140, 51, 31))
        self.toolButton_5.setStyleSheet("border:none;\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("56237491_264594491117454_6294432180407894016_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_6.setGeometry(QtCore.QRect(0, 180, 51, 31))
        self.toolButton_6.setStyleSheet("border:none;\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("56589696_2090984727686960_8305382584754372608_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_7.setGeometry(QtCore.QRect(0, 220, 51, 31))
        self.toolButton_7.setStyleSheet("border:none;\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("56619860_2408290069182223_4179440299304550400_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon6)
        self.toolButton_7.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_7.setObjectName("toolButton_7")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, 50, 281, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Webp.net-resizeimage222.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 340, 641, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        emotions.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(emotions)
        self.statusbar.setObjectName("statusbar")
        emotions.setStatusBar(self.statusbar)

        self.retranslateUi(emotions)
        QtCore.QMetaObject.connectSlotsByName(emotions)

    def retranslateUi(self, emotions):
        _translate = QtCore.QCoreApplication.translate
        emotions.setWindowTitle(_translate("emotions", "MainWindow"))
        self.toolButton.setText(_translate("emotions", "..."))
        self.toolButton_2.setText(_translate("emotions", "..."))
        self.toolButton_3.setText(_translate("emotions", "..."))
        self.toolButton_4.setText(_translate("emotions", "..."))
        self.toolButton_5.setText(_translate("emotions", "..."))
        self.toolButton_6.setText(_translate("emotions", "..."))
        self.toolButton_7.setText(_translate("emotions", "..."))
        self.label_2.setText(_translate("emotions", "Cette fonctionnalité est en construction, suivez nous pour mise à jour !"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    emotions = QtWidgets.QMainWindow()
    ui = Ui_emotions()
    ui.setupUi(emotions)
    emotions.show()
    sys.exit(app.exec_())

