#!/usr/bin/env python3

# https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

import sys

print("stations\tdate\telement\tvalue\tmflag\tqflag\tsflag")

for line in sys.stdin:
    station = line[0:11]
    year = int(line[11:15])
    month = int(line[15:17])
    element = line[17:21]

    for (day_0, day_offset) in enumerate(range(23, len(line), 8)):
        day = day_0 + 1
        day_data = line[day_offset:day_offset+8]
        if len(day_data) < 8:
            continue

        value = day_data[0:5]
        mflag = day_data[5]
        qflag = day_data[6]
        sflag = day_data[7]

        if value == "-9999": # and mflag == "  " and qflag == "  " and sflag == "  ":
            continue

        print(f"{station}\t{year:04d}-{month:02d}-{day:02d}\t{element}\t{value}\t{mflag}\t{qflag}\t{sflag}")

