from multiprocessing import Pool
import time


def f(x):
    time.sleep(4)
    return x * x


if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(f, list(range(21))))
