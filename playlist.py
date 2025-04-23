from mutagen import MutagenError, File
from PyQt6.QtCore import QVariant, QAbstractTableModel, QModelIndex, Qt

class Playlist(QAbstractTableModel):
    def __init__(self, url, library_dir, columns = ["artist", "title", "album", "year"]):
        """
        `url` is the m3u file url to be processed.

        `columns` is a list of user-specified tags to sort the list by (title, artist, etc)
        """
        super().__init__()
        self.library_dir = library_dir
        self.columns = columns
        self.url = url
        self.track_url_list = self.parseM3UFile()
        self.tracks = self.getTrackTags()
        self.roles = self.roleNames()
            
    def parseM3UFile(self):
        playlist = []
        url = self.library_dir + "/" + self.url
        with open(url, 'r', encoding="utf-8") as file:
            playlist = [
                self.library_dir + '/' + line.strip("\n")
                for line in file
                if not line.startswith("#EXT")
            ]
        return playlist

    def getTrackTags(self):
        """Get a list of music file urls and return a dictlist of tags, or a list with a broken link tag, and the url"""
        tracks = []
        for p in self.track_url_list:
            try:
                tags = File(p, easy=True)
                tracks.append(tags)
            except MutagenError:
                tracks.append(p)
        return tracks

    # QAbstractTableModel virtual functions
    def rowCount(self, parent=QModelIndex()):
        return len(self.tracks)

    def columnCount(self, parent=QModelIndex()):
        return len(self.columns)

    # TODO
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return QVariant()
        
        row = index.row()
        column = index.column()
        
        if role == Qt.ItemDataRole.DisplayRole:
            key = self.columns[column]
            return self.tracks[row].get(key, "")
        
        return QVariant()