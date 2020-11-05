import random

N = 100 * 1000000

with open('numbers_unsorted.data', 'w') as f:
    for x in range(N):
        f.write(f'{random.randrange(0, 10000000):7}\n')
