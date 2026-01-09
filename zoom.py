from moviepy.editor import VideoFileClip
import os
import cv2

# Load the video file
video_path = 'media/output_video.mp4'
clip = VideoFileClip(video_path)

# Get the frames per second (fps) of the video
fps = clip.fps

# Get the duration of the video in seconds
duration_sec = clip.duration

output_folder = 'frames_2/'
os.makedirs(output_folder, exist_ok=True)

# Extract frames at regular intervals until the end of the video
t = 0
frame_count = 0
scale_factor = 1.5  # Zoom factor

while t < duration_sec:
    # Get the frame at the current time point (t)
    frame = clip.get_frame(t)
    frame_np = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Calculate the new dimensions after zooming
    new_width = int(frame_np.shape[1] * scale_factor)
    new_height = int(frame_np.shape[0] * scale_factor)

    # Resize the frame
    scaled_frame_np = cv2.resize(frame_np, (new_width, new_height))

    # Save the zoomed frame to the frames_2 folder
    frame_path = os.path.join(output_folder, f"frame_{frame_count}.png")
    cv2.imwrite(frame_path, cv2.cvtColor(scaled_frame_np, cv2.COLOR_BGR2RGB))

    frame_count += 1
    print(f"Frame {frame_count} at time {t} seconds processed with zoom effect")

    # Move to the next time point based on the frame duration
    t += 1 / fps

# Close the video clip
clip.close()

print(f"Zoomed frames saved in: {output_folder}")
