from moviepy.editor import VideoFileClip, ImageClip
import os

# Load the video file
video_path = 'media/output_video.mp4'
clip = VideoFileClip(video_path)

# Get the frames per second (fps) of the video
fps = clip.fps

# Get the duration of the video in seconds
duration_sec = clip.duration

output_folder = 'frames/'
os.makedirs(output_folder, exist_ok=True)

# Extract frames at regular intervals until the end of the video
t = 0
frame_count = 0

while t < duration_sec:
    # Get the frame at the current time point (t)
    frame = clip.get_frame(t)
    
    # Create an ImageClip from the frame (NumPy array)
    frame_clip = ImageClip(frame)
    
    # Save the frame as an image file
    frame_path = os.path.join(output_folder, f'frame_{frame_count}.png')
    frame_clip.save_frame(frame_path)
    
    print(f"Frame at time {t} seconds saved as {frame_path}")
    
    # Move to the next time point based on the frame duration
    t += 1 / fps
    frame_count += 1

# Close the video clip
clip.close()

print(f"Frames extraction completed. {frame_count} frames saved.")
