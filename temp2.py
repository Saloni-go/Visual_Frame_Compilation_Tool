from moviepy.editor import VideoFileClip,clips_array

length=2

clip1=VideoFileClip("Mera saya sath hoga @MakeJokeOf _ Saurabh Shukla.mp4").subclip(0,0+length)
clip2=VideoFileClip("pexels-peter-fowler-6394054 (Original) (1) (1) (1).mp4").subclip(0,0+length)
clip3=VideoFileClip("output_video_fast_opacity_transition.mp4").subclip(0,0+length)
clip4=VideoFileClip("output_video6.mp4").subclip(0,0+length)

combined=clips_array([[clip1,clip2]])

combined.write_videofile("test.mp4")