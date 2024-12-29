import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

input_dir = 'E:/Academic/CS4203 - Research and Development Project/DataSet/Jester/20BN-JESTER/Test'
output_dir = 'C:/Users/ishar/Downloads/Test'

def process_folder(name):
    read_dir = name.strip()
    image_path = os.path.join(input_dir, read_dir)
    output_file = os.path.join(output_dir, read_dir + '.mp4')

    if not os.path.exists(image_path):
        with open('errors.log', 'a') as error_file:
            error_file.write(f"{read_dir} Error Occurred! Skipping...\n")
        return

    if os.path.exists(output_file):
        print(f"Video already exists: {output_file}, skipping...")
        return

    result = subprocess.run([
        'ffmpeg', '-framerate', '12', '-i', os.path.join(image_path, '%05d.JPG'), 
        '-vf', 'format=yuv420p', '-threads', '4', output_file
    ], capture_output=True, text=True)

    if result.returncode != 0:
        with open('errors.log', 'a') as error_file:
            error_file.write(f"Error processing {read_dir}: {result.stderr}\n")
    else:
        print(f"Video {read_dir} created successfully!")

with open('video_names.txt', 'r') as file:
    folder_names = file.readlines()

with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust max_workers
    executor.map(process_folder, folder_names)
