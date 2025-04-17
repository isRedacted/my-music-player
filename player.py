# Find it in the folder
# Send file name to QT multimedia to play that hibbledy dibbledy

from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtCore import QUrl

class Player(QMediaPlayer):
    def __init__(self):
        super().__init__()
        
    def newSong(self, url):
        self.setSource(QUrl(url))
        self.play()