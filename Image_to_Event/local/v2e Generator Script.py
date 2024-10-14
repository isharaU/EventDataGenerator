import os

# clone & install v2e
# Installing dependencies
# %pip install numba -q
# %pip install engineering-notation -q
# %pip install opencv-contrib-python -q
# %pip install argcomplete -q
# %pip install dv-processing -q

os.system("nvidia-smi")

names = "names_full.txt"
input_dir = "/input"
output_dir = "/output"
slowmo_path = "/SuperSloMo39.ckpt"

# Open the file in read mode
with open(names, "r") as file:
    for name in file:
        name = name.strip()
        path = input_dir + "/" + name 

        output_folder = output_dir + "/" + name

        overwrite = True
        unique_output_folder = True
        out_filename = "events.h5"
        davis_output = True

        skip_video_output = False 
        dvs_exposure = "duration .033"
        output_mode = "dvs346" 

        input_frame_rate = 15
        input_slowmotion_factor =  1

        disable_slomo = True
        timestamp_resolution = 0.001
        auto_timestamp_resolution = True

        # download of SuperSloMo39.ckpt from https://github.com/SensorsINI/v2e/blob/main/input/SuperSloMo39.ckpt
        slomo_model = slowmo_path

        condition = "Clean" #["Custom", "Clean", "Noisy"]

        # Do not change following parameters unless you are in the custom mode
        thres = 0.2 
        sigma = 0.03 
        cutoff_hz = 200 
        leak_rate_hz = 5.18 
        shot_noise_rate_hz = 2.716 


        if condition == "Clean":
            thres = 0.2
            sigma = 0.02
            cutoff_hz = 0
            leak_rate_hz = 0
            shot_noise_rate_hz = 0

        elif condition == "Noisy":
            thres = 0.2
            sigma_thres = 0.05
            cutoff_hz = 30
            leak_rate_hz = 0.1
            shot_noise_rate_hz = 5


        v2e_command = ["v2e"]

        # the video_path can be a video file or a folder of images
        v2e_command += ["-i", path]

        # set the output folder
        v2e_command += ["-o", output_folder]

        # if the output will rewrite the previous output
        if overwrite:
            v2e_command.append("--overwrite")

        # if there the output folder is unique
        v2e_command += ["--unique_output_folder", "{}".format(unique_output_folder).lower()]

        # set output configs, for the sake of this tutorial, let's just output HDF5 record
        if davis_output:
            v2e_command += ["--davis_output"]

        v2e_command += ["--dvs_h5", out_filename]
        v2e_command += ["--dvs_aedat2", "None"]
        v2e_command += ["--dvs_text", "None"]

        # in Colab, let's say no preview
        v2e_command += ["--no_preview"]

        # if skip video output
        if skip_video_output:
            v2e_command += ["--skip_video_output"]
        else:
            # set DVS video rendering params
            v2e_command += ["--dvs_exposure", dvs_exposure]

        # set slomo related options
        v2e_command += ["--input_frame_rate", "{}".format(input_frame_rate)]
        v2e_command += ["--input_slowmotion_factor", "{}".format(input_slowmotion_factor)]

        # set slomo data
        if disable_slomo:
            v2e_command += ["--disable_slomo"]
            v2e_command += ["--auto_timestamp_resolution", "false"]
        else:
            v2e_command += ["--slomo_model", slomo_model]
            if auto_timestamp_resolution:
                v2e_command += ["--auto_timestamp_resolution", "{}".format(auto_timestamp_resolution).lower()]
            else:
                v2e_command += ["--timestamp_resolution", "{}".format(timestamp_resolution)]

        # threshold
        v2e_command += ["--pos_thres", "{}".format(thres)]
        v2e_command += ["--neg_thres", "{}".format(thres)]

        # sigma
        v2e_command += ["--sigma_thres", "{}".format(sigma)]

        # DVS non-idealities
        v2e_command += ["--cutoff_hz", "{}".format(cutoff_hz)]
        v2e_command += ["--leak_rate_hz", "{}".format(leak_rate_hz)]
        v2e_command += ["--shot_noise_rate_hz", "{}".format(shot_noise_rate_hz)]

        # append output mode
        v2e_command += [f"--{output_mode}"]

        # Final v2e command

        final_v2e_command = " ".join(v2e_command)

        print(final_v2e_command)

        # Run command!
        os.system(final_v2e_command)
