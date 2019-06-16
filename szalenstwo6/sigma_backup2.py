
import scipy.special as ss
import numpy as np
import math

C_value = [0.75, 0.95]
p = 0.50
table_values = np.array(([]))

for C in C_value:
    l_M = []
    N_begin = math.ceil((np.log10(1 - C)) / (np.log10(1 - p)))
    N_finish = 100

    for N in range(0, N_begin):
        l_M.append("-")

    for N in range(N_begin + 1, N_finish + 1):
        m_value = int(N / 2)
        if m_value == N / 2:
            m_value -= 1

        for m in range(m_value, 0, -1):
            sum = 0

            for k in range(m - 1):
                sum += ss.binom(N, k) * (1 / 2 ** N)

            temp = float(1 - 2 * sum)

            if temp >= C:
                print(
                    "N = {0:3}, temp = {1:10.5}, m = {2:3}, m_value = {3:3}".format(
                        N, temp, m, m_value
                    )
                )
                l_M.append(m)
                break
            else:
                continue
    if table_values.size <= 0:
        table_values = np.array((l_M))
    else:
        table_values = np.array((table_values, l_M))

print(table_values)
