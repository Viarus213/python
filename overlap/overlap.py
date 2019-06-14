import numpy as np
import random
import matplotlib.pyplot as plt
import time


def overlap_save(X, h):
    N = len(X)
    M = len(h)
    block = 8  # Default block value

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

    result = []

    for i in range(0, noOfBlocks):
        result.append(y1[i])

    result = list(result)


times = []
vectors = []

for i in range(0, 20):
    y = [1, 1, 1, 1, -1]
    x = random.randint(1024, 1024 * 1024)
    a = []

    for j in range(0, x):
        a.append(random.randint(-100, 100))

    a = list(a)

    startTime = time.time()
    overlap_save(a, y)
    endTime = time.time()
    times.append(endTime - startTime)
    vectors.append(x)

print(vectors, "\n")
print(times)

plt.plot(vectors, times, "o", label="Przeprowadzone testy")
plt.xlabel("Długość wektora wejściowego")
plt.ylabel("Czas wykonania splotu metodą overlap-save")
plt.legend()
plt.show()
