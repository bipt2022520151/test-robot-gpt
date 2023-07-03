import sys
import pyttsx3 as pyttsx
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wgt_video = QVideoWidget(self.centralwidget)  # 创建一个 视频播放组件
        self.wgt_video.setGeometry(QtCore.QRect(50, 20, 500, 300))
        self.wgt_video.setObjectName("wgt_video")

        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(260, 320, 120, 50))
        self.btn_open.setObjectName("btn_open")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_open.setText(_translate("MainWindow", "打开视频文件并播放"))

        self.player = QMediaPlayer()  # 创建视频播放管理器
        self.player.setVideoOutput(self.wgt_video)  # 视频播放输出的widget，就是上面定义的
        self.btn_open.clicked.connect(self.openVideoFile)  # 打开视频文件按钮

    def openVideoFile(self):
        print('open file')

        # 选择本地视频播放
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取本地视频文件
        self.player.setVolume(20)
        print(self.player.state())
        # engine.say('你好，我是你的语音助手！')
        # engine.runAndWait()
        self.player.play()  # 播放视频
        self.player.mediaStatusChanged.connect(self.media_status_changed)

    def media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.player.setPosition(0)  # 将视频播放位置设置为0，即重新开始播放
            self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = Ui_MainWindow()
    vieo_gui.show()
    sys.exit(app.exec_())
