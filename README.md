grib2json
=========

```
# download gribfile
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_1p00.pl

example:
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_1p00.pl?file=gfs.t00z.pgrb2.1p00.anl&lev_100_m_above_ground=on&var_UGRD=on&var_VGRD=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20211103%2F00%2Fatmos
```

How to use in windows os
=========

```
git clone https://github.com/bigbeef/grib2json.git

# in china
#git clone https://github.com.cnpmjs.org/bigbeef/grib2json

cd grib2json/bin
grib2json.cmd --data --output ../demo/output.json --names --compact ../demo/gfs.t12z.pgrb2.1p00.f000
```

Create docker image
=========

```
git clone https://github.com/bigbeef/grib2json.git

# in china
#git clone https://github.com.cnpmjs.org/bigbeef/grib2json

cd grib2json

docker build -t winfed/grib2json .
```

How to use in docker
=========

```
docker run --name grib2json \
--rm -v /app/docker/grib2json:/app/docker/grib2json \
-e "ARGS=--names --data --output /app/docker/grib2json/output.json --compact /app/docker/grib2json/gfs.t18z.pgrb2.1p00.anl" \
winfed/grib2json
```
