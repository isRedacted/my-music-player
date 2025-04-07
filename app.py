import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine, qmlRegisterSingletonType
from PyQt6.QtCore import QUrl

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

engine.quit.connect(app.quit)
engine.load('./ui/Main.qml')

sys.exit(app.exec())