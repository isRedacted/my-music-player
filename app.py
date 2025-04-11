import os
import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QFileDialog, QApplication

from bridge import Bridge

app = QGuiApplication(sys.argv)
dialogApp = QApplication(sys.argv)

engine = QQmlApplicationEngine()

# Set settings file and check for library path
path = os.path.dirname(os.path.abspath(__file__))
settings = QSettings(os.path.join(path, "settings.ini"), QSettings.Format.IniFormat)

if not settings.contains("library_dir") or not os.path.exists(settings.value("library_dir")):
    library_dialog = QFileDialog()
    library_dialog.setFileMode(QFileDialog.FileMode.Directory)
    library_dir = library_dialog.getExistingDirectory(None, "Select music library folder", os.path.join(os.path.expanduser("~"), "Music"))
    
    if library_dir:
        settings.setValue("library_dir", library_dir)
    else:
        sys.exit()

# Bridge between QML frontend and PyQt backend
bridge = Bridge()
engine.rootContext().setContextProperty("bridge", bridge)

# START BAYBEEE
engine.quit.connect(app.quit)
engine.load('./ui/Main.qml')

sys.exit(app.exec())