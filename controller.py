from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl

from player import Player
from playlist import Playlist
from playlist_library import PlaylistLibrary


class Controller(QObject):
    # Init (With saved playlist and saved columns)
    # TODO Implement overloading for last_playlist and columns
    def __init__(self, library_dir, last_playlist=None, columns=None):
        super().__init__()
        self.library_dir = library_dir
        self.player = Player()
        self.playlist_library = PlaylistLibrary(library_dir)
        if (last_playlist != None):
            self.playlist = Playlist(last_playlist, library_dir, columns)

    # Signals to QML
    toQml = pyqtSignal(str)

    # Signals from PyQt

    # Playlist controls
    @pyqtSlot(str)
    def setPlaylist(self, url):
        track_url_list = self.playlist.parseM3UFile(url)
        self.playlist.track_url_list = track_url_list
        self.playlist.tracks = self.playlist.getTrackTags(track_url_list)

    # Player controls
    @pyqtSlot(str)
    def fromQml(self, msg):
        print("Receive {msg}")
        self.toQml.emit("Echo {msg}")

    @pyqtSlot()
    def previousButton(self):
        print("Previous button pressed")

    @pyqtSlot()
    def playPause(self):
        self.player.play()

    @pyqtSlot()
    def nextButton(self):
        print("Play/pause button pressed")

    @pyqtSlot()
    def seek(self, pos):
        self.player.setPosition(pos)

    @pyqtSlot()
    def newSong(self, track):
        self.player.newSong(track)
