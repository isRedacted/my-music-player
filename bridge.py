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
    @pyqtSlot(str)
    def fromQml(self, msg):
        print("Receive {msg}")
        self.toQml.emit("Echo {msg}")