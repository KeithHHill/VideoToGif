# Author: Keith Hill
# Date: 3/24/2018

import os
from moviepy.editor import *
import glob
import ConfigParser
import imgurpython


# get items in the config file

config = ConfigParser.ConfigParser()
myPath = os.path.dirname(os.path.abspath(__file__))

config.read(myPath+"\config.ini")
input_path = config.get('gif','input_path')
output_path = config.get('gif','output_path')
output_fps = int(config.get('gif','fps'))
resize = float(config.get('gif','resize'))

# get imgur credentials and create a client
client_id = config.get('imgur','client_id')
client_secret = config.get('imgur','client_secret')
ImgurClient = imgurpython.ImgurClient(client_id,client_secret)


def convertVideo(file) :
    # get a new file name
    file_name = file[:-4] + ".gif"
  
    # set the clip
    clip = (VideoFileClip(file)
        .resize(resize))


    # go to output folder and write
    os.chdir(output_path)
    clip.write_gif(file_name,fps = output_fps)
    
    #return to input folder
    os.chdir(input_path)
    return file_name


def uploadToImgur(gif) :
    os.chdir(output_path) # move to output folder

    # get the file size of the new gif
    fileinfo = os.stat(gif)

    if fileinfo.st_size > 10000000 : # imgur limits the upload to 10mb
        print("file is too large and cannot be uploaded to imgur")
        return None

    else :
        config = {
		    'name':  gif,
		    'title': gif,
	    }
        print("Uploading image... ")
        image = ImgurClient.upload_from_path(gif, config=config, anon=True)
        return image



os.chdir(input_path) # move to input folder
for file in glob.glob("*.mp4") : #loop for each video in the folder
    print(file + " has been found and will be converted to gif")
    
    # convert the video
    new_gif = convertVideo(file) 

    # upload to imgur
    image = uploadToImgur(new_gif)
    
    if image is not None:
        print(image['gifv'])

    
