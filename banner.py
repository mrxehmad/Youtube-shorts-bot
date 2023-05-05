import os
import random
from moviepy.editor import *
from moviepy.video.tools.credits import credits1
from moviepy.video.VideoClip import TextClip


# Define input and output directories
in_dir = 'vids'
out_dir = 'out'

# Define top and bottom text
top_text = 'Subscribe'
bottom_text = 'Sweatwise'

# Create output directory if it doesn't exist
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# Get list of input files
input_files = [f for f in os.listdir(in_dir) if f.endswith('.mp4')]

# Loop over input files and add text overlay to each video
for input_file in input_files:
    # Load input video
    video = VideoFileClip(os.path.join(in_dir, input_file))

    # Set duration attribute
    duration = video.reader.ffmpeg_duration
    video.duration = duration

    # Create text clips for top and bottom text
    txt_clip_args = {'fontsize':50, 'color':'white', 'stroke_width':2, 'stroke_color':'black'}
    top_text_clip = TextClip(top_text, **txt_clip_args).set_position(('center', 0.1), relative=True)
    bottom_text_clip = TextClip(bottom_text, **txt_clip_args).set_position(('center', 0.9), relative=True)

    # Combine video and text clips
    result = CompositeVideoClip([video, top_text_clip, bottom_text_clip])

    # Generate random filename and save output video to disk
    output_file = ''.join([str(random.randint(0, 9)) for _ in range(10)]) + '.mp4'
    result.write_videofile(os.path.join(out_dir, output_file))

    # Clear video from memory
    video.reader.close()
    video.audio.reader.close_proc()
