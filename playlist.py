# Add error checking for missing file
from PyQt6.QtCore import QAbstractTableModel, QUrl

class Playlist(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def parseM3UData(self, url):
        playlist = []
        qurl = QUrl(url).url()
        with open(qurl, 'r') as file:
            for line in file.readlines():
                if line.startswith("#EXT"):
                    continue
                else:
                    playlist.append(line)
        return playlist