import QtQuick 2.12
import QtQuick.Controls 2.12

Page {
    width: 960
    height: 500

    header: Label {
        color: "#FFFFFF"
        text: qsTr("List")
        font.pointSize: 17
        font.bold: true
        font.family: "Arial"
        renderType: Text.NativeRendering
        horizontalAlignment: Text.AlignHCenter
        padding: 1
    }
    Rectangle {
        id: root
        width: parent.width
        height: parent.height

        Image {
            id: image
            fillMode: Image.PreserveAspectCrop
            anchors.centerIn: root
            source: "./resource/earth.960x540.jpg"
            opacity: 1
        }

        ListView {
            id: view
            anchors.fill: root
            anchors.margins: 25
            model: myModel
            delegate: Text {
                color: "#0080FF"
                anchors.leftMargin: 70
                font.pointSize: 16
                font.bold: true
                horizontalAlignment: Text.AlignHCenter
                text: display
            }
        }
    }
    NumberAnimation {
        id: anim
        running: true
        target: view
        property: "contentY"
        duration: 900
    }
}
