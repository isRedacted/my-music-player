import os
from PyQt6.QtCore import QAbstractListModel, QUrl

class PlaylistLibrary(QAbstractListModel):
    def __init__(self, library):
        super().__init__()
        self.library = library
        
    def getFolderPlaylists(self):
        playlists = [str]
        for dirpath, dirname, filename in os.walk(self.library):
            for file in filename:
                if file.endswith(".m3u"):
                    playlists.append(dirpath + "/" + file)
        return playlists