import sys
from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget,QInputDialog,QFileDialog
from PyQt5.QtGui import QImage,QPixmap, QPainter, QPen,QGuiApplication
from PyQt5.QtCore import Qt
import cv2
import time
serialdata = [{"pos":(0,0),"rgb":(0,0,0)}]
import pyautogui
from op import Capture


#
# class my_label(QtWidgets.QLabel):
#     def __init__(self):
#         super().__init__()
#         # setMouseTracking设置为False，否则不按下鼠标时也会跟踪鼠标事件
#         # self.setMouseTracking(False)
#         # 设置鼠标位置存储
#         self.mousexy = []
#
#     def paintEvent(self, event):
#         """画鼠标选中的框
#
#         """
#         super().paintEvent(event)
#         painter = QPainter()
#         painter.begin(self)
#         #绘画的画笔配置
#         pen = QPen(Qt.red, 2, Qt.SolidLine)
#         painter.setPen(pen)
#         #绘画区域
#         if len(self.start_xy)>0:
#             painter.drawRect(self.mousexy[0][0],self.mousexy[0][1],self.mousexy[-1][0]-self.mousexy[0][0],self.mousexy[-1][1]-self.mousexy[0][1])
#         painter.end()
#
#         pqscreen = QGuiApplication.primaryScreen()
#         pixmap2 = pqscreen.grabWindow(self.winId(), self.mousexy[0][0],self.mousexy[0][1], abs(self.mousexy[-1][0]-self.mousexy[0][0]), abs(self.mousexy[-1][1]-self.mousexy[0][1]))
#         pixmap2.save('555.png')
#
#     def mouseMoveEvent(self, event):
#         #鼠标按下时开始记录鼠标位置
#         pos_tmp = event.pos().x(),event.pos().y()
#         self.start_xy.append(pos_tmp)
#         print(pos_tmp)
#         #self.update()每次改变位置会重新绘画
#         self.update()
#
#     def mouseReleaseEvent(self, event):
#         #鼠标松开按键清空记录的数据
#         self.mousexy = []

