from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QSize, QUrl, QStringListModel

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
    data = ['Python', 'is ', 'awesome']
    list_controller.set_list_model(data)
    # Expose the controllers to the Qml code
    my_model = QStringListModel()
    my_model.setStringList(data)

    # Set Qml Context
    view.rootContext().setContextProperty('myListControl', list_controller)
    view.rootContext().setContextProperty('myModel', my_model)

    # Retrieve list.qml
    qml_list_file = File(DEFAULT_QML_VIEW_FOLDER() / "list.qml")
    # Retrieve the absolute path as str
    qml_path = str(qml_list_file().absolute())
    # Add qml to the view
    view.setSource(QUrl.fromLocalFile(qml_path))

    # Show the window
    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.show()

    # Run the application & cleanup
    app.exec_()
    del view
