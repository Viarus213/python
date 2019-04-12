from scipy import stats
import random
import time
import matplotlib.pyplot as plt
import numpy as np
import math

class kopiec(list):
    def __init__(self, items = []):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 2:
            self._swap(1, len(self.heap) -1)
            max = self.heap.pop()
            self._bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def sort (self):
        sortList = []
        for i in range (len(self.heap) - 1):
            sortList.append(self.pop())
        self.heap = sortList

    def check (self):
        for i in range (len(self.heap) - 2):
            if self.heap[i] < self.heap[i + 1]:
                return 0
        return 1
            
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self.__floatUp(parent)

    def _bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._bubbleDown(largest)

M = 100000
testList = kopiec()
for k in range (M):
    testList.push(random.randint(-100, 100))

t1 = time.time()
testList.sort()
t2 = time.time()
    
T0 = t2 - t1

M = np.zeros(12, dtype='int64')
TT0 = np.zeros(12)
log2 = np.zeros(12)
timeArr = np.zeros(12)

for i in range (12):
    list = kopiec()
    #M.append(random.randint(10000, 50000))
    M[i] = random.randint(10000, 50000)
    print(M)
    for j in range (M[i]):
        list.push(random.randint(-100, 100))
    t1 = time.time()
    list.sort()
    t2 = time.time()
    T = t2 - t1

    #log2.append(math.log(M[i], 2))
    #timeArr.append(math.log(T/(T0*log2[i]), 2))
    #TT0.append(T/T0)

    log2[i] = math.log(M[i], 2)
    timeArr[i] = math.log(T/(T0*log2[i]), 2)
    TT0[i] = T/T0

print("M", log2)
print("TT0", TT0)
print(timeArr)

slope, intercept, r_value, p_value, std_err = stats.linregress(timeArr, log2)

a = slope
b = intercept

plt.plot(log2, timeArr, '.', label = 'Original data')
plt.plot(log2, a*log2 + b, '-', label = 'Fitted line')
plt.xlabel("log2(M)")
plt.ylabel("log2(T/(T0log2(M)))")
plt.legend()
plt.show()
print ("a = ",slope)
