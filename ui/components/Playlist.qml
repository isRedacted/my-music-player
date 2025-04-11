import QtQuick 2.15
import QtQuick.Controls 2.15
import "."

Rectangle {
    anchors.fill: parent
    
    Rectangle {
        height: parent.height / 6
        width: parent.width
        color: "green"
    }

    TableView {
        anchors.fill: parent
    }
}