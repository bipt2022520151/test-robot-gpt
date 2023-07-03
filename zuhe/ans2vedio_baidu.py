import openai
import pyttsx3 as pyttsx
from baidu_speech import baidusSpeechAPI
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate
from shengyin_baiduapi import baidu_tts


def answer_vedio():
    openai.api_key = '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'

    def chat_with_bot(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是我的助手，名字叫做杰杰,我问你的问题都不能超过20个字。"},
                {"role": "system", "content": prompt},
            ]
        )
        bot_reply = response.choices[0].message.content
        return bot_reply

    engine = pyttsx.init()
    engine.setProperty('rate', 115)  # 设置语音播报速度，一般115比较合适。
    engine.setProperty('volume', 1.0)  # 设置音量，level  between 0 and 1，默认是1。
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    while True:
        print("你说：", end='')
        question = baidusSpeechAPI()

        if "result" in question:
            user_input = question['result'][0]
            print(user_input)

        else:
            print("没声音啊~")
            continue

        bot_response = chat_with_bot(user_input)
        baidu_tts(bot_response)
        print("机器人:", bot_response)
        gptsay = bot_response
        # engine.save_to_file(gptsay, 'lswj.wav') # 电脑自带音频
        # engine.runAndWait()
        vedio_name = "video.mp4"
        sound_name = "lswj.wav"
        v_add_s(vedio_name, sound_name)


def v_add_s(vn, sn):
    video = VideoFileClip(vn)
    audio = AudioFileClip(sn)
    video_duration = video.duration
    audio_duration = audio.duration
    repetitions = int(audio_duration / video_duration) + 1
    repeated_video = concatenate([video] * repetitions)
    repeated_video = repeated_video.subclip(0, audio_duration)
    video_with_audio = repeated_video.set_audio(audio)
    video_with_audio.write_videofile("output.mp4", codec="libx264", audio_codec="aac")


answer_vedio()
