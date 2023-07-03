from aip import AipSpeech
import speech_recognition as sr
def baidusSpeechAPI():
    # 定义百度语音识别API的APP ID、API Key和Secret Key
    APP_ID = '35150158'
    API_KEY = '03GWo2bv2xX9Se0LPG6xkr09'
    SECRET_KEY = 'BcSqW5bC6buGOD0ZnsiEhDF7vw1H8ZjF'
    # # 读取文件
    # def get_file_content(filePath):
    #     with open(filePath, 'rb') as fp:
    #         return fp.read()
    #
    r = sr.Recognizer()
    # 启用麦克风
    mic = sr.Microphone()
    # print('你说:')
    with mic as source:
        # 降噪
        r.adjust_for_ambient_noise(source, duration=1)
        # 设置阈值
        r.energy_threshold = 4000
        audio = r.listen(source)
    # WAVE_OUTPUT_FILENAME = "test.wav"
    # 创建AipSpeech对象，用于调用百度语音识别API
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 调用百度语音识别API，识别WAV文件中的语音，返回识别结果
    result = client.asr(audio.get_wav_data(convert_rate=16000), 'wav', 16000, {
        'dev_pid': 1536,
    })
    # result = client.asr(get_file_content(WAVE_OUTPUT_FILENAME), 'wav', 16000, {
    #     'dev_pid': 1536,
    # })
    # print(result['result'][0]) # 如果没有内容，则没有result这个字典
    # return result['result'][0]
    return result
# print(baidusSpeechAPI())
