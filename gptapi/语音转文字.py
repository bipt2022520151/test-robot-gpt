
# import PyAudio
import speech_recognition as sr
wav_num = 0
while True:
    r = sr.Recognizer()
    # 启用麦克风
    mic = sr.Microphone()
    print('录音中...')
    with mic as source:
        # 降噪
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    with open(f"00{wav_num}.wav", "wb") as f:
        # 将麦克风录到的声音保存为wav文件
        f.write(audio.get_wav_data(convert_rate=16000))
    print('录音结束，识别中...')
    content = r.recognize_sphinx(audio)
    print('文本内容：', content.replace(' ', ''))
    wav_num += 1
# audio_file = "00{wav_num}.wav"
# audio_file = 'test.wav'
# r = sr.Recognizer()
# with sr.AudioFile(audio_file) as source:
#     audio = r.record(source)
# try:
#     content = r.recognize_sphinx(audio)
#     print('文本内容：', content.replace(' ', ''))
#
# except Exception as e:
#     print(e)
