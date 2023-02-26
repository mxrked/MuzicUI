


from PyQt5 import QtCore, QtGui, QtWidgets
from assets.medias.qrc import gradient, music
from _backupFiles import backupAllFiles

import sys
import SongsWindow

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):

        ''' Functions '''
        def enterSongsWindow():

            # Showing the Songs Window
            self.window = QtWidgets.QMainWindow()
            self.ui = SongsWindow.Ui_SongsWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            # Hiding Start Window
            StartWindow.hide()

        def exitApp():
            sys.exit()

        StartWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(800, 650)
        StartWindow.setMinimumSize(QtCore.QSize(800, 650))
        StartWindow.setMaximumSize(QtCore.QSize(800, 650))
        StartWindow.setStyleSheet("border-image: url(:/newPrefix/images/gradient.png);")
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startWindow_MainHeadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_MainHeadingLabel.setGeometry(QtCore.QRect(-50, 130, 901, 101))
        font = QtGui.QFont()
        font.setFamily("Metropolis Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_MainHeadingLabel.setFont(font)
        self.startWindow_MainHeadingLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.startWindow_MainHeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_MainHeadingLabel.setObjectName("startWindow_MainHeadingLabel")
        self.startWindow_IconLabel = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_IconLabel.setGeometry(QtCore.QRect(360, 250, 91, 91))
        self.startWindow_IconLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"}")
        self.startWindow_IconLabel.setText("")
        self.startWindow_IconLabel.setPixmap(QtGui.QPixmap(":/newPrefix/images/music.png"))
        self.startWindow_IconLabel.setScaledContents(True)
        self.startWindow_IconLabel.setObjectName("startWindow_IconLabel")
        self.startWindow_SubHeadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_SubHeadingLabel.setGeometry(QtCore.QRect(-50, 360, 901, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_SubHeadingLabel.setFont(font)
        self.startWindow_SubHeadingLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.startWindow_SubHeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_SubHeadingLabel.setObjectName("startWindow_SubHeadingLabel")
        self.startWindow_EnterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startWindow_EnterBtn.setGeometry(QtCore.QRect(314, 470, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_EnterBtn.setFont(font)
        self.startWindow_EnterBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startWindow_EnterBtn.clicked.connect(enterSongsWindow)
        self.startWindow_EnterBtn.setStyleSheet("QPushButton {\n"
"    padding-top: 4px;\n"
"    border-image: none;\n"
"    color: white;\n"
"    background-color: #3F0071;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #9900F0;\n"
"}")
        self.startWindow_EnterBtn.setObjectName("startWindow_EnterBtn")
        self.startWindow_ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startWindow_ExitBtn.setGeometry(QtCore.QRect(414, 470, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_ExitBtn.setFont(font)
        self.startWindow_ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startWindow_ExitBtn.clicked.connect(exitApp)
        self.startWindow_ExitBtn.setStyleSheet("QPushButton {\n"
"    padding-top: 4px;\n"
"    border-image: none;\n"
"    color: white;\n"
"    background-color: #3F0071;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #9900F0;\n"
"}")
        self.startWindow_ExitBtn.setObjectName("startWindow_ExitBtn")
        self.startWindow_BottomLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_BottomLabel1.setGeometry(QtCore.QRect(20, 600, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        self.startWindow_BottomLabel1.setFont(font)
        self.startWindow_BottomLabel1.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color:rgba(255, 255, 255, 155)\n"
"}")
        self.startWindow_BottomLabel1.setObjectName("startWindow_BottomLabel1")
        self.startWindow_BottomLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_BottomLabel2.setGeometry(QtCore.QRect(20, 620, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        self.startWindow_BottomLabel2.setFont(font)
        self.startWindow_BottomLabel2.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color:rgba(255, 255, 255, 155)\n"
"}")
        self.startWindow_BottomLabel2.setObjectName("startWindow_BottomLabel2")
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "MuzicUI - Start"))
        self.startWindow_MainHeadingLabel.setText(_translate("StartWindow", "Muzic.UI"))
        self.startWindow_SubHeadingLabel.setText(_translate("StartWindow", "MP3 Music Player"))
        self.startWindow_EnterBtn.setText(_translate("StartWindow", "ENTER"))
        self.startWindow_ExitBtn.setText(_translate("StartWindow", "EXIT"))
        self.startWindow_BottomLabel1.setText(_translate("StartWindow", "Made in PyQt5"))
        self.startWindow_BottomLabel2.setText(_translate("StartWindow", "By Parker Phelps"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()

    # backupAllFiles()

    sys.exit(app.exec_())
