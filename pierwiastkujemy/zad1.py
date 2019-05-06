import random
import numpy as np
import matplotlib.pyplot as plt
import math

def root_function (a):
    buffer = float(a)
    iteration = 0
    while 1:
        iteration += 1
        result = 1/2*(buffer + a/buffer)
        if (buffer - result) == 0:
            return iteration
        else:
            buffer = result
        
L = 100
min_iteration_array = []
max_iteration_array = []
c_array = np.arange(-300,301,1)

for c in (c_array):
    first_loop = 1
    
    for i in range (L):
        m = random.random ()
        a = m*math.pow(10, c)
        
        iteration_no = root_function (a)
        
        if first_loop:
            iter_buffer_min = iteration_no
            iter_buffer_max = iteration_no
            first_loop = 0
        else:
            if iteration_no < iter_buffer_min:
                iter_buffer_min = iteration_no # No. of min iterations changed
            elif iteration_no > iter_buffer_max:
                iter_buffer_max = iteration_no # No. of max iterations changed

    min_iteration_array = np.append (min_iteration_array, iter_buffer_min)
    max_iteration_array = np.append (max_iteration_array, iter_buffer_max)

plt.plot (c_array, min_iteration_array, label = "Min. no. of iterations")
plt.plot (c_array, max_iteration_array, label = "Max. no. of iterations")

plt.xlabel ("c")
plt.ylabel ("No. of iterations")
plt.legend()
plt.show ()
