import math
import time
import sys
import multiprocessing as mp

LIST_SIZE = 6000000
NUMBER_LENGTH = 5  # zero padded 5 digit numbers


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


def read_data_seek(fname='numbers.data', line_start=0, line_end=1):
    """Read data from file starting from line_start and upto line_end not included"""
    data = []
    with open(fname) as f:
        f.seek(line_start * (NUMBER_LENGTH + 1))  # +1 for newline
        line = line_start
        while line < line_end:
            data.append(int(f.readline()))
            line += 1
    return data


def search_number(data, number, queue=None):
    total_count = 0
    first_index = None
    for i, x in enumerate(data):
        [b for b in range(20)]  # NOTE: this is just to increase time per iteration to make each iteration significant
        if x == number and first_index is None:
            first_index = i
        elif x == number:
            total_count += 1
    if queue:
        queue.put((first_index, total_count))
    else:
        return (first_index, total_count)


def run_parallel(number, num_processes=2):
    chunk_size = math.ceil(LIST_SIZE / num_processes)
    queue = mp.Queue()

    for i in range(num_processes):
        with log_time(f'read data chunk {i+1}'):
            data = read_data_seek('numbers.data', i * chunk_size, (i+1) * chunk_size)
        p = mp.Process(target=search_number, args=(data, number, queue))
        p.start()
        p.join()

    # Now collect data
    first_index = None
    total_count = 0
    for i in range(num_processes):
        ind, cnt = queue.get()
        total_count += cnt
        first_index = ind if first_index is None or i*chunk_size + ind < first_index else first_index
    print((first_index, total_count))


def run_sequential(number):
    with log_time('read_data'):
        data = read_data_seek('numbers.data', 0, LIST_SIZE)
    with log_time('search number'):
        print(search_number(data, number))


def main():
    if len(sys.argv) < 2:
        print('ERROR: Provide an integer to search for')
        exit()

    number = int(sys.argv[1])
    processors = 3
    if len(sys.argv) > 2 and sys.argv[2] == 'parallel':
        with log_time('parallel run'):
            run_parallel(number, processors)
    else:
        with log_time('sequential run'):
            run_sequential(number)


if __name__ == '__main__':
    with log_time('total_runtime'):
        main()
