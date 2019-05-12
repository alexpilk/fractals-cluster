#
# Mandelbrotfractal--on Spark
#
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from pyspark import SparkContext


# p --griddla ktoregopoliczymy fraktal
def julia_calculate(p):
    maxit = 500
    c = -0.73+0.19j #-0.10+0.65j
    z = p
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z ** 2 + c
        diverge = z * np.conj(z) > 2 ** 2  # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i  # note when
        z[diverge] = 2  # avoi ddiverg. too much

    return divtime


if __name__ == "__main__":
    sc = SparkContext(appName="Julia-spark")

    h = 3000
    w = 3000
    y, x = np.ogrid[-1.5:1.5:h * 1j, -1.5:1.5:w * 1j]
    grid = x + y * 1j  # gridh x w punktow

    #print(grid)

    t0 = time.time()

    grid_rdd = sc.parallelize(grid, 2)  # stworzenie RDD z 2 partycjami
    grid_rdd2 = grid_rdd.map(julia_calculate) # stworzenie kolejnego RDD na podstawie istniejącego RDD, dla każdego elementu z grid_rdd wykonywana jest funkcja julia_calculate
    fractal = grid_rdd2.collect()  # collect() --zbieramy wyniki do drivera

    t1 = time.time()

    sc.stop()

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("\n\nElapsedtime: {} s\n\n".format(t1 - t0))

    plt.imshow(fractal)
    plt.show()
    plt.savefig("dane.jpg")
