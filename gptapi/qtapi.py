
import sys
import openai
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle('小杰巨无霸gpt自动生成器')
        self.resize(500, 400)

        # 创建一个垂直布局，并将所有控件添加到布局中
        layout = QVBoxLayout()

        # 创建一个标签，并添加到布局中
        label = QLabel('请在下方输入您的问题:')
        label.setStyleSheet('font-size: 18pt; color: #006699; font-family: SimSun')
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # 创建一个文本框，并添加到布局中
        self.text_edit = QLineEdit()
        self.text_edit.setStyleSheet('font-size: 14pt; font-family: SimSun')
        layout.addWidget(self.text_edit)

        # 创建一个水平布局，并添加一个按钮和一个标签
        hbox = QHBoxLayout()
        self.button = QPushButton('开始生成')
        self.button.setStyleSheet('font-size: 16pt; font-family: SimSun; color: white; background-color: #006699')
        self.button.clicked.connect(self.on_button_clicked)
        hbox.addWidget(self.button)
        self.answer_label = QLabel()
        self.answer_label.setStyleSheet('font-size: 14pt; color: #006699; font-family: SimSun')
        self.answer_label.setAlignment(Qt.AlignCenter)
        hbox.addWidget(self.answer_label)
        layout.addLayout(hbox)
        hbox.setAlignment(Qt.AlignCenter)

        # 设置窗口的主布局
        self.setLayout(layout)

        # 初始化OpenAI API
        openai.api_key = "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"

    def on_button_clicked(self):
        # 从文本框中获取问题
        prompt = self.text_edit.text()

        # 使用OpenAI API获取答案
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        # 将答案显示在标签中
        self.answer_label.setText(response.choices[0].text.strip())


# 创建一个Qt应用对象
app = QApplication(sys.argv)

# 创建一个窗口对象
window = ChatWindow()

# 显示窗口
window.show()

# 运行Qt应用的主循环
sys.exit(app.exec_())

