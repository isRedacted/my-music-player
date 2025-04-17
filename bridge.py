from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot

from player import Player

# Send/receive play/pause state
# Send/receive mute state
# Send/receive song progress state

class Bridge(QObject):   
    # Init
    def __init__(self):
        super().__init__()
        self.player = Player()

    # Signals to QML
    toQml = pyqtSignal(str)
    
    # Signals from PyQt
    # Player controls
    @pyqtSlot(str)
    def fromQml(self, msg):
        print("Receive {msg}")
        self.toQml.emit("Echo {msg}")
    
    @pyqtSlot()
    def previousButton(self):
        print("Previous button pressed")
        
    @pyqtSlot()
    def playPause(self):
        self.player.play()
        
    @pyqtSlot()
    def nextButton(self):
        print("Play/pause button pressed")