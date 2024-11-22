import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 120
    height: 30

    // Définir un signal qui sera émis lorsqu'on change l'état du switch
    signal modeChanged(bool checked)

    Switch {
        anchors.centerIn: parent
        onCheckedChanged: {
            modeChanged(checked)
        }
    }
    style: SwitchStyle {
                handle: Rectangle {
                    width: 20
                    height: 20
                    radius: 10
                    color: "white"
                }
                indicator: Rectangle {
                    width: 40
                    height: 20
                    radius: 10
                    color: "gray"
                }
            }
}
