from moviepy.editor import *

# Load the video file
video_path = 'example_video.mp4'
clip = VideoFileClip(video_path)

# Get the frames per second (fps) of the video
fps = clip.fps

# Get the duration of the video in seconds
duration_sec = clip.duration

# Define the time interval (in seconds) for extracting frames
interval_sec = 1  # Extract frames every 1 second

# Extract frames at regular intervals until the end of the video
t = 0
while t < duration_sec:
    # Get the frame at the current time point (t)
    frame = clip.get_frame(t)
    
    # Save the frame as an image file (you can save in any format supported by PIL)
    frame_path = f'frame_{int(t)}.png'  # Use integer time as part of the filename
    ImageClip(frame).save_frame(frame_path)

    print(f"Frame at time {t} seconds saved as {frame_path}")
    
    # Move to the next time point based on the interval
    t += interval_sec

# Close the video clip
clip.close()