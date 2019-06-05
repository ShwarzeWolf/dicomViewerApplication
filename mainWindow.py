from PyQt5 import QtWidgets, QtGui, QtCore

class mainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setFont(
            QtGui.QFont('SansSerif', 14)
        )

        self.ui.label.setGeometry(
            QtCore.QRect(10, 20, 200, 400)
        )  # изменить геометрию ярлыка

        self.ui.label.setText("PyScripts")
