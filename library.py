from PyQt6.QtCore import QAbstractTableModel
import mutagen

class Library(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        
    def getLibraryTracks(url):
        # Get all tracks with tags at library url
        library = []
        try:
            print("Get file tags with mutagen and add to library")
        except(mutagen.MutagenError):
            print("Not a file with valid tags, skipping")