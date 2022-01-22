from moviepy import editor

video = editor.VideoFileClip('Mohsen-Chavoshi-Shahrzad-Kojaei.mp4')
video.audio.write_audiofile('Kojaei.mp3')
