from moviepy.editor import ImageClip, CompositeVideoClip, concatenate_videoclips

# Create a duration for the animation (in seconds)
animation_duration = 5  # 5 seconds
fps = 2  # Frames per second

# Load your image (assuming it's in the same directory as your script)
image_path = "download1.jpeg"
slide_image = ImageClip(image_path)

# Define animation function
def slide_in_animation(t):
    # Calculate the x-position based on time
    x_position = 1280 * t / animation_duration  # Assuming a 1280x720 resolution video

    # Set the position of the image clip
    return slide_image.set_position((x_position, 'center')).set_duration(1/fps)

# Calculate the number of frames based on duration and frame rate
num_frames = int(animation_duration * fps)

# Create list of image clips for each frame of the animation
image_clips = [slide_in_animation(t) for t in range(num_frames)]

# Concatenate image clips into a single video clip
animated_clip = concatenate_videoclips(image_clips, method="compose")

# Create a composite video clip with the animation
composite_clip = CompositeVideoClip([animated_clip], size=(1280, 720))

# Export the video with the sliding animation
composite_clip.write_videofile("sliding_animation.mp4", fps=fps)
