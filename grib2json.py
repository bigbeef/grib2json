#!/usr/bin/python3
import os
import time
import urllib.request
import platform

if __name__ == '__main__':
    myOs = "linux"
    if platform.system().lower() == 'windows':
        myOs = "windows"
    date = time.strftime("%Y%m%d", time.localtime())
    # date = "20211103"
    fileDir = (myOs == "linux") and "/app/project/download.prod.443/grib2json/" or "d:/"
    success = False

    filename = "data.grib2"
    for hour in (18, 12, 6, 0):
        if success:
            break
        url = "https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_1p00.pl?file=gfs.t{:02d}z.pgrb2.1p00.anl&lev_100_m_above_ground=on&var_UGRD=on&var_VGRD=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.{}%2F{:02d}%2Fatmos".format(
            hour, date, hour)
        try:
            print(url)
            result = urllib.request.urlretrieve(url, "{}/temp".format(fileDir))
            success = True
            print("下载成功:{}{:02d}".format(date, hour))
            os.popen("cp -f {}temp {}{}".format(fileDir, fileDir, filename))
        except Exception as e:
            print("下载失败:{}{:02d}".format(date, hour))
    if success:
        dockerCmd = "docker run --name grib2json --rm -v {}:{} -e \"ARGS=--names --data --output {}/gfs.json --compact {}{}\" winfed/grib2json".format(
            fileDir, fileDir, fileDir, fileDir, filename)
        p = os.popen(dockerCmd)
        print(p.read())
