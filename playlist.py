from mutagen import MutagenError, File
from PyQt6.QtCore import QUrl, QAbstractTableModel, QModelIndex, Qt

class Playlist(QAbstractTableModel):
    def __init__(self, url: QUrl, library: str, columns = ["artist", "title", "album"]):
        """
        `url` is the m3u file url to be processed.

        `columns` is a list of user-specified tags to sort the list by (title, artist, etc)
        """
        super().__init__()
        self.library = library
        self.track_url_list = self.parseM3UFile(url)
        self.columns = columns
        self.tracks = self.getPlaylistTags(self.track_url_list)

    def parseM3UFile(self, url: QUrl):
        playlist = []
        with open(url.toString(), 'r', encoding="utf-8") as file:
            playlist = [
                self.library + '\\' + line.strip("\n")
                for line in file
                if not line.startswith("#EXT")
            ]
        return playlist

    def getPlaylistTags(self, playlist: list[str]):
        """Get a list of music file urls and return a dictlist of tags, or a list with a broken link tag, and the url"""
        tracks = []
        for p in playlist:
            try:
                tags = File(p, easy=True)
                tracks.append([tags, p])
            except MutagenError:
                tracks.append(["BROKEN LINK", p])
        return tracks

    # QAbstractTableModel virtual functions
    def rowCount(self, parent=QModelIndex()):
        return len(self.tracks)

    def columnCount(self, parent=QModelIndex()):
        return len(self.columns)

    # TODO
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        row = index.row()
        column = index.column()
        return self.tracks[row][column]
