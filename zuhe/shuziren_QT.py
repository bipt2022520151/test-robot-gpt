import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer, QUrl, pyqtSignal, QThread, QObject, pyqtSlot
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
a = 0


class Worker(QObject):
    finished = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtSlot(int, str)
    def do_work(self, arg1, arg2):
        # 在这里执行耗时的操作
        # ...
        print(arg1,arg2)
        print("这里是线程")
        print("提出你的问题")
        number_vedio = input()
        print("你好！", "aa" + number_vedio)
        sp = "D:/Users/Administrator/PycharmProjects/flaskwl/zuhe/output" + number_vedio + ".mp4"

        # "D:/Users/Administrator/PycharmProjects/flaskwl/zuhe/output0.mp4"

        print("播放新的视频之后~")
        # self.finished.emit()


class Ui_MainWindow(QMainWindow):
    start_work = pyqtSignal(int, str)

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

        # 计时器
        self.next_step_timer = QTimer(self)
        self.next_step_timer.setSingleShot(True)
        self.next_step_timer.timeout.connect(self.next_step)
        self.ansnum = 0
        # 线程
        # 创建一个新线程
        self.thread = QThread()
        # 创建一个 worker 对象
        self.worker = Worker()
        # 将 worker 对象移动到新线程中
        self.worker.moveToThread(self.thread)
        # 连接信号和槽
        self.worker.finished.connect(self.thread.quit)
        self.start_work.connect(self.worker.do_work)


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
        # self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取本地视频文件
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("D:/Users/Administrator/PycharmProjects/flaskwl/zuhe"
                                                              "/output0.mp4")))
        # print(os.getcwd())
        self.player.setVolume(100)
        # print(self.player.state())
        self.player.play()  # 播放视频
        self.player.mediaStatusChanged.connect(self.media_status_changed)

    def media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.next_step_timer.start(0)  # 立即触发下一步的执行

    @pyqtSlot(int, str)
    def next_step(self):
        # 启动线程
        self.thread.start()
        # 发送带参数的信号
        self.start_work.emit(123, 'hello')
        # q = self.ansnum
        # 在这里执行下一步的代码


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = Ui_MainWindow()
    vieo_gui.show()
    sys.exit(app.exec_())
