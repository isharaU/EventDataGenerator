import os
import subprocess

input_dir = 'E:\\Academic\\CS4203 - Research and Development Project\\DataSet\\Jester\\20BN-JESTER\\Train\\' # folder contain image contained folders
output_dir = 'E:\\Academic\\CS4203 - Research and Development Project\\DataSet\\Jester\\Converted-Jester\\' # folder to save video

# open the file to read file names
with open('video_names.txt', 'r') as file:

    for name in file:
        read_dir = name.strip() 
        image_path = os.path.join(input_dir, read_dir)

        if os.path.exists(image_path):
            output_file = os.path.join(output_dir, read_dir + '.mp4')

            # Check if the output file already exists
            if os.path.exists(output_file):
                print(f"Video already exists: {output_file}, skipping...")
                continue  

            os.chdir(image_path)
            # Run the FFmpeg command to create a video from the images
            subprocess.run(['ffmpeg', '-framerate', '15', '-i', '%05d.JPG', 
                            '-vf', 'format=yuv420p', output_file])
            
            print(f"Video {read_dir} created successfully!")
        else:
            print(f"{read_dir} Error Occurred! Skipping...")
