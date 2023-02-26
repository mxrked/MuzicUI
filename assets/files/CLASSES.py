from assets.medias.qrc import care, colorful, holdme, morning

class Song:

    def __init__(self, name, artist, img, song):
        self.__name = name
        self.__artist = artist
        self.__img = img
        self.__song = song

    def setName(self, name):
        self.__name = name
    def setArtist(self, artist):
        self.__artist = artist
    def setImg(self, img):
        self.__img = img
    def setSong(self, song):
        self.__song = song

    def getName(self):
        return self.__name
    def getArtist(self):
        return self.__artist
    def getImg(self):
        return self.__img
    def getSong(self):
        return self.__song



careSong = Song("Care", "Mixaund", "assets/medias/images/mixaund-care.jpg", "assets/medias/music/mixaund-care.mp3")
colorfulSong = Song("Colorful", "Roa-Music", "assets/medias/images/roa-music-colorful.jpg", "assets/medias/music/roa-music-colorful.mp3")
holdMeSong = Song("Hold Me", "Purple Cat", "assets/medias/images/purrple-cat-please-hold-me.jpg", "assets/medias/music/purple-cat-please-hold-me.mp3")
morningSong = Song("Morning", "Qlowdy", "assets/medias/images/qlowdy-morning.jpg", "assets/medias/music/qlowdy-morning.mp3")
