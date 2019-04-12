import random
import numpy as np
import matplotlib.pyplot as plt
import math

m_2_range = 100
L = 1000

m2_root_tab = []        # Set of 100 sqrt(m2)
double_m2_root_tab = [] # Set of 100 1/(2*sqrt(x0))

m2_array = []
iteration_array = []

m_2_tab = np.linspace (1., 9.9, m_2_range)

for k in range (m_2_range):
    m2_root_tab = np.append (m2_root_tab, math.sqrt (m_2_tab [k]))
    double_m2_root_tab = np.append (double_m2_root_tab, 1 / (2 * m2_root_tab [k]))
    
def root_function (a):
    iteration = 0
    border = math.pow (10, -15)
    
    ix = round (10*a) - 10
    x0 = m2_root_tab[ix]
    buffer = x0

    while 1:
        iteration += 1
        result = buffer + double_m2_root_tab[ix] * (a - buffer**2)

        if (abs (buffer - result) < border):
            return iteration
        else:
            buffer = result
        

for i in range (L):
    m_2 = random.uniform (1.0, 10.0)
    iteration_no = root_function (m_2)

    m2_array = np.append (m2_array, m_2)
    iteration_array = np.append (iteration_array, iteration_no)

plt.plot (m2_array, iteration_array, ".")
 
plt.xlabel ("m_2")
plt.ylabel ("No. of iterations")
plt.grid (True)
plt.show ()
