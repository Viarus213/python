import numpy as np
import random
import matplotlib.pyplot as plt
import copy
import math
import time


class Wielomian(list):
    """ Add two polynomials """

    def add_poly(poly_a, poly_b):
        max_len = len(poly_a)
        if len(poly_b) > len(poly_a):
            max_len = len(poly_b)

        poly_c = np.zeros(max_len)

        for i in range(0, len(poly_a)):
            poly_c[i] = poly_a[i]
        for i in range(0, len(poly_b)):
            poly_c[i] += poly_b[i]

        return poly_c

    """ Subtract two polynomials """

    def sub_poly(poly_a, poly_b):
        max_len = len(poly_a)
        if len(poly_b) > len(poly_a):
            max_len = len(poly_b)

        poly_c = np.zeros(max_len)

        for i in range(0, len(poly_a)):
            poly_c[i] = poly_a[i]
        for i in range(0, len(poly_b)):
            poly_c[i] -= poly_b[i]

        return poly_c

    """ Multiply two polynomials using FFT """

    def mult_poly(poly_a, poly_b):
        pad_A = Wielomian._pad_with_zeros(poly_a, len(poly_a) + len(poly_b) - 1)
        pad_B = Wielomian._pad_with_zeros(poly_b, len(poly_a) + len(poly_b) - 1)

        while not (
            Wielomian._is_pow_of_2(len(poly_a)) and Wielomian._is_pow_of_2(len(poly_b))
        ):
            pad_A.append(0)
            pad_B.append(0)

        fft_A = np.fft.fft(pad_A)
        fft_B = np.fft.fft(pad_B)

        poly_c = []
        for i in range(0, len(fft_1)):
            poly_c.append(fft_1[i] * fft_2[i])

        poly_c = np.real(np.fft.ifft(poly_c))
        return poly_c

    """ Fill with zeros consecutive polynomial's factors """

    def _pad_with_zeros(poly, length):
        padded_poly = copy.copy(poly)
        while True:
            padded_poly.append(0)
            if len(padded_poly) == length:
                return padded_poly

    """ Check if the number is the power of 2 """

    def _is_pow_of_2(number):
        while ((number % 2) == 0) and (number > 1):
            number /= 2
        if number == 1:
            return True
        else:
            return False


# Draw number with the specified possibility
def draw_number(choices):
    total = sum(w for c, w in choices)
    rand = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= rand:
            if c == 10:
                return 0
            return c
        upto += w
    assert False, "Error, shouldn't be here."


def create_benfords_law(n):
    temp = 0
    for i in range(1, 11):
        temp += math.log10(1 + 1 / i)
    alpha = 1 / temp
    pn = alpha * math.log10(1 + 1 / n)
    return pn


benford_items = []
for i in range(0, 11):
    benford_items.append(create_benfords_law(i + 1))

items = []
it = np.arange(1, 11)
for a, b in zip(it, benford_items):
    items.append([a, b])

eq = []
N = np.arange(100, 1001, 100)  # Degree of a polynomial
mult_no = 5000  # Number of multiplications need to reach mult_time > 3s
times = np.zeros(len(N))
time_allow = np.zeros(len(N))

for i in range(len(N)):
    polynomials = np.zeros((2, N[i]))
    for j in range(0, N[i]):
        for k in range(0, 2):
            polynomials[k][j] = 0.1 * draw_number(items) + (0.1 * random.uniform(0, 1))
    x = list(polynomials[0])
    x1 = list(polynomials[1])
    t1 = time.time()
    for l in range(0, mult_no):
        eq = list(eq)
        eq = Wielomian.mult_poly(x, x1)
    t2 = time.time()
    times[i] = t2 - t1

x0 = np.array([1, 1])
res = optimize.least_squares(fun, x0, args=(N, times))

y_test = model(res.x, N)

plt.plot(N, times, "o", label="Dane")
plt.plot(N, y_test, "r", label="Dopasowana krzywa")
plt.xlabel("Stopień wielomianu N")
plt.ylabel("Czas x-krotnego mnożenia")
plt.legend()
plt.show()

print("Współczynnik a =", res.x[0])
print("Współczynnik b =", res.x[1])
