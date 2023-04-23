#Autoplay Script
import os, random

#playlist path
path = "/media/videoDrive/GreekVids"

videoList = os.listdir(path)
random.shuffle(videoList)
for video in videoList:
    target = os.path.join(path, video)
#    print video
#   print target
    os.system('omxplayer "{}" > /dev/null'.format(target))
    #os.system('echo "And here we have {}"'.format(video))
