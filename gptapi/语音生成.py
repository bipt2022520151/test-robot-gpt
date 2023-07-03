import pyttsx3 as pyttsx

engine = pyttsx.init()
engine.setProperty('rate', 240)  # 设置语音播报速度，一般115比较合适。
engine.setProperty('volume', 1.0)  # 设置音量，level  between 0 and 1，默认是1。

# getting details of current voice
voices = engine.getProperty('voices')
# changing index, changes voices. o for male。中度的女音，播报中、英文。
engine.setProperty('voice', voices[0].id)
# changing index, changes voices. 1 for female。高亮的女音，只播报英文，中文未播报。
# engine.setProperty('voice', voices[1].id)

engine.say('你好，我是你的语音助手！')
# engine.say('End of Test')

# Saving Voice to a file，On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('单个 CPU 可以执行多进程和多线程，即由操作系统在多个进程或者线程之间快速切换，使得每个进程或者线程短暂的交替运行。真正实现多线程需要多核 CPU 才可能实现。当我们要执行多个任务的时候，我们可以采用多进程、多线程、多进程+多线程的模式来实现 但是多个任务间可能有', 'test.wav')
engine.save_to_file('单个 CPU 可以执行多进程和多线程，即由操作系统在多个进程或者线程之间快速切换', 'test1.wav')
engine.runAndWait()