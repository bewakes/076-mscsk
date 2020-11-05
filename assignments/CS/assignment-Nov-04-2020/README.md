# Comparison of parallel and sequential search algorithms
We slightly modified the problem statement to not only find the index of first appearance of the searched number, but also to calculate the total number of appearances 
of the number in the list. This way, all of the array will be traversed and the program does not have to exit when the element is found which reduces complex
communication between the processes.

## Approach 1
In this approach, we generated numbers in the program itself and passed chunks to corresponding processes to search for a given number. However, there were some issues:
1. The parallel search ran slower than the sequential search for "not large enough" datasets. Only when the large enough dataset size(approx. 10 million) provided expected results.
2. With large datasets, the copying of the chunks from main process to other spawned process took a lot of memory and hence ran very slow, sometimes even crashing the program itself.

## Approach 2
Here the numbers are generated separately and loaded in a file. With an aim to parallelize the file reading process as well, the numbers are zero-padded so that different
processes can read the chunks in the file easily.
### Set up
100 million random numbers in range (0, 10000000) are generated in a ASCII file, one number in each line and smaller numbers are zero-padded so that every
number is 7-digit long.
### Pseudo Code
<pre>
p <- number of processors
n <- number to search for

declare queue to store processors results

for each processor i, run in parallel:
    read i-th chunk of file
    result:[first_index, total_count] <- search for number in the chunk
    push the result to queue

Now collect results
for each i in 0 to p-1:
    [ind, count] <- result from queue
    accumulate count and compare ind for least index
return accumulated count and first index

</pre>

## Results from Approach 2
We ran the parallel and sequential algorithms in datasets of size 100000,
1000000, 10000000 and 100000000 using 1 to 8 processors. Corresponding speedup vs number of processors plot is shown below.
![Speedup Vs Processors Graph](speedup-graph.png)


## Conclusion
From the graph above we can see the obvious speedup of the search process when multi processors are used.
The speedup monotonically increases upto the point where 4 processors are used. Then strangely enough, for
every dataset size, there is a sudden drop in speedup for 5 processors. The speedup in general again rises
 except for the smallest dataset size. 

It is also important to note that, ignoring the drop of speedup for 5 processors, the speedup tends to be flat afterwards,
conforming to **Amhdal's Law**.

## Source Code
The source code is located [here](https://github.com/bewakes/076-mscsk/blob/master/assignments/CS/assignment-Nov-04-2020/search.py).

## Sources
- [Python docs for multiprocessing](https://docs.python.org/3.8/library/multiprocessing.html)
