import os
import subprocess
import argparse
import sys
import re


def extract_labels_from_filename(filename):
    pattern = re.compile(r'[(](.*)[)]', re.S)  # 贪婪匹配
    labels = re.findall(pattern, filename)
    print(labels)
    return labels[0] if len(labels) else filename


def overlay_text_and_compress(input_path, output_path, text):
    # First overlay text
    tmp_output_path = "/tmp/tmp_overlay.mp4"
    overlay_cmd = [
        'ffmpeg', '-y', '-i', input_path,
        '-vf', f"drawtext=text='{text}':fontcolor=white:fontsize=24:x=10:y=10",
        '-c:a', 'copy', tmp_output_path
    ]
    subprocess.run(overlay_cmd, check=True, stdout=None)

    # Then compress
    compress_cmd = [
        'ffmpeg', '-y', '-i', tmp_output_path,
        '-b:v', '800k', '-b:a', '128k',
        '-c:v', 'libx264', '-preset', 'medium',
        '-c:a', 'aac', '-strict', 'experimental',
        output_path
    ]
    subprocess.run(compress_cmd, check=True, stdout=None)
    os.remove(tmp_output_path)  # clean up


def hconcat(*inpvideos, output):
    output_files = []
    for video_path in inpvideos:
        label = extract_labels_from_filename(video_path)
        tmp_output_path = f"/tmp/{label}.mp4"
        overlay_text_and_compress(video_path, tmp_output_path, label)
        output_files.append(tmp_output_path)

    # Create video inputs for ffmpeg concat filter
    input_files_str = ' '.join([f"-i {file}" for file in output_files])

    # Generate hstack filter string
    hstack_filter = f"hstack=inputs={len(output_files)}"

    # Final combined file output path

    # Concatenate video using hstack
    ffmpeg_concat_command = f"ffmpeg -y {input_files_str} -filter_complex \"{hstack_filter}\" -c:a copy {output}"
    subprocess.run(ffmpeg_concat_command, shell=True, check=True)


def vconcat(*inpvideos, output):
    output_files = []
    for video_path in inpvideos:
        label = extract_labels_from_filename(video_path)
        tmp_output_path = f"/tmp/{label}.mp4"
        overlay_text_and_compress(video_path, tmp_output_path, label)
        output_files.append(tmp_output_path)

    # Create video inputs for ffmpeg concat filter
    input_files_str = ' '.join([f"-i {file}" for file in output_files])

    # Generate vstack filter string
    hstack_filter = f"vstack=inputs={len(output_files)}"

    # Final combined file output path

    # Concatenate video using hstack
    ffmpeg_concat_command = f"ffmpeg -y {input_files_str} -filter_complex \"{hstack_filter}\" -c:a copy {output}"
    subprocess.run(ffmpeg_concat_command, shell=True, check=True)


def imgs2gif(*imgs, output):
    print(imgs, output)
    from PIL import Image
    import imageio

    def resize_images(images, max_width, max_height):
        resized_images = []
        for img in images:
            img.thumbnail((max_width, max_height), Image.ANTIALIAS)
            resized_images.append(img)
        return resized_images

    def save_gif(frames, output_path, duration=0.5, loop=0):
        imageio.mimsave(output_path, frames, duration=duration, loop=loop)

    def compress_gif(input_path, output_path, max_file_size):
        # Use imageio's `get_reader` to read the GIF and compress it
        with imageio.get_reader(input_path) as reader:
            frames = [frame for frame in reader]

        # Save compressed version
        save_gif(frames, output_path)
        while os.path.getsize(output_path) > max_file_size:
            # Reduce quality by resizing or decreasing duration
            reduction_factor = 0.9
            frames = resize_images(frames, int(
                frames[0].width * reduction_factor), int(frames[0].height * reduction_factor))
            save_gif(frames, output_path, duration=0.1)

    # Replace with your image paths
    images = [Image.open(img_path) for img_path in imgs]

    # Resize images to limit initial GIF size
    images = resize_images(images, 800, 800)  # Max width & height

    # Save initial GIF
    temp_path = 'temp.gif'
    save_gif(images, temp_path)

    # Compress GIF to ensure it doesn't exceed 10MB
    max_file_size = 10 * 1024 * 1024  # 10MB
    compress_gif(temp_path, output, max_file_size)

    # Clean up temporary files
    if os.path.exists(temp_path):
        os.remove(temp_path)


app = {
    "hconcat": hconcat,
    "vconcat": vconcat,
    "imgs2gif": imgs2gif,
}
