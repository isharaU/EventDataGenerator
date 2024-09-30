import os
import subprocess

input_dir = 'E:\\Academic\\CS4203 - Research and Development Project\\DataSet\\Jester\\20BN-JESTER\\Train\\' # folder contain image contained folders
output_dir = 'E:\\Academic\\CS4203 - Research and Development Project\\DataSet\\Jester\\Converted-Jester\\' # folder to save video

# create a file to save file names
with open('video_names.txt', 'r') as file:

    for name in file:
        read_dir = name.strip()
        image_path = os.path.join(input_dir, read_dir)

        if os.path.exists(image_path):
            output_file = os.path.join(output_dir, read_dir + '.mp4')
            os.chdir(image_path)
            # Run the FFmpeg command to create a video from the images
            subprocess.run(['ffmpeg', '-framerate', '15', '-i', '%05d.JPG', 
                            '-vf', 'format=yuv420p', output_file])
            print(f"Video created successfully: {output_file}")
        else:
            print(f"Folder {read_dir} Error Occured! Skipping...")
