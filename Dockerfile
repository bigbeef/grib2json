FROM docker.io/adoptopenjdk:11.0.7_10-jre-hotspot
ADD bin/* /usr/bin/
ADD lib/* /usr/lib/
CMD grib2json $ARGS
