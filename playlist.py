# Add error checking for missing file
import os
import mutagen
from PyQt6.QtCore import QUrl, QAbstractTableModel, QModelIndex, Qt
from charset_normalizer import from_path

class Playlist(QAbstractTableModel):
    # Playlist is the m3u file url to be processed, columns is a list of user-specified tags to sort the list by (title, artist, etc), and the library directory
    def __init__(self, playlist, columns, library):
        super().__init__()
        self.library = library
        self.playlist = self.parseM3UData(playlist, library)
        self.columns = columns
        self.tracks = self.getPlaylistTags(self.playlist)

    def parseM3UData(self, url, library):
        playlist = []
        qurl = QUrl(url).url()
        print(str(from_path(url)))
        with open(qurl, 'r') as file:
            for line in file.readlines():
                if line.startswith("#EXT"):
                    continue
                elif os.path.exists(line):
                    playlist.append(line.strip('\n'))
                else:
                    playlist.append(library + "/" + line.strip('\n'))
                    print(line.strip('\n'))
        return playlist

    # Return a list of mutagen FileType objects
    def getPlaylistTags(self, playlist):
        tracks = []
        for t in playlist:
            try:
                tracks.append(mutagen.File(t))
            except(mutagen.MutagenError):
                tracks.append(["BROKEN LINK", t])
        return tracks

    # QAbstractTableModel virtual functions
    def rowCount(self, parent=QModelIndex()):
        return len(self.tracks)

    def columnCount(self, parent=QModelIndex()):
        return len(self.columns)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        row = index.row()
        column = index.column()
        return self.tracks[row][column]