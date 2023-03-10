from multiprocessing import Pool
import time
import random


def f(x):
    time.sleep(random.random() * 2)
    return x * x


if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(f, list(range(21))))
