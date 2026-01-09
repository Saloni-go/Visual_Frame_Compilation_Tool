from moviepy.editor import VideoFileClip

clip = VideoFileClip("output_video_p/output_video_1080p.mp4")


fade_duration = 4.0  # in seconds

faded_clip = clip.fadein(fade_duration).fadeout(fade_duration)

faded_clip.write_videofile("output_video6.mp4")