class myLabel(QtWidgets.QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False
    start_drw=False
    arename='1.bmp'
    def mousePressEvent(self,event):
        if self.start_drw:
            self.flag = True
            self.x0 = event.x()
            self.y0 = event.y()

    def mouseReleaseEvent(self,event):
        if self.start_drw:
            text, ok = QInputDialog.getText(self, '输入选择的区域名字',
                                            '请输入:')
            if ok and str(text)!='':
                self.arename = str(text) + '.bmp'
            self.flag = False
            pqscreen = QGuiApplication.primaryScreen()
            pixmap2 = pqscreen.grabWindow(self.winId(), self.x0 + 2, self.y0 + 2, abs(self.x1 - self.x0 - 4),
                                          abs(self.y1 - self.y0 - 4))
            pixmap2.save("photo/" + self.arename)

            # self.label_2.start_drw = False
    def mouseMoveEvent(self,event):
        if self.flag and self.start_drw:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.start_drw:

            rect =QtCore.QRect(self.x0, self.y0, self.x1-self.x0, self.y1-self.y0)
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
            painter.drawRect(rect)


            # self.label_2.start_drw = False

class my_photoshop(QWidget):

    def __init__(self):
        super(my_photoshop,self).__init__()
        self.setupUI()

        #定时器 作用是定时刷新label的文本
        self.timer = QtCore.QTimer()
        self.timer.start(300)
        self.timer.timeout.connect(self.timeout_slot)
        #线程获取当前的鼠标位置
        self.serial=SensorThread()
        self.serial.start()




    # def paintEvent(self, event):
    #     """画鼠标选中的框
    #
    #     """
    #     painter = QPainter()
    #     painter.begin(self)
    #     #绘画的画笔配置
    #     pen = QPen(Qt.red, 2, Qt.SolidLine)
    #     painter.setPen(pen)
    #     #绘画区域
    #     if len(self.start_xy)>0:
    #         painter.drawRect(self.mousexy[0][0],self.mousexy[0][1],self.mousexy[-1][0]-self.mousexy[0][0],self.mousexy[-1][1]-self.mousexy[0][1])
    #     painter.end()
    #
    # def mouseMoveEvent(self, event):
    #     #鼠标按下时开始记录鼠标位置
    #     pos_tmp = event.pos().x(),event.pos().y()
    #     self.start_xy.append(pos_tmp)
    #     print(pos_tmp)
    #     #self.update()每次改变位置会重新绘画
    #     self.update()
    #
    # def mouseReleaseEvent(self, event):
    #     #鼠标松开按键清空记录的数据
    #     self.mousexy = []


    def setupUI(self):

        self.resize(1540, 750)
        # self.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 30, 200, 70))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Microsoft YaHei")

        self.label.setFont(font)
        self.label.setLineWidth(3)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(2, 130, 200, 40))
        self.pushButton.setFont(font)

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(2, 170, 200, 40))
        self.pushButton_2.setFont(font)

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(2, 210, 200, 40))
        self.pushButton_3.setFont(font)

        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(2, 250, 200, 40))
        self.pushButton_4.setFont(font)

        self.label_2 = myLabel(self)
        self.label_2.setGeometry(QtCore.QRect(220, 0, 1320, 750))
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)

        pixmap = self.readpic_cv2QT("photo/now.bmp")
        self.label_2.setPixmap(QtGui.QPixmap(pixmap))
        self.label_2.setCursor(Qt.CrossCursor)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.pushButton.clicked.connect(self.uicapture)
        self.pushButton_2.clicked.connect(self.reloadphoto)
        self.pushButton_3.clicked.connect(self.bingen_choose_area)
        self.pushButton_4.clicked.connect(self.change_area_name)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(QWidget)


    def retranslateUi(self):
        self.setWindowTitle("shenx's Program")
        self.label.setText( "当前鼠标位置和颜色\nx,y:(0,0)\nRGB:(0,0,0)")
        self.pushButton.setText("截图")
        self.pushButton_2.setText("加载图片")
        self.pushButton_3.setText("选择区域")
        self.pushButton_4.setText("标注选择区域名字")
        self.label_2.pixmap()

    def timeout_slot(self):

        # print("当前鼠标位置和颜色\nx,y:%s\nRGB:%s"%(serialdata[-1]["pos"],serialdata[-1]["rgb"]))
        self.label.setText("当前鼠标位置和颜色\nx,y:%s\nRGB:%s"%(serialdata[-1]["pos"],serialdata[-1]["rgb"]))
    def reloadphoto(self):
        self.label_2.start_drw = False
        fname = QFileDialog.getOpenFileName(self, '选择图片', 'photo')
        if fname[0]:
            pixmap = self.readpic_cv2QT(fname[0])
        else:
            pixmap = self.readpic_cv2QT("photo/now.bmp")
        self.label_2.setPixmap(pixmap)
    def uicapture(self):

        Capture()
        self.label_2.start_drw = False
        pixmap=self.readpic_cv2QT("photo/now.bmp")
        self.label_2.setPixmap(pixmap)

    def bingen_choose_area(self):
        # setMouseTracking设置为False，否则不按下鼠标时也会跟踪鼠标事件
        # self.setMouseTracking(False)
        # self.label_2.start_drw=~self.label_2.start_drw
        self.label_2.start_drw=True
    def change_area_name(self):
        text, ok = QInputDialog.getText(self, '输入选择的区域名字',
                                        '请输入:')

        if ok and str(text)!='':
            self.label_2.arename=str(text)+'.bmp'
            # print (self.label_2.arename)
    def readpic_cv2QT(self,path):
        img = cv2.imread(path)
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        return QPixmap.fromImage(QImg)
class SensorThread(QtCore.QThread):
    def run(self):
        try:
            while True:
                pos = pyautogui.position()
                serialdata[0]={"pos":pos,"rgb":pyautogui.pixel(*pos)}
                time.sleep(0.3)
        except KeyboardInterrupt:
            exit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = my_photoshop()
    ui.show()
    app.exec_()















# class my_label(QLabel):
#     def __init__(self):
#         super().__init__()
#         # setMouseTracking设置为False，否则不按下鼠标时也会跟踪鼠标事件
#         # self.setMouseTracking(False)
#         # 设置鼠标位置存储
#         self.mousexy = []
#
#     def paintEvent(self, event):
#         """画鼠标选中的框
#
#         """
#         super().paintEvent(event)
#         painter = QPainter()
#         painter.begin(self)
#         #绘画的画笔配置
#         pen = QPen(Qt.red, 2, Qt.SolidLine)
#         painter.setPen(pen)
#         #绘画区域
#         if len(self.start_xy)>0:
#             painter.drawRect(self.mousexy[0][0],self.mousexy[0][1],self.mousexy[-1][0]-self.mousexy[0][0],self.mousexy[-1][1]-self.mousexy[0][1])
#         painter.end()
#         #
#         # pqscreen = QGuiApplication.primaryScreen()
#         # pixmap2 = pqscreen.grabWindow(self.winId(), self.mousexy[0][0],self.mousexy[0][1], abs(self.mousexy[-1][0]-self.mousexy[0][0]), abs(self.mousexy[-1][1]-self.mousexy[0][1]))
#         # pixmap2.save('555.png')
#
#     def mouseMoveEvent(self, event):
#         #鼠标按下时开始记录鼠标位置
#         pos_tmp = event.pos().x(),event.pos().y()
#         self.start_xy.append(pos_tmp)
#         print(pos_tmp)
#         #self.update()每次改变位置会重新绘画
#         self.update()
#
#     def mouseReleaseEvent(self, event):
#         #鼠标松开按键清空记录的数据
#         self.mousexy = []
