#!/bin/bash -e
date=$(date "+%Y%m%d")
dir="/app/project/download.prod.443/grib2json/"
filename="data.grib2"
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_1p00.pl?file=gfs.t00z.pgrb2.1p00.anl&lev_100_m_above_ground=on&var_UGRD=on&var_VGRD=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.${date}%2F00%2Fatmos"
download_cmd=$(curl --connect-timeout 120 -s -w "%{http_code}" -o ${dir}temp  "${url}")
mkdir -p  ${dir}
touch ${dir}temp

if [ 200 = $download_cmd ];then
    echo "下载成功"
    cp -f ${dir}temp ${dir}${filename}
    docker run --name grib2json \
    --rm -v ${dir}:${dir} \
    -e "ARGS=--names --data --output ${dir}/gfs.json --compact ${dir}${filename}" \
    winfed/grib2json
else
   echo "下载失败"
 fi
