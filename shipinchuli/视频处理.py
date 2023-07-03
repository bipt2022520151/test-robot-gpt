from moviepy.editor import VideoFileClip, AudioFileClip, concatenate
import pyttsx3 as pyttsx

engine = pyttsx.init()
engine.setProperty('rate', 200)  # 设置语音播报速度，一般115比较合适。
engine.setProperty('volume', 1.0)  # 设置音量，level  between 0 and 1，默认是1。
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
gptsay = '真正的cpu是不畏艰险卑微去洗睡觉啊和你代金卡是你的卡是3看到了哈撒'
engine.save_to_file(gptsay, 'lswj.wav')
engine.runAndWait()
# # 读取视频文件和音频文件
video = VideoFileClip("video.mp4")
audio = AudioFileClip("lswj.wav")

# 计算视频和音频的持续时间
video_duration = video.duration
audio_duration = audio.duration

# 计算重复播放视频所需的倍数
repetitions = int(audio_duration / video_duration) + 1

# 重复播放视频
repeated_video = concatenate([video] * repetitions)

# 截取与音频持续时间匹配的视频部分
repeated_video = repeated_video.subclip(0, audio_duration)

# 将音频添加到视频中
video_with_audio = repeated_video.set_audio(audio)

# 保存融合后的视频文件
video_with_audio.write_videofile("output.mp4", codec="libx264", audio_codec="aac")
