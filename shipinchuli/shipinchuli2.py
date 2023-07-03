from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip
import tempfile

# 使用gTTS生成语音
text = "这是要转化为语音的文本"
tts = gTTS(text)

# 创建临时文件
temp_file = tempfile.NamedTemporaryFile(suffix='.mp3', delete=False)
temp_file_path = temp_file.name
temp_file.close()

# 保存语音到临时文件
tts.save(temp_file_path)

# 读取视频文件和音频文件
video = VideoFileClip("video.mp4")
audio = AudioFileClip(temp_file_path)

# 从视频文件中提取视频部分的持续时间
duration = video.duration

# 将音频文件与视频持续时间匹配
audio = audio.subclip(0, duration)

# 将音频添加到视频中
video = video.set_audio(audio)

# 保存融合后的视频文件
video.write_videofile("output3.mp4", codec="libx264", audio_codec="aac")

# 删除临时文件
temp_file.unlink()
