from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot

# Send/receive play/pause state
# Send/receive mute state
# Send/receive song progress state

class Bridge(QObject):
    
    
    # Signals to QML
    toQml = pyqtSignal(str)
    
    # Init
    def __init__(self):
        super().__init__()
    
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
        print("Play/pause button pressed")
        
    @pyqtSlot()
    def nextButton(self):
        print("Play/pause button pressed")