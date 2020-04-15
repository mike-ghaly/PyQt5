import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet("font: 24pt 'Gabriola'")
        self.verticalLayout.addWidget(self.title_label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        self.ui_path = QtWidgets.QLineEdit(self.centralwidget)
        self.ui_path.setText("")
        self.ui_path.setObjectName("ui_path")
        self.horizontalLayout.addWidget(self.ui_path)
        self.browse_1 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_1.setObjectName("browse_1")
        self.horizontalLayout.addWidget(self.browse_1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.py_path = QtWidgets.QLineEdit(self.centralwidget)
        self.py_path.setText("")
        self.py_path.setObjectName("py_path")
        self.horizontalLayout_2.addWidget(self.py_path)
        self.browse_2 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_2.setObjectName("browse_2")
        self.horizontalLayout_2.addWidget(self.browse_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.convert_b = QtWidgets.QPushButton(self.centralwidget)
        self.convert_b.setObjectName("convert_b")
        self.verticalLayout.addWidget(self.convert_b)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ui_path, self.browse_1)
        MainWindow.setTabOrder(self.browse_1, self.py_path)
        MainWindow.setTabOrder(self.py_path, self.browse_2)
        MainWindow.setTabOrder(self.browse_2, self.convert_b)

        # Button Connections
        self.convert_b.clicked.connect(self.convert)
        self.browse_1.clicked.connect(self.browse_ui_file)
        self.browse_2.clicked.connect(self.browse_py_file)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UI to Py Converter"))
        self.title_label.setText(_translate("MainWindow", "UI to Py Converter"))
        self.label_1.setText(_translate("MainWindow", "UI File Path:"))
        self.browse_1.setStatusTip(_translate("MainWindow", "Lets you choose the path of your .ui file"))
        self.browse_1.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Py File Path:"))
        self.browse_2.setStatusTip(_translate("MainWindow", "Lets you choose the path of your .py file"))
        self.browse_2.setText(_translate("MainWindow", "..."))
        self.convert_b.setStatusTip(_translate("MainWindow", "Converts .ui to .py in the desired location"))
        self.convert_b.setText(_translate("MainWindow", "Convert"))

    def convert(self):

        ui_file_path = self.ui_path.text()
        py_file_path = self.py_path.text()

        slash_index = None
        for i in range(len(ui_file_path)):
            if ui_file_path[i] == "/":
                slash_index = i

        py_file_path += ui_file_path[slash_index:]
        py_file_path = py_file_path.replace(".ui", ".py")

        command = f'pyuic5 -x "{ui_file_path}" -o "{py_file_path}"'
        print(command)
        os.system(command)

    def browse_ui_file(self):
        file = QFileDialog.getOpenFileName(self.centralwidget, "Choose File", "", "UI Files (*.ui)")
        path = file[0]
        self.ui_path.setText(path)

    def browse_py_file(self):
        folder = QFileDialog.getExistingDirectory(self.centralwidget, "Select Folder", "")
        self.py_path.setText(folder)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")

    stylesheet = resource_path("dracula.css")
    with open(stylesheet, "r") as fh:
        app.setStyleSheet(fh.read())

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon(resource_path("gear.ico")))
    MainWindow.show()
    sys.exit(app.exec_())
