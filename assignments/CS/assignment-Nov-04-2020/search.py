import time
import sys
from multiprocessing import Process


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


def search_number(data, number):
    appearances = 0
    first_index = None
    for i, x in enumerate(data):
        if x == number and first_index is None:
            first_index = i
        elif x == number:
            appearances += 1
    return (first_index, appearances)


def run_parallel(number):
    with log_time('read_data'):
        data = read_data()
    print('parallel')


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
