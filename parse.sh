#!/bin/sh

set -e

cd `dirname $0`

parse_city_value() {
    cat "raw/$2.dly" | fgrep "$3" | ./parse-ghcn.py > "data/$1-$3.tsv"
}

parse_city_value "boston" "USC00198368" "TMAX"
parse_city_value "boston" "USC00198368" "TMIN"
