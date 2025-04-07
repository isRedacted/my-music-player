import QtQuick 2.15

Image {
    property string source: "../../assets/play_circle.svg"
    property int sourceSize.width: Style.playerButtonWidth
    property int sourceSize.height: Style.playerButtonHeight
    MouseArea {
        anchors.fill: parent
        onClicked: {
            console.log("Clicked!")
        }
    }
}