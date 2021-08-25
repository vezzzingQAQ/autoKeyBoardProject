import sys
from PyQt5.QtWidgets import QMainWindow, QApplication#Qapplication任何基于PyQt5的程序都得导入
from PyQt5.QtWidgets import QVBoxLayout, QWidget,QLabel#放控件
from PyQt5.QtWidgets import QToolTip#显示提示信息

from PyQt5.QtGui import QImage, QPalette#调色板
from PyQt5.QtGui import QPixmap#用于在程序中导入图片

from PyQt5.QtCore import QTimer, Qt#储存有一些常量
from main import postImg

class QLabelEXPForm(QWidget):
    def __init__(self):
        super(QLabelEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        #创建标签
        self.timeCount=0

        self.timer=QTimer()
        self.timer.timeout.connect(self.getImg)
        self.timer.start(1)

        self.label1=QLabel(self)
        self.label3 = QLabel(self)
        self.label3.setPixmap(QPixmap("images/2.BMP"))

        #垂直布局显示四个标签
        vbox=QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label3)

        #窗体处理
        self.setLayout(vbox)
        self.setWindowTitle("和QLabel控件")

    def getImg(self):
        img=postImg()
        x=img.shape[1]  # 获取图像大小
        y=img.shape[0]
        channel=img.shape[2]
        bytesperline=channel*x
        currentImg=QImage(img.data, x, y, bytesperline, QImage.Format_RGB888)
        self.timeCount+=1
        self.label1.setText(str(self.timeCount))
        self.label3.setPixmap(QPixmap.fromImage(currentImg))

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=QLabelEXPForm()
    main.show()

    sys.exit(app.exec_())
