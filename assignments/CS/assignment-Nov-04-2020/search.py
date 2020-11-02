import os
import math
import time
import sys
import multiprocessing as mp


class log_time:
    def __init__(self, blockname='BLOCK'):
        self.blockname = blockname

    def __enter__(self, *args, **kwargs):
        self.time = time.time()

    def __exit__(self, *args, **kwargs):
        print(self.blockname, ': ', time.time() - self.time, 'seconds')


def read_data(fname='numbers.data'):
    with open(fname) as f:
        data = [int(x) for x in f.readlines()]
    return data


def search_number(data, number, start=None, end=None, queue=None):
    total_count = 0
    first_index = None
    start = start or 0
    end = min(end or len(data), len(data))
    for i in range(start, end):
        if data[i] == number and first_index is None:
            first_index = i
        elif data[i] == number:
            total_count += 1
    if queue:
        queue.put((first_index, total_count))
    else:
        return (first_index, total_count)


def run_parallel(number, num_processes=5):
    with log_time('read_data'):
        data = read_data()

    chunk_size = math.ceil(len(data) / num_processes)
    queue = mp.Queue()

    for i in range(num_processes):
        p = mp.Process(target=search_number, args=(data, number, i*chunk_size, (i+1)*chunk_size, queue))
        p.start()
        p.join()

    # Now collect data
    first_index = None
    total_count = 0
    for i in range(num_processes):
        ind, cnt = queue.get()
        total_count += cnt
        first_index = ind if first_index is None or ind < first_index else first_index
    print((first_index, total_count))


def run_sequential(number):
    with log_time('read_data'):
        data = read_data()
    with log_time('search number'):
        print(search_number(data, number))


def main():
    if len(sys.argv) < 2:
        print('ERROR: Provide an integer to search for')
        exit()

    number = int(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2] == 'parallel':
        with log_time('parallel run'):
            run_parallel(number)
    else:
        with log_time('sequential run'):
            run_sequential(number)


if __name__ == '__main__':
    with log_time('total_runtime'):
        main()
