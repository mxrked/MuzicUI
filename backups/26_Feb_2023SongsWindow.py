


from PyQt5 import QtCore, QtGui, QtWidgets
from assets.medias.qrc import gradient, music, colorful, care, holdme, morning
from assets.files.GLOBALS import allSongs, currentSong
from _backupFiles import backupAllFiles

import sys
import StartWindow, CurrentSongWindow


class Ui_SongsWindow(object):
    def setupUi(self, SongsWindow):

        ''' Functions '''
        def enterCurrentSongWindow():

            # Showing the Current Song Window
            self.window = QtWidgets.QMainWindow()
            self.ui = CurrentSongWindow.Ui_CurrentSongWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            # Hiding Songs Window
            SongsWindow.hide()

        def openCare():

            # Adding song
            currentSong.clear()
            currentSong.append(allSongs[0])

            enterCurrentSongWindow()

        def openColorful():

            # Adding song
            currentSong.clear()
            currentSong.append(allSongs[1])

            enterCurrentSongWindow()

        def openHoldMe():

            # Adding song
            currentSong.clear()
            currentSong.append(allSongs[2])

            enterCurrentSongWindow()

        def openMorning():

            # Adding song
            currentSong.clear()
            currentSong.append(allSongs[3])

            enterCurrentSongWindow()

        def exitApp():
            sys.exit()

        SongsWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        SongsWindow.setObjectName("SongsWindow")
        SongsWindow.resize(470, 750)
        SongsWindow.setMinimumSize(QtCore.QSize(470, 750))
        SongsWindow.setMaximumSize(QtCore.QSize(470, 750))
        SongsWindow.setStyleSheet("border-image: url(:/newPrefix/images/gradient.png);")
        self.centralwidget = QtWidgets.QWidget(SongsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.songsWindow_ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.songsWindow_ExitBtn.setGeometry(QtCore.QRect(20, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.songsWindow_ExitBtn.setFont(font)
        self.songsWindow_ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.songsWindow_ExitBtn.clicked.connect(exitApp)
        self.songsWindow_ExitBtn.setStyleSheet("QPushButton {\n"
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
        self.songsWindow_ExitBtn.setObjectName("songsWindow_ExitBtn")
        self.songsWindow_SongsHolderFrame = QtWidgets.QFrame(self.centralwidget)
        self.songsWindow_SongsHolderFrame.setGeometry(QtCore.QRect(20, 80, 431, 651))
        self.songsWindow_SongsHolderFrame.setStyleSheet("QFrame {\n"
"    border-image: none;\n"
"    background-color: ghostwhite;\n"
"    border-radius: 5px;\n"
"}")
        self.songsWindow_SongsHolderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.songsWindow_SongsHolderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.songsWindow_SongsHolderFrame.setObjectName("songsWindow_SongsHolderFrame")
        self.songsWindow_CareImgLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_CareImgLabel.setGeometry(QtCore.QRect(50, 40, 141, 131))
        self.songsWindow_CareImgLabel.setAutoFillBackground(False)
        self.songsWindow_CareImgLabel.setStyleSheet("QLabel {\n"
"    border-radius: 5px;\n"
"}")
        self.songsWindow_CareImgLabel.setText("")
        self.songsWindow_CareImgLabel.setPixmap(QtGui.QPixmap(":/newPrefix/images/mixaund-care.jpg"))
        self.songsWindow_CareImgLabel.setScaledContents(True)
        self.songsWindow_CareImgLabel.setObjectName("songsWindow_CareImgLabel")
        self.songsWindow_CareArtistLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_CareArtistLabel.setGeometry(QtCore.QRect(50, 190, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.songsWindow_CareArtistLabel.setFont(font)
        self.songsWindow_CareArtistLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songsWindow_CareArtistLabel.setObjectName("songsWindow_CareArtistLabel")
        self.songsWindow_CareLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_CareLabel.setGeometry(QtCore.QRect(50, 220, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.songsWindow_CareLabel.setFont(font)
        self.songsWindow_CareLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songsWindow_CareLabel.setObjectName("songsWindow_CareLabel")
        self.songsWindow_CareListenBtn = QtWidgets.QPushButton(self.songsWindow_SongsHolderFrame)
        self.songsWindow_CareListenBtn.clicked.connect(openCare)
        self.songsWindow_CareListenBtn.setGeometry(QtCore.QRect(80, 260, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.songsWindow_CareListenBtn.setFont(font)
        self.songsWindow_CareListenBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.songsWindow_CareListenBtn.setStyleSheet("QPushButton {\n"
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
        self.songsWindow_CareListenBtn.setObjectName("songsWindow_CareListenBtn")
        self.songsWindow_HoldMeListenBtn = QtWidgets.QPushButton(self.songsWindow_SongsHolderFrame)
        self.songsWindow_HoldMeListenBtn.clicked.connect(openHoldMe)
        self.songsWindow_HoldMeListenBtn.setGeometry(QtCore.QRect(270, 260, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.songsWindow_HoldMeListenBtn.setFont(font)
        self.songsWindow_HoldMeListenBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.songsWindow_HoldMeListenBtn.setStyleSheet("QPushButton {\n"
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
        self.songsWindow_HoldMeListenBtn.setObjectName("songsWindow_HoldMeListenBtn")
        self.songsWindow_HoldMeImgLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_HoldMeImgLabel.setGeometry(QtCore.QRect(240, 40, 141, 131))
        self.songsWindow_HoldMeImgLabel.setAutoFillBackground(False)
        self.songsWindow_HoldMeImgLabel.setStyleSheet("QLabel {\n"
"    border-radius: 5px;\n"
"}")
        self.songsWindow_HoldMeImgLabel.setText("")
        self.songsWindow_HoldMeImgLabel.setPixmap(QtGui.QPixmap(":/newPrefix/images/purrple-cat-please-hold-me.jpg"))
        self.songsWindow_HoldMeImgLabel.setScaledContents(True)
        self.songsWindow_HoldMeImgLabel.setObjectName("songsWindow_HoldMeImgLabel")
        self.songsWindow_HoldMeLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_HoldMeLabel.setGeometry(QtCore.QRect(240, 220, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.songsWindow_HoldMeLabel.setFont(font)
        self.songsWindow_HoldMeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songsWindow_HoldMeLabel.setObjectName("songsWindow_HoldMeLabel")
        self.songsWindow_HoldMeArtistLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_HoldMeArtistLabel.setGeometry(QtCore.QRect(240, 190, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.songsWindow_HoldMeArtistLabel.setFont(font)
        self.songsWindow_HoldMeArtistLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songsWindow_HoldMeArtistLabel.setObjectName("songsWindow_HoldMeArtistLabel")
        self.songsWindow_MorningLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_MorningLabel.setGeometry(QtCore.QRect(50, 530, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.songsWindow_MorningLabel.setFont(font)
        self.songsWindow_MorningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songsWindow_MorningLabel.setObjectName("songsWindow_MorningLabel")
        self.songsWindow_MorningImgLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_MorningImgLabel.setGeometry(QtCore.QRect(50, 350, 141, 131))
        self.songsWindow_MorningImgLabel.setAutoFillBackground(False)
        self.songsWindow_MorningImgLabel.setStyleSheet("QLabel {\n"
"    border-radius: 5px;\n"
"}")
        self.songsWindow_MorningImgLabel.setText("")
        self.songsWindow_MorningImgLabel.setPixmap(QtGui.QPixmap(":/newPrefix/images/qlowdy-morning.jpg"))
        self.songsWindow_MorningImgLabel.setScaledContents(True)
        self.songsWindow_MorningImgLabel.setObjectName("songsWindow_MorningImgLabel")
        self.songsWindow_MorningArtistLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_MorningArtistLabel.setGeometry(QtCore.QRect(50, 500, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.songsWindow_MorningArtistLabel.setFont(font)
        self.songsWindow_MorningArtistLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songsWindow_MorningArtistLabel.setObjectName("songsWindow_MorningArtistLabel")
        self.songsWindow_MorningListenBtn = QtWidgets.QPushButton(self.songsWindow_SongsHolderFrame)
        self.songsWindow_MorningListenBtn.setGeometry(QtCore.QRect(80, 570, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.songsWindow_MorningListenBtn.setFont(font)
        self.songsWindow_MorningListenBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.songsWindow_MorningListenBtn.clicked.connect(openMorning)
        self.songsWindow_MorningListenBtn.setStyleSheet("QPushButton {\n"
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
        self.songsWindow_MorningListenBtn.setObjectName("songsWindow_MorningListenBtn")
        self.songsWindow_ColorfulLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_ColorfulLabel.setGeometry(QtCore.QRect(230, 530, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.songsWindow_ColorfulLabel.setFont(font)
        self.songsWindow_ColorfulLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songsWindow_ColorfulLabel.setObjectName("songsWindow_ColorfulLabel")
        self.songsWindow_ColorfulImgLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_ColorfulImgLabel.setGeometry(QtCore.QRect(230, 350, 141, 131))
        self.songsWindow_ColorfulImgLabel.setAutoFillBackground(False)
        self.songsWindow_ColorfulImgLabel.setStyleSheet("QLabel {\n"
"    border-radius: 5px;\n"
"}")
        self.songsWindow_ColorfulImgLabel.setText("")
        self.songsWindow_ColorfulImgLabel.setPixmap(QtGui.QPixmap(":/newPrefix/images/roa-music-colorful.jpg"))
        self.songsWindow_ColorfulImgLabel.setScaledContents(True)
        self.songsWindow_ColorfulImgLabel.setObjectName("songsWindow_ColorfulImgLabel")
        self.songsWindow_ColorfulArtistLabel = QtWidgets.QLabel(self.songsWindow_SongsHolderFrame)
        self.songsWindow_ColorfulArtistLabel.setGeometry(QtCore.QRect(230, 500, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.songsWindow_ColorfulArtistLabel.setFont(font)
        self.songsWindow_ColorfulArtistLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songsWindow_ColorfulArtistLabel.setObjectName("songsWindow_ColorfulArtistLabel")
        self.songsWindow_ColorfulListenBtn = QtWidgets.QPushButton(self.songsWindow_SongsHolderFrame)
        self.songsWindow_ColorfulListenBtn.clicked.connect(openColorful)
        self.songsWindow_ColorfulListenBtn.setGeometry(QtCore.QRect(260, 570, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.songsWindow_ColorfulListenBtn.setFont(font)
        self.songsWindow_ColorfulListenBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.songsWindow_ColorfulListenBtn.setStyleSheet("QPushButton {\n"
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
        self.songsWindow_ColorfulListenBtn.setObjectName("songsWindow_ColorfulListenBtn")
        SongsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SongsWindow)
        QtCore.QMetaObject.connectSlotsByName(SongsWindow)

    def retranslateUi(self, SongsWindow):
        _translate = QtCore.QCoreApplication.translate
        SongsWindow.setWindowTitle(_translate("SongsWindow", "MuzicUI - Songs"))
        self.songsWindow_ExitBtn.setText(_translate("SongsWindow", "EXIT"))
        self.songsWindow_CareArtistLabel.setText(_translate("SongsWindow", "Mixaund"))
        self.songsWindow_CareLabel.setText(_translate("SongsWindow", "Care"))
        self.songsWindow_CareListenBtn.setText(_translate("SongsWindow", "LISTEN"))
        self.songsWindow_HoldMeListenBtn.setText(_translate("SongsWindow", "LISTEN"))
        self.songsWindow_HoldMeLabel.setText(_translate("SongsWindow", "Hold Me"))
        self.songsWindow_HoldMeArtistLabel.setText(_translate("SongsWindow", "Purple Cat"))
        self.songsWindow_MorningLabel.setText(_translate("SongsWindow", "Morning"))
        self.songsWindow_MorningArtistLabel.setText(_translate("SongsWindow", "Qlowdy"))
        self.songsWindow_MorningListenBtn.setText(_translate("SongsWindow", "LISTEN"))
        self.songsWindow_ColorfulLabel.setText(_translate("SongsWindow", "Colorful"))
        self.songsWindow_ColorfulArtistLabel.setText(_translate("SongsWindow", "Roa-Music"))
        self.songsWindow_ColorfulListenBtn.setText(_translate("SongsWindow", "LISTEN"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SongsWindow = QtWidgets.QMainWindow()
    ui = Ui_SongsWindow()
    ui.setupUi(SongsWindow)

    backupAllFiles()

    print("Run app via StartWindow.py ....")

    sys.exit()
