import numpy as np
import matplotlib.pyplot as plt


SubplotPos = 131
PlotColor = (['red', 'green', 'violet'])
LamVal = ([1., 2., 10.])

for i in range (3):
    PoisDist = np.random.poisson (lam = (LamVal[i]), size = (10000))
    plt.subplot (SubplotPos)
    SubplotPos += 1
    plt.xscale ('linear', linthreashy = 4)
    plt.axis ([0, 20, 0, 0.4])
    plt.subplots_adjust (wspace = 1)
    plt.hist (PoisDist, 20, range = (0, 20), density = 1, rwidth = 0.3, color = PlotColor[i], label = "L = " + str(LamVal[i]))
    plt.legend()
    plt.xlabel ("n")
    plt.ylabel ("P(n)")

plt.show ()
