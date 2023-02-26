import os

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from assets.medias.qrc import gradient
from assets.files.GLOBALS import currentSong
from _backupFiles import backupAllFiles

import sys
import SongsWindow

class Ui_CurrentSongWindow(object):
    def setupUi(self, CurrentSongWindow):


        self.player = QtMultimedia.QMediaPlayer()

        ''' Functions '''
        def enterSongsWindow():

            # Showing the Songs Window
            self.window = QtWidgets.QMainWindow()
            self.ui = SongsWindow.Ui_SongsWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            self.player.pause()

            # Hiding Current Song Window
            CurrentSongWindow.hide()

        def playSong():

            self.currentSongWindow_CurrentSongPlayBtn.setDisabled(True)
            self.currentSongWindow_CurrentSongPauseBtn.setDisabled(False)

            self.currentSongWindow_CurrentSongPlayBtn.setStyleSheet("background-color: rgba(0,0,0,.05); color: white; border: none; border-radius: 5px; border-image: none;")
            self.currentSongWindow_CurrentSongPauseBtn.setStyleSheet("background-color: #3F0071; color: white; border: none; border-radius: 5px; border-image: none;")

            print("Playing: " + currentSong[0].getName())

            song = os.path.join(os.getcwd(), currentSong[0].getSong())
            url = QtCore.QUrl.fromLocalFile(song)
            mediaContent = QtMultimedia.QMediaContent(url)

            self.player.setMedia(mediaContent)
            self.player.play()

        def pauseSong():
            print("Paused: " + currentSong[0].getName())

            self.currentSongWindow_CurrentSongPlayBtn.setDisabled(False)
            self.currentSongWindow_CurrentSongPauseBtn.setDisabled(True)

            self.currentSongWindow_CurrentSongPlayBtn.setStyleSheet("background-color: #3F0071; color: white; border: none; border-radius: 5px; border-image: none;")
            self.currentSongWindow_CurrentSongPauseBtn.setStyleSheet("background-color: rgba(0,0,0,.05); color: white; border: none; border-radius: 5px; border-image: none;")

            self.player.pause()

        def exitApp():
            sys.exit()


        CurrentSongWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        CurrentSongWindow.setObjectName("CurrentSongWindow")
        CurrentSongWindow.resize(600, 485)
        CurrentSongWindow.setMinimumSize(QtCore.QSize(600, 485))
        CurrentSongWindow.setMaximumSize(QtCore.QSize(600, 485))
        CurrentSongWindow.setStyleSheet("border-image: url(:/newPrefix/images/gradient.png);")
        self.centralwidget = QtWidgets.QWidget(CurrentSongWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.currentSongWindow_SongsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.currentSongWindow_SongsBtn.setGeometry(QtCore.QRect(20, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.currentSongWindow_SongsBtn.setFont(font)
        self.currentSongWindow_SongsBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.currentSongWindow_SongsBtn.clicked.connect(enterSongsWindow)
        self.currentSongWindow_SongsBtn.setStyleSheet("QPushButton {\n"
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
        self.currentSongWindow_SongsBtn.setObjectName("currentSongWindow_SongsBtn")
        self.currentSongWindow_ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.currentSongWindow_ExitBtn.clicked.connect(exitApp)
        self.currentSongWindow_ExitBtn.setGeometry(QtCore.QRect(110, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.currentSongWindow_ExitBtn.setFont(font)
        self.currentSongWindow_ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.currentSongWindow_ExitBtn.setStyleSheet("QPushButton {\n"
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
        self.currentSongWindow_ExitBtn.setObjectName("currentSongWindow_ExitBtn")
        self.currentSongWindow_CurrentSongImgLabel = QtWidgets.QLabel(self.centralwidget)

        # Making sure that a current song is selected
        if len(currentSong) > 0:
            # Adding pixmap to label
            self.currentSong_Pixmap = QtGui.QPixmap(currentSong[0].getImg())
            self.currentSongWindow_CurrentSongImgLabel.setPixmap(self.currentSong_Pixmap)

        self.currentSongWindow_CurrentSongImgLabel.setGeometry(QtCore.QRect(240, 110, 131, 121))
        self.currentSongWindow_CurrentSongImgLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background-color: ghostwhite;\n"
"}")
        self.currentSongWindow_CurrentSongImgLabel.setText("")
        self.currentSongWindow_CurrentSongImgLabel.setObjectName("currentSongWindow_CurrentSongImgLabel")
        self.currentSongWindow_CurrentSongArtistLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentSongWindow_CurrentSongArtistLabel.setGeometry(QtCore.QRect(200, 250, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.currentSongWindow_CurrentSongArtistLabel.setFont(font)
        self.currentSongWindow_CurrentSongArtistLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.currentSongWindow_CurrentSongArtistLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentSongWindow_CurrentSongArtistLabel.setObjectName("currentSongWindow_CurrentSongArtistLabel")
        self.currentSongWindow_CurrentSongLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentSongWindow_CurrentSongLabel.setGeometry(QtCore.QRect(200, 290, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.currentSongWindow_CurrentSongLabel.setFont(font)
        self.currentSongWindow_CurrentSongLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.currentSongWindow_CurrentSongLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentSongWindow_CurrentSongLabel.setObjectName("currentSongWindow_CurrentSongLabel")
        # self.currentSongWindow_CurrentSongSlider = QtWidgets.QSlider(self.centralwidget)
        # self.currentSongWindow_CurrentSongSlider.setGeometry(QtCore.QRect(170, 340, 271, 22))
        # self.currentSongWindow_CurrentSongSlider.setStyleSheet("border-image: none;")
        # self.currentSongWindow_CurrentSongSlider.setOrientation(QtCore.Qt.Horizontal)
        # self.currentSongWindow_CurrentSongSlider.setObjectName("currentSongWindow_CurrentSongSlider")
        self.currentSongWindow_CurrentSongPlayBtn = QtWidgets.QPushButton(self.centralwidget)
        self.currentSongWindow_CurrentSongPlayBtn.clicked.connect(playSong)
        self.currentSongWindow_CurrentSongPlayBtn.setGeometry(QtCore.QRect(250, 380, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.currentSongWindow_CurrentSongPlayBtn.setFont(font)
        self.currentSongWindow_CurrentSongPlayBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.currentSongWindow_CurrentSongPlayBtn.setStyleSheet("QPushButton {\n"
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
        self.currentSongWindow_CurrentSongPlayBtn.setObjectName("currentSongWindow_CurrentSongPlayBtn")
        self.currentSongWindow_CurrentSongPauseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.currentSongWindow_CurrentSongPauseBtn.setDisabled(True)
        self.currentSongWindow_CurrentSongPauseBtn.clicked.connect(pauseSong)
        self.currentSongWindow_CurrentSongPauseBtn.setGeometry(QtCore.QRect(310, 380, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentSongWindow_CurrentSongPauseBtn.setFont(font)
        self.currentSongWindow_CurrentSongPauseBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.currentSongWindow_CurrentSongPauseBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: white;\n"
"    background-color: rgba(0,0,0,.05);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #9900F0;\n"
"}")
        self.currentSongWindow_CurrentSongPauseBtn.setObjectName("currentSongWindow_CurrentSongPauseBtn")
        CurrentSongWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(CurrentSongWindow)
        QtCore.QMetaObject.connectSlotsByName(CurrentSongWindow)

    def retranslateUi(self, CurrentSongWindow):
        _translate = QtCore.QCoreApplication.translate
        CurrentSongWindow.setWindowTitle(_translate("CurrentSongWindow", "Muzic - Current Song"))
        self.currentSongWindow_SongsBtn.setText(_translate("CurrentSongWindow", "SONGS"))
        self.currentSongWindow_ExitBtn.setText(_translate("CurrentSongWindow", "EXIT"))

        # Making sure that a current song is selected
        if len(currentSong) > 0:
            self.currentSongWindow_CurrentSongArtistLabel.setText(_translate("CurrentSongWindow", str(currentSong[0].getArtist())))
            self.currentSongWindow_CurrentSongLabel.setText(_translate("CurrentSongWindow",  str(currentSong[0].getName())))

        self.currentSongWindow_CurrentSongPlayBtn.setText(_translate("CurrentSongWindow", "▶"))
        self.currentSongWindow_CurrentSongPauseBtn.setText(_translate("CurrentSongWindow", "||"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentSongWindow = QtWidgets.QMainWindow()
    ui = Ui_CurrentSongWindow()
    ui.setupUi(CurrentSongWindow)

    # backupAllFiles()

    print("Run app via StartWindow.py ....")

    sys.exit()
