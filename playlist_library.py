import os
from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt
# TODO Add comments

class PlaylistLibrary(QAbstractListModel):
    def __init__(self, library_dir):
        super().__init__()
        self.library_dir = library_dir
        self.playlists = self.getFolderPlaylists()
        
    def getFolderPlaylists(self):
        playlists = [str]
        for dirpath, dirname, filename in os.walk(self.library_dir):
            for file in filename:
                if file.endswith(".m3u"):
                    playlists.append(dirpath + "/" + file)
        return playlists
    
    # QAbstractTableModel virtual functions
    def rowCount(self, parent=QModelIndex()):
        return len(self.playlists)
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        row = index.row()
        
        if role == Qt.ItemDataRole.DisplayRole:
            return self.playlists[row]