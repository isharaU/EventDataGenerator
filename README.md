# Image Sequence to Video and Event Data Conversion Pipeline

This project consists of two main scripts that combine to convert image sequences into videos and then into event data using the v2e (Video to Events) tool.

## Part 1: Image Sequence to Video Conversion

### Prerequisites

- Python 3
- FFmpeg installed and accessible from the command line

### Configuration

Before running the script, ensure you set the following variables:

- `lower_bound`: The starting folder number (default: 2)
- `upper_bound`: The ending folder number (default: 2054)
- `input_dir`: The directory containing the numbered folders with image sequences
- `output_dir`: The directory where the output video files will be saved

### How it works

1. The script iterates through folders numbered from `lower_bound` to `upper_bound`.
2. For each existing folder, it uses FFmpeg to convert the image sequence into an MP4 video.
3. The output video is named after the corresponding folder number.
4. A file named `video_names.txt` is created, listing all the successfully converted video files.

### Usage

1. Set the correct paths for `input_dir` and `output_dir`.
2. Run the script:

   ```bash
   python image_to_video_conversion.py
   ```

### Output

- MP4 video files will be created in the specified `output_dir`.
- A `video_names.txt` file will be generated, listing all created video files.

## Part 2: Video to Event Data Conversion

### There are versions i.e local & colab you can choose corresponding to your need.

### Prerequisites

- NVIDIA GPU (the script checks for GPU availability)
- Python libraries: numba, engineering-notation, opencv-contrib-python, argcomplete, dv-processing
- v2e (Video to Events) tool

### Installation

1. Clone the v2e repository and install it:

   ```bash
   git clone https://github.com/SensorsINI/v2e
   cd v2e
   pip install .
   ```

2. Install required Python libraries:

   ```bash
   pip install numba engineering-notation opencv-contrib-python argcomplete dv-processing
   ```

### Configuration

- Set the `names_file_path` variable to the location of your `video_names.txt` file.
- Adjust the input and output paths as needed.
- Configure v2e parameters such as `output_mode`, `input_frame_rate`, and various noise and threshold settings.

### How it works

1. The script reads the video names from `video_names.txt`.
2. For each video, the v2e tool converts the video into event data.
3. The event data is saved in the specified output format (HDF5 in this case).

### Usage

Run the script after setting up the environment and configuring the parameters:

```bash
python video_to_event_conversion.py
```

### Output

- Event data files (e.g., `events.h5`) will be created in the specified output directories.
- The event data represents the video content in the format of a Dynamic Vision Sensor (DVS).

## Notes

- The video-to-event conversion script uses the v2e tool, which simulates how a Dynamic Vision Sensor would capture the scene.
- You can adjust various parameters to control the quality and characteristics of the event data output.
- The script supports different output modes corresponding to various DVS sensor resolutions (e.g., dvs128, dvs240, dvs346, dvs640, dvs1024).

## Error Handling

- The scripts will skip any missing input files or folders and continue with the next available input.
- Any errors during the conversion processes will be displayed in the console.


