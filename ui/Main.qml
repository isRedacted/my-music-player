import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15

import "./components"

ApplicationWindow {
    visible: true
    width: 1280
    height: 720
    title: "My Music Player"
    minimumWidth: 640
    minimumHeight: 360

    Rectangle {
        anchors.fill: parent
        color: Style.backgroundColor

        ColumnLayout {
            anchors.fill: parent

            // Main container
            Rectangle {
                Layout.fillHeight: true
                Layout.fillWidth: true
                color: "transparent"
                Text {
                    text: "Main container"
                }

                RowLayout {
                    anchors.fill: parent

                    // Sidebar
                    Rectangle {
                        Layout.preferredWidth: 180
                        Layout.fillHeight: true
                        color: "green"
                        Text {
                            text: "Sidebar"
                        }
                    }

                    // Main content area
                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: "yellow"
                        Text {
                            text: "Main content area"
                        }
                    }
                }
            }

            // Bottom bar
            Rectangle {
                height: 80
                width: parent.width
                Layout.fillWidth: true
                color: "blue"
                Text {
                    text: "play/pause"
                    color: "white"
                }
                Controls {}
            }
        }
    }
}