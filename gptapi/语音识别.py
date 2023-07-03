import speech_recognition as sr

audio_file = '../shipinchuli/test.wav'
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
try:
    content = r.recognize_sphinx(audio)
    print('文本内容：', content.replace(' ', ''))

except Exception as e:
    print(e)
