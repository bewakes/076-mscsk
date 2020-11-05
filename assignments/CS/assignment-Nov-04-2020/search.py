import argparse
import math
import time
import multiprocessing as mp

LIST_SIZE = 100 * 1000000
NUMBER_LENGTH = 7  # zero padded 5 digit number


class log_time:
    def __init__(self, blockname='BLOCK'):
        self.blockname = blockname

    def __enter__(self, *args, **kwargs):
        self.time = time.time()

    def __exit__(self, *args, **kwargs):
        print(self.blockname, ': ', time.time() - self.time, 'seconds')


def read_data_seek(fname='numbers.data', line_start=0, line_end=1):
    """Read data from file starting from line_start and upto line_end not included"""
    data = []
    with open(fname) as f:
        f.seek(line_start * (NUMBER_LENGTH + 1))  # +1 for newline
        line = line_start
        while line < line_end:
            try:
                data.append(int(f.readline()))
            except Exception:
                pass
            line += 1
    return data


def search_number(data, number, queue=None):
    total_count = 0
    first_index = None
    for i, x in enumerate(data):
        if x == number:
            total_count += 1
            first_index = i if first_index is None else first_index
    if queue:
        queue.put((first_index, total_count))
    else:
        return (first_index, total_count)


def run_parallel(filename, number, num_processes=2, size=LIST_SIZE):
    chunk_size = math.ceil(size/ num_processes)
    queue = mp.Queue()

    processes = []
    for i in range(num_processes):
        # with log_time(f'read data chunk {i+1}'):
        data = read_data_seek(filename, i * chunk_size, (i+1) * chunk_size)
        p = mp.Process(target=search_number, args=(data, number, queue))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    # Now collect data
    first_index = None
    total_count = 0
    for i in range(num_processes):
        ind, cnt = queue.get()
        total_count += cnt
        if ind is not None:
            first_index = i*chunk_size + ind if first_index is None or i*chunk_size + ind < first_index else first_index
    print((first_index, total_count))


def run_sequential(filename, number, size=LIST_SIZE):
    # with log_time('read_data'):
    data = read_data_seek(filename, 0, size)
    # with log_time('search number'):
    print(search_number(data, number))


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-n', '--number', type=int,
                    help='an integer to look for')
    parser.add_argument('-p', '--processors', type=int, nargs='?', default=1,
                    help='number of processors')
    parser.add_argument('-d', '--data-size', type=int, nargs='?', default=LIST_SIZE,
                    help=f'data size, defaults to {LIST_SIZE}')

    args = parser.parse_args()
    filename = 'numbers_unsorted.data'

    if args.processors >= 1:
        with log_time('parallel run'):
            run_parallel(filename, args.number, args.processors, args.data_size)
    else:
        with log_time('sequential run'):
            run_sequential(filename, args.number, args.data_size)


if __name__ == '__main__':
    main()
