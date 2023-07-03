import openai
import pyttsx3 as pyttsx
from baidu_speech import baidusSpeechAPI
import speech_recognition as sr

wav_num = 0

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
    # tips = "（请将你的回答限制在50词以内）"
    question = baidusSpeechAPI()
    # user_input = question + tips
    user_input = question
    # user_input = input("你：")
    print(question)
    if user_input.lower() == 'exit':
        break
    bot_response = chat_with_bot(user_input)
    print("机器人:", bot_response)
    engine.say(bot_response)
    engine.runAndWait()
