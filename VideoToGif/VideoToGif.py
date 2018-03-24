# Author: Keith Hill
# Date: 3/24/2018

import os
from moviepy.editor import *
import sys
import glob



# set the input and output path

input_path = "E:\Video\VideoToGif\input"
output_path = "E:\Video\VideoToGif\output"
output_fps = 15

os.chdir(input_path) # move to input folder
for file in glob.glob("*.mp4") : #loop for each video in the folder
    print(file + " has been found and will be converted to gif")

    #strip the .mp4 off the name and make it gif
    #file_name = file.strip(".mp4") + ".gif"
    file_name = file[:-4] + ".gif"
    
    # set the clip
    clip = (VideoFileClip(file)
        .resize(0.25))


    # go to output folder and write
    os.chdir(output_path)
    clip.write_gif(file_name,fps = output_fps)
    
    #return to input folder
    os.chdir(input_path)