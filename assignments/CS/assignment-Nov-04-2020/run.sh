#!/bin/bash
set -e

N=${2:-1}
d=${3:-100000000}

for x in {1..8}; do
    s=0
    for y in $(seq 1 $N); do
        t=`python search.py -n $1 -p $x -d $d | grep seconds | grep -o '[0-9]\+.[0-9]\+'`
        s=`awk -v s=$s -v t=$t 'BEGIN { print s+t*1000 }'`
    done
    avg=`awk -v s=$s -v N=$N 'BEGIN { print s / N }'`
    echo processors $x: $avg
done
