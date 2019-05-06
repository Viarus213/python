from scipy import stats
import random
import time
import matplotlib.pyplot as plt
import numpy as np

class Kopiec(list):
    def __init__(self, items = []):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__float_up(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 2:
            self._swap(1, len(self.heap) -1)
            max = self.heap.pop()
            self._bubble_down(1)
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

    def check_sort (self):
        for i in range (len(self.heap) - 2):
            if self.heap[i] < self.heap[i + 1]:
                print("Sortowanie nie prawidłowe")
                return 0
        return 1
            
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self.__float_up(parent)

    def _bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._bubble_down(largest)

M = 100000
random_numbers_range = [-100, 100]

""" Calculate T0 """
T0_list = np.random.randint(random_numbers_range[0], random_numbers_range[1], M)
T0_list = Kopiec(T0_list)

t1 = time.time()
T0_list.sort()
t2 = time.time()
T0 = t2 - t1

""" Calculate T """
M = []#np.zeros(12, dtype='int64')
T_div_T0 = np.zeros(12)
log2 = np.zeros(12)
a_factor_list = np.zeros(12)

for i in range (12):
    M.append(np.random.randint(1e6, 5e6))
    heap_list = np.random.randint(random_numbers_range[0], random_numbers_range[1], M[i])
    heap = Kopiec(heap_list)

    t1 = time.time()
    heap.sort()
    t2 = time.time()
    T = t2 - t1
    if heap.check_sort() == 0:
        break

    a_factor_list[i] = (np.log2(T / (T0 * np.log2(M[i])))) / (np.log2(M[i]))
    T_div_T0[i] = T / T0

a_factor = np.mean(a_factor_list)
print("a =", a_factor)

slope, intercept, r_value, p_value, std_err = stats.linregress(T_div_T0, M)

plt.plot(T_div_T0, M, '.', label = 'Original data')
plt.plot(T_div_T0, intercept + slope*T_div_T0, '-', label = 'Fitted line')
plt.xlabel("T / T0")
plt.ylabel("M")
plt.legend()
plt.show()
