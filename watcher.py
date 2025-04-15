# Watch folder in thread using threading to run it at the same time
# Maybe add option to not use if scan on startup preferred
import threading

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LibraryFolderWatcher(FileSystemEventHandler):
    def __init__(self):
    
    def startWatching(self):
        self.observer.schedule(self.event_handler, self.folder_path, recursive=True)
        threading.Thread(target=self.observer.start, daemon=True).start()