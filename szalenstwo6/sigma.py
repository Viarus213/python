#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Viarus

import scipy.special as ss
import numpy as np
import math
import csv

# Confidence level
C_value = [0.80, 0.97]
# Percintile
p = 0.10

N_finish = 100
l_M = [[], []]
l_P = [[], []]

for C in C_value:
    if C == C_value[0]:
        iter_list = 0
    elif C == C_value[1]:
        iter_list = 1

    for N in range(1, N_finish + 1):
        m_value = int(N / 2)

        if m_value == N / 2:
            m_value -= 1

        if m_value == 0:
            l_M[iter_list].append("-")
            l_P[iter_list].append("-")

        ########################################################################
        # Count the M
        ########################################################################
        for m in range(m_value, 0, -1):
            sum_m = 0

            for k in range(m):
                sum_m += ss.binom(N, k) * (1 / 2 ** N)

            temp = float(1 - 2 * sum_m)

            if temp >= C:
                l_M[iter_list].append(m)
                break

            # Protection, if it never get the required confidence
            elif temp < C and m == 1:
                l_M[iter_list].append("-")

        ########################################################################
        # Count the P_10
        ########################################################################
        for m in range(m_value, 0, -1):
            sum_p = 0

            for k in range(m):
                sum_p += ss.binom(N, k) * (p ** k) * ((1 - p) ** (N - k))

            temp = float(1 - sum_p)

            if temp >= C:
                l_P[iter_list].append(m)
                break

            # Protection, if it never get the required confidence
            elif temp < C and m == 1:
                l_P[iter_list].append("-")

################################################################################
# Create CSV file, allows to generate the pdf
################################################################################
with open("sigma.csv", "w") as csvfile:
    fieldnames = ["N", "M 80%", "M 97%", "P 80%", "P 97%"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(l_M[0])):
        writer.writerow(
            {
                "N": i + 1,
                "M 80%": l_M[0][i],
                "M 97%": l_M[1][i],
                "P 80%": l_P[0][i],
                "P 97%": l_P[1][i],
            }
        )
