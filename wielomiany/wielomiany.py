import numpy as np
import random
import matplotlib.pyplot as plt
import copy

# poly = polynomial

class Polynomials (list):
    """ Add two polynomials """
    def add_poly(poly_1, poly_2): 
        max_len = len(poly_1)
        if len(poly_2) > len(poly_1):
            max_len = len(poly_2)
            
        poly_3 = np.zeros(max_len)
        
        for i in range (0, len(poly_1)):
            poly_3[i] = poly_1[i]
        for i in range (0, len(poly_2)):
            poly_3[i] += poly_2[i]
            
        return poly_3

    """ Subtract two polynomials """
    def sub_poly(poly_1, poly_2):
        max_len = len(poly_1)
        if len(poly_2) > len(poly_1):
            max_len = len(poly_2)
            
        poly_3 = np.zeros(max_len)
        
        for i in range (0, len(poly_1)):
            poly_3[i] = poly_1[i]
        for i in range (0, len(poly_2)):
            poly_3[i] -= poly_2[i]

        return poly_3

    """ Multiply two polynomials using FFT """
    def mult_poly (poly_1, poly_2):
        pad_1 = Polynomials._pad_with_zeros(poly_1, len(poly_1) + len(poly_2) - 1)
        pad_2 = Polynomials._pad_with_zeros(poly_2, len(poly_1) + len(poly_2) - 1)

        while not (Polynomials._is_pow_of_2(len(poly_1)) and Polynomials._is_pow_of_2(len(poly_2))):
            pad_1.append(0)
            pad_2.append(0)

        fft_1 = np.fft.fft(pad_1)
        fft_2 = np.fft.fft(pad_2)

        poly_3 = []
        for i in range (0, len(fft_1)):
            poly_3.append(fft_1[i] * fft_2[i])

        poly_3 = np.real(np.fft.ifft(poly_3))
        return poly_3

    """ Fill with zeros consecutive tpolynomial's factors """
    def _pad_with_zeros(poly, length):
        padded_poly = copy.copy(poly)
        while True:
            padded_poly.append(0)
            if len(padded_poly) == length:
                return padded_poly

    """ Check if the number is the power of 2 """
    def _is_pow_of_2(number):
        while (((x % 2) == 0) and (x > 1)):
            x /= 2
        if x == 1:
            return True
        else:
            return False
