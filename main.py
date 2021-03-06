import cv2
import serial
import sys
import glob
import qt.design
import pyzbar.pyzbar as pyzbar


from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import serial.tools.list_ports

font = cv2.FONT_HERSHEY_SIMPLEX

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, parent=None):
        super().__init__(parent)
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            print(port)

        com = input("Select port:")
        ser = serial.Serial(com, int(9600))
        self.ser = ser

    def run(self):
        cap = cv2.VideoCapture(1)
        x2, y2 = cap.get(3) // 2, cap.get(4) // 2
        while True:
            ret, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                print(obj)
                x, y, w, h = obj.rect
                cv2.putText(frame, obj.data, (x, y), font, 15, (0, 255, 0))
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)


            key = cv2.waitKey(1)
            if key == 27:
                break
                
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

class App(QtWidgets.QMainWindow, qt.design.Ui_MainWindow):
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.th = Thread(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.start()
        self.pushButton.clicked.connect(self.shoot)
        self.pushButton_2.clicked.connect(self.up)
        self.pushButton_3.clicked.connect(self.down)
        self.pushButton_4.clicked.connect(self.left)
        self.pushButton_5.clicked.connect(self.right)

    def shoot(self):
        self.th.ser.write(b'p')

    def down(self):
        for _ in range(int(self.lineEdit.text())):
            self.th.ser.write(b'd')

    def up(self):
        for _ in range(int(self.lineEdit.text())):
            self.th.ser.write(b'u')

    def left(self):
        for _ in range(int(self.lineEdit.text())):
            self.th.ser.write(b'l')

    def right(self):
        for _ in range(int(self.lineEdit.text())):
            self.th.ser.write(b'r')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

cv2.waitKey(0)
cv2.destroyAllWindows()