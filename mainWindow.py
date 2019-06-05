from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap
from App import Ui_MainWindow
import pydicom
import functions
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy


class mainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.file1.setText("Path to file 1:")
        self.ui.file2.setText("Path to file 2:")

        firstFile = r'C:\Users\1358365\PycharmProjects\untitled\dataset\Brain-Tumor-Progression\PGBM-001\11-19-1991-FH-HEADBrain Protocols-40993\35637-FLAIRreg-16386\000008.dcm'
        secondFile = r'C:\Users\1358365\PycharmProjects\untitled\dataset\Brain-Tumor-Progression\PGBM-001\11-19-1991-FH-HEADBrain Protocols-40993\35637-FLAIRreg-16386\000010.dcm'

        dicomFile1 = pydicom.dcmread(firstFile);
        dicomFile2 = pydicom.dcmread(secondFile);

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


    def load_image(self, file_name):

        firstFile = r'C:\Users\1358365\PycharmProjects\untitled\dataset\Brain-Tumor-Progression\PGBM-001\11-19-1991-FH-HEADBrain Protocols-40993\35637-FLAIRreg-16386\000008.dcm'
        secondFile = r'C:\Users\1358365\PycharmProjects\untitled\dataset\Brain-Tumor-Progression\PGBM-001\11-19-1991-FH-HEADBrain Protocols-40993\35637-FLAIRreg-16386\000010.dcm'

        dicomFile1 = pydicom.dcmread(firstFile);
        dicomFile2 = pydicom.dcmread(secondFile);

        image1 = dicomFile1.pixel_array
        image2 = dicomFile2.pixel_array

        #pixmap = QPixmap(image)
        self.image1.setPixmap(image1)

