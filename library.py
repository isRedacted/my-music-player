from PyQt6.QtCore import QAbstractTableModel
import mutagen

class Library(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        
    def getLibraryTracks(url):
        # Get all tracks with tags at library url