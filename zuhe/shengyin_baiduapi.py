from aip import AipSpeech


def baidu_tts(text):
    # 示例
    app_id = '35150158'
    api_key = '03GWo2bv2xX9Se0LPG6xkr09'
    secret_key = 'BcSqW5bC6buGOD0ZnsiEhDF7vw1H8ZjF'
    client = AipSpeech(app_id, api_key, secret_key)
    # 实例化完毕

    result = client.synthesis(text, "zh", "1", {
        "vol": 4,  # 音量（1~9）
        "spd": 5,  # 语速（1~9）
        "pit": 4,  # 语调（1~9）
        "per": 5118,  # 0：女声 1：男声 3：逍遥音 4:萝莉音 5：御姐音
    })

    with open("lswj.wav", "wb") as f:  # audio是你所想建立的语音名，记得加上后缀".mp3"
        f.write(result)
    # print("语音已生成成功！")


# baidu_tts("你是傻逼吗")
