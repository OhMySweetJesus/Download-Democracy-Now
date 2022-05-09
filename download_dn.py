import requests
import datetime
from ftplib import FTP

today = datetime.datetime.now()
title = "dn" + str(today.strftime("%Y-%m%d"))
url = "https://mpeg.democracynow.org/" + title + ".mp4"
video = "LOCATION_WHERE_YOU_WANT_STORED/Dn" + str(today.strftime("%Y-%m%d")) + "-hd.mp4" # i.e. C:/Users/username/Desktop

def downloadVideo(url, video):
    print("Downloading new Democracy Now! video...")
    local_filename = "Dn" + str(today.strftime("%Y-%m%d")) + "-hd.mp4"
    r = requests.get(url, stream=True)
    with open(video, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

def uploadVideo(video):
    print("Uploading video to server...")
    ftp = FTP('FTP_SERVER_IP_ADDRESS')
    ftp.login(user='USERNAME', passwd='PASSWORD')
    ftp.cwd("LOCATION_YOU_WANT_FILE_SAVED")
    file = open(video, 'rb')
    ftp.storbinary("STOR Dn" + str(today.strftime("%Y-%m%d")) + "-hd.mp4")
    file.close()
    ftp.quit()

downloadVideo(url, video)
uploadVideo(video)
print("Done!")
    
