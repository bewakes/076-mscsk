for x in {1..8}; do
    s=0
    for y in {1..10}; do
        t=`python search.py -n $1 -p $x | grep seconds | grep -o '[0-9]\+.[0-9]\+'`
        s=`awk -v s=$s -v t=$t 'BEGIN { print s+t*1000 }'`
    done
    avg=`awk -v s=$s 'BEGIN { print s / 10 }'`
    echo processors $x: $avg
    echo
done
