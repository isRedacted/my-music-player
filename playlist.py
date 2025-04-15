# Add error checking for missing file
from PyQt6.QtCore import QAbstractTableModel
from m3u_parser import M3uParser

class PlaylistTableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data_list = data
        m3u_parser = M3uParser()
        
    def parseM3UData(url):
        