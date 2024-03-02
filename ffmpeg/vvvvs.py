import ffmpeg

# Define input video file path and output image directory path
input_path = 'D:\vscode\bai_tap_py\ffmpeg/video.mp4'
output_dir = 'D:\hinh'

# Define the times in seconds where you want to extract the images from
times_seconds = [1, 10, 15, 17]

# Extract the images from the video using ffmpeg-python
for i, time_sec in enumerate(times_seconds):
    (
        ffmpeg
        .input(input_path, ss=time_sec)
        .filter('scale', 640, -1)
        .output(f'{output_dir}/image_{i}.jpg', vframes=1)
        .overwrite_output()
        .run()
    )