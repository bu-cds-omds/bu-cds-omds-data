#!/bin/sh

set -e

cd `dirname $0`/raw

wget -N 'https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt'

download_daily() {
    wget -N "https://www.ncei.noaa.gov/pub/data/ghcn/daily/all/$1.dly"
}

download_daily 'USC00198368'
download_daily 'USW00012960'
download_daily 'USW00023188'
download_daily 'USW00024229'

for station in `cat ghcnd-stations.txt | grep -E '[0-9] [A-Z]{2} [A-Z]{3,} AP' | awk '{print $1}'`
do
    download_daily $station
done
               
