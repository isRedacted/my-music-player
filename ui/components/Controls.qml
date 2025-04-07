import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15
import "."

Rectangle {
    anchors.fill: parent
    color: Style.primaryColor

    // Play and slider controls
    ColumnLayout {
        anchors.fill: parent

        // All buttons
        RowLayout {
            Layout.fillWidth: true

            // Player buttons
            RowLayout {
                Layout.alignment: Qt.AlignHCenter
                // Previous button
                Image {
                    id: "previousButton"
                    source: "../../assets/skip_previous.svg"
                    sourceSize.width: Style.playerButtonWidth
                    sourceSize.height: Style.playerButtonHeight
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            console.log("Prev Clicked!")
                        }
                    }
                }
                // Play/pause button
                Image {
                    id: "playButton"
                    source: "../../assets/play_circle.svg"
                    sourceSize.width: Style.playButtonWidth
                    sourceSize.height: Style.playButtonHeight
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            console.log("Play Clicked!")
                        }
                    }
                }
                // Next button
                Image {
                    id: "nextButton"
                    source: "../../assets/skip_next.svg"
                    sourceSize.width: Style.playerButtonWidth
                    sourceSize.height: Style.playerButtonHeight
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            console.log("Next Clicked!")
                        }
                    }
                }
            }

            // Secondary control buttons
            RowLayout {
                Layout.alignment: Qt.AlignRight
                // Play queue button
                Image {
                    id: "playQueue"
                    source: "../../assets/play_queue.svg"
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            console.log("Play queue Clicked!")
                        }
                    }
                }
            }
        }

        // Progress
        Slider {
            Layout.alignment: Qt.AlignHCenter
            Layout.fillWidth: true
            Layout.leftMargin: 20
            Layout.rightMargin: 20
            focusPolicy: Qt.NoFocus
        }
    }
}