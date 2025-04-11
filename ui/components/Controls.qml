import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15
import "."

/*
TODO:
- Add alt text on highlight
- Add accent colour on highlight
- Style progress/volume sliders
*/

Rectangle {
    anchors.fill: parent
    color: Style.primaryColor

    // Play and slider controls
    ColumnLayout {
        anchors.fill: parent
        anchors.bottomMargin: 10

        // All buttons
        RowLayout {
            Layout.fillWidth: true
            Layout.leftMargin: 50
            Layout.topMargin: 10

            // Song time
            RowLayout {
                Layout.alignment: Qt.AlignTop
                Text {
                    text: "0:00"
                    color: Style.textColor
                    font.pixelSize: Style.fontSizeSmall
                }
                Text {
                    text: "/"
                    color: Style.textColor
                    font.pixelSize: Style.fontSizeSmall
                }
                Text {
                    text: "0:00"
                    color: Style.textColor
                    font.pixelSize: Style.fontSizeSmall
                }
            }

            // Left spacer (pushes away from the left)
            Item {Layout.fillWidth: true}

            Rectangle {
                anchors.horizontalCenter: parent.horizontalCenter

                // Player buttons
                RowLayout {
                    anchors.centerIn: parent
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
            }
            // Centre spacer (pushes to the right)
            Item {Layout.fillWidth: true}

            // Volume controls
            RowLayout {
                // Mute button
                Image {
                    source: "../../assets/volume.svg"
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            console.log("Volume Clicked!")
                        }
                    }
                }
                // Volume slider
                Slider {
                    Layout.rightMargin: 20
                    Layout.maximumWidth: 100
                    focusPolicy: Qt.NoFocus
                    value: 1
                }
            }

            // Secondary control buttons
            RowLayout {
                Layout.alignment: Qt.AlignRight
                Layout.rightMargin: 5

                // Play queue button
                Image {
                    source: "../../assets/play_queue.svg"
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            console.log("Play queue Clicked!")
                        }
                    }
                }
                // Shuffle button
                Image {
                    source: "../../assets/shuffle.svg"
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            console.log("Shuffle Clicked!")
                        }
                    }
                }
                // Repeat button
                Image {
                    source: "../../assets/repeat.svg"
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            console.log("Repeat Clicked!")
                        }
                    }
                }
                // Last.fm button
                Image {
                    source: "../../assets/last_fm.svg"
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            console.log("Last.fm Clicked!")
                        }
                    }
                }
            }
        }

        // Progress slider
        Slider {
            Layout.alignment: Qt.AlignHCenter
            Layout.fillWidth: true
            Layout.leftMargin: 20
            Layout.rightMargin: 20
            Layout.maximumWidth: 1000
            focusPolicy: Qt.NoFocus

            onPressedChanged: {
                if (!pressed)
                {
                    console.log(value)
                }
            }
        }
    }
}