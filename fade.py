from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips
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

# Function to generate smoothly changing opacity values
def smooth_opacity_sequence(start_opacity, end_opacity, num_steps):
    opacity_step = (end_opacity - start_opacity) / num_steps
    opacity_values = [start_opacity + i * opacity_step for i in range(num_steps + 1)]
    return opacity_values

# Extract frames at regular intervals until the end of the video
t = 0
frame_count = 0
frames_list = []

while t < duration_sec:
    # Get the frame at the current time point (t)
    frame = clip.get_frame(t)
    
    # Generate smoothly changing opacity values (faster transition with fewer steps)
    opacity_values = smooth_opacity_sequence(1.0, 0.1, 2) + smooth_opacity_sequence(0.1, 1.0,2 )
    
    # Create frames with smoothly changing opacity
    for opacity_value in opacity_values:
        # Apply opacity to the frame
        frame_with_opacity = (frame * opacity_value).astype('uint8')
        
        # Append the frame with opacity to the frames list
        frames_list.append(ImageClip(frame_with_opacity).set_duration(1/fps))
        frame_count += 1

    print(f"Frame at time {t} seconds processed with smooth opacity transition")

    # Move to the next time point based on the frame duration
    t += 1 / fps

# Close the video clip
clip.close()

# Create a video clip from the frames list
final_clip = concatenate_videoclips(frames_list)

output_video_path = 'output_video_fast_opacity_transition.mp4'

# Write the final video with fast opacity transition effect
final_clip.write_videofile(output_video_path, codec='libx264', fps=fps)

# Close the video clip
final_clip.close()

print(f"Video with fast opacity transition effect saved at: {output_video_path}")
