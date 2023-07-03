from moviepy.editor import VideoFileClip, AudioFileClip, concatenate


def add2vedio():
    video = VideoFileClip("video.mp4")
    audio = AudioFileClip("lswj.wav")
    video_duration = video.duration
    audio_duration = audio.duration
    repetitions = int(audio_duration / video_duration) + 1
    repeated_video = concatenate([video] * repetitions)
    repeated_video = repeated_video.subclip(0, audio_duration)
    video_with_audio = repeated_video.set_audio(audio)
    video_with_audio.write_videofile("output.mp4", codec="libx264", audio_codec="aac")
    # nihao
    print()