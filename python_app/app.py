#
# Mandelbrotfractal--on Spark
#
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from pyspark import SparkContext

c = -0.73+0.19j

# p --griddla ktoregopoliczymy fraktal
def julia_calculate(p):
    maxit = 500
    #c = -0.73+0.19j #-0.10+0.65j
    global c
    z = p
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z ** 2 + c
        diverge = z * np.conj(z) > 2 ** 2  # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i  # note when
        z[diverge] = 2  # avoi ddiverg. too much

    return divtime


# c --griddla ktoregopoliczymy fraktal
def mandelbrot_calculate(p):
    maxit = 100
    z = p
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z ** 2 + p
        diverge = z * np.conj(z) > 2 ** 2  # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i  # note when
        z[diverge] = 2  # avoi ddiverg. too much

    return divtime

if __name__ == "__main__":

    #zmienne, które będą wczytywane z jsona
    fraktalOption = "julia"                     #"mandelbrot" / "julia"#
    c = -0.10+0.65j                             #liczba zespolona
    h = 3000                                    #rozdzielczosc y
    w = 3000                                    #rozdzielczosc x
    p1 = -1.5                                   #obszary generowania obrazu
    p2 = -1.5
    k1 = 1.5
    k2 = 1.5
    #dodatkowo ewentualnie jakieś kolory
    ##########

    context = SparkContext("local", "first app")


    y, x = np.ogrid[p1:k1:h * 1j, p2:k2:w * 1j]
    grid = x + y * 1j  # gridh x w punktow

    #print(grid)

    t0 = time.time()

    grid_rdd = context.parallelize(grid, 2)  # stworzenie RDD z 2 partycjami

    if fraktalOption == "julia":
        grid_rdd2 = grid_rdd.map(julia_calculate) # stworzenie kolejnego RDD na podstawie istniejącego RDD, dla każdego elementu z grid_rdd wykonywana jest funkcja julia_calculate
    elif fraktalOption == "mandelbrot":
        grid_rdd2 = grid_rdd.map(mandelbrot_calculate)

    fractal = grid_rdd2.collect()  # collect() --zbieramy wyniki do drivera

    t1 = time.time()

    context.stop()

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("\n\nElapsedtime: {} s\n\n".format(t1 - t0))

    plt.imshow(fractal)
    plt.show()
    plt.savefig("dane.png")
