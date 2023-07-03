import openai

from gptapi.baidu_speech import baidusSpeechAPI
from vedio_connect import add2vedio
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

    while True:
        print("你说：", end='')
        question = baidusSpeechAPI()

        if "result" in question:
            user_input = question['result'][0]
            print(question['result'][0])
        else:
            print("再见！")
            break

        bot_response = chat_with_bot(user_input)
        print("机器人:", bot_response)
        baidu_tts(bot_response)
        add2vedio()


