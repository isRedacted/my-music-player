import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15
import "."

Rectangle {
    anchors.fill: parent
    color: Style.primaryColor

    ColumnLayout {
        spacing: 5
        anchors.left: parent.left
        anchors.right: parent.right

        // Hardcoded library button
        Rectangle {
            implicitWidth: parent.width
            implicitHeight: childrenRect.height + 20
            color: "transparent"
            border.color: Style.secondaryColor
            radius: 10

            Text {
                text: "Library"
                color: Style.textColor
                font.pixelSize: Style.fontSizeMedium
            }
        }
    }
    // Horizontal seperator
    ToolSeparator {
        implicitWidth: parent.width

        orientation: Qt.Horizontal
        verticalPadding: 10
        horizontalPadding: 10

        contentItem: Rectangle {
            implicitWidth: 24
            implicitHeight: 1
            color: Style.secondaryColor
        }
    }
    // List of playlists
    ListView {
    }
}