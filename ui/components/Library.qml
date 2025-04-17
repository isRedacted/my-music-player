/* Will look something like MusicBee's album and artists view */

import QtQuick 2.15
import QtQuick.Controls 2.15
import "."

Rectangle {
    anchors.fill: parent
    color: "Green"

    Component.onCompleted: {
        console.log("loaded!")
    }
}