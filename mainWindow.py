from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from App import Ui_MainWindow
import pydicom
import functions

class mainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Dicom Viewer')

        self.ui.file1searchButton.clicked.connect(self.showFile1SearchDialog)
        self.ui.file2searchButton.clicked.connect(self.showFile2SearchDialog)

        self.ui.loadFilesButton.clicked.connect(self.loadFiles)

    def showFile1SearchDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        self.ui.file1Path.setText(fname)

    def showFile2SearchDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        self.ui.file2path.setText(fname)

    def loadFiles(self):
        firstFileName = self.ui.file1Path.text()
        secondFileName = self.ui.file2path.text()

        print(parseFileName(firstFileName))
        print(parseFileName(secondFileName))

        dicomFile1 = pydicom.dcmread(firstFileName)
        dicomFile2 = pydicom.dcmread(secondFileName)

        image1 = dicomFile1.pixel_array
        image2 = dicomFile2.pixel_array

        qimage1 = QImage(image1.data, image1.shape[1], image1.shape[0] , QImage.Format_RGB444)
        self.ui.image1.resize(image1.shape[1], image1.shape[0])

        qimage2 = QImage(image2.data, image2.shape[1], image2.shape[0], QImage.Format_RGB444)
        self.ui.image2.resize(image2.shape[1], image2.shape[0])

        pixmap1 = QPixmap(qimage1)
        pixmap2 = QPixmap(qimage2)

        self.ui.image1.setPixmap(pixmap1)
        self.ui.image2.setPixmap(pixmap2)

        resultedImage = functions.imposeImages(image1, image2)

        qresultedImage = QImage(resultedImage.data, resultedImage.shape[1], resultedImage.shape[0], QImage.Format_RGB444)
        self.ui.resultedImage.resize(resultedImage.shape[1], resultedImage.shape[0])

        pixmapResultedImage = QPixmap(qresultedImage)

        self.ui.resultedImage.setPixmap(pixmapResultedImage)


def parseFileName(fileName):
    return fileName.replace('/', '\\')