import os
import shutil

# Function to copy specified folders to a new destination
def copy_folders(src_dir, text_file, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Read the folder names from the text file
    with open(text_file, 'r') as f:
        folder_names = [line.strip() for line in f.readlines()]
    
    # Loop through each folder name and copy the folder
    for folder_name in folder_names:
        src_folder_path = os.path.join(src_dir, folder_name)
        dest_folder_path = os.path.join(dest_dir, folder_name)

        # Check if the folder exists before copying
        if os.path.exists(src_folder_path):
            shutil.copytree(src_folder_path, dest_folder_path)
            print(f"Copied folder {folder_name} to {dest_dir}")
        else:
            print(f"Folder {folder_name} does not exist in {src_dir}")

src_directory = 'E:/Academic/CS4203 - Research and Development Project/DataSet/Jester/20BN-JESTER/Train'   # The parent folder where all numbered folders are located
text_file_path = "E:/Academic/CS4203 - Research and Development Project/DataSet/Converting/Classified/labels/Sliding_Two_Fingers_Up.txt"   # Path to the text file containing folder names
dest_directory = "E:/Academic/CS4203 - Research and Development Project/DataSet/Converting/Classified/data/Sliding_Two_Fingers_Up"  # The folder where you want to copy the folders
copy_folders(src_directory, text_file_path, dest_directory)
