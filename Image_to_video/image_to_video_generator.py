import os
import subprocess

lower_bound = 49968
upper_bound = 148073
input_dir = 'E:\\Academic\\CS4203 - Research and Development Project\\DataSet\\Jester\\20BN-JESTER\\Test\\' # folder contain image contained folders
output_dir = 'E:\\Academic\\CS4203 - Research and Development Project\\DataSet\\Jester\\Converted-Jester\\' # folder to save video

# create a file to save file names
with open('video_names.txt', 'w') as f:

    for i in range(lower_bound, upper_bound + 1):
        read_dir = str(i)  
        image_path = os.path.join(input_dir, read_dir)

        if os.path.exists(image_path):
            output_file = os.path.join(output_dir, read_dir + '.mp4')
            os.chdir(image_path)
            # Run the FFmpeg command to create a video from the images
            subprocess.run(['ffmpeg', '-framerate', '15', '-i', '%05d.JPG', 
                            '-vf', 'format=yuv420p', output_file])
            print(f"Video created successfully: {output_file}")
            f.write(f"{i}\n") # write the file name to the file

        else:
            print(f"Folder {read_dir} does not exist. Skipping...")
