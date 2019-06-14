import numpy as np
import random
import matplotlib.pyplot as plt
import time
import multiprocessing as mp


def overlap_save(X, h):
    N = len(X)
    M = len(h)
    block = 4096  # Default block value

    while block < 2 * M:
        block *= 2

    X = list(X)
    while len(X) % block != 0:  # Fill with zeros to get required length
        X.append(0)
        N += 1

    noOfBlocks = int(N / block)
    blocks = np.zeros((noOfBlocks, block))

    # Fill the blocks with the input data
    for i in range(0, noOfBlocks):
        for j in range(0, block):
            if i == 0 and j < M - 1:
                blocks[i][j] = 0
            else:
                blocks[i][j] = X[j - M + i]
            if i > 0:
                blocks[i][j] = X[i * (block - M + 1) + j - M + 1]

    blocks = np.fft.fft(blocks)
    h = list(h)

    while len(h) != block:
        h.append(0)

    h = np.fft.fft(h)
    y = blocks * h
    y1 = np.fft.ifft(y)
    y1 = list(y1)

    for i in range(0, len(y1)):
        for j in range(0, M - 1):
            y1[i] = np.delete(y1[i], j, 0)


def worker(X):
    R = 2
    y = [1, 1, 1]
    for i in range(0, R):
        overlap_save(X, y)


if __name__ == "__main__":
    K = 2 ** 20

    x_vec = []
    x_vec = np.random.randint(-10, 10, K)
    x_vec = list(x_vec)

    times = []
    daemons = []

    Z = 0

    while Z < 40:
        Z = Z + 1
        daemons.append(Z)
        works = []

        for i in range(0, Z):
            work = mp.Process(target=worker, args=(x_vec,))
            work.daemon = True
            works.append(work)
            work.start()

        startTime = time.time()
        for work in works:
            work.join()
        endTime = time.time()
        times.append(endTime - startTime)

    plt.plot(daemons, times, "o")
    plt.xlabel("Liczba daemon'ów")
    plt.ylabel("Czas wykonywania obliczeń")
    plt.legend()
    plt.show()
