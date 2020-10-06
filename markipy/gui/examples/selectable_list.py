from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QSize, QUrl

from markipy.gui import DEFAULT_QML_VIEW_FOLDER
from markipy.gui import ListController
from markipy.basic import File
import sys

if __name__ == '__main__':
    # Start a QTApp
    app = QGuiApplication(sys.argv)

    # Create view
    view = QQuickView()
    view.setMaximumSize(QSize(960, 500))
    view.setResizeMode(QQuickView.SizeRootObjectToView)

    # Create the list controller
    list_controller = ListController()

    # Add data to the list controller
    list_controller.set_list_model(['Python', 'is ', 'awesome'])

    # Retrieve list.qml
    qml_list_file = File(DEFAULT_QML_VIEW_FOLDER() / "list.qml")
    # Retrive the absolute path as str
    qml_path = str(print(qml_list_file().absolute()))

    # Add qml to the view
    view.setSource(QUrl.fromLocalFile(qml_path))

    view.rootContext().setContextProperty('ListController', list_controller)
    view.rootContext().setContextProperty('ListModel', list_controller.list_model)

    # Show the window
    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.show()

    # Run the application & cleanup
    app.exec_()
    del view
