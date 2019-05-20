#
# Mandelbrotfractal--on Spark
#
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import json
import urllib.request
import base64
from pyspark import SparkContext

c = -0.73 + 0.19j
maxit = 0


# p --griddla ktorego policzymy fraktal
def julia_calculate(p):
    global c, maxit
    # c = -0.73+0.19j #-0.10+0.65j
    z = p
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z ** 2 + c
        diverge = z * np.conj(z) > 2 ** 2  # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i  # note when
        z[diverge] = 2  # avoi ddiverg. too much

    return divtime


# p --griddla ktorego policzymy fraktal
def mandelbrot_calculate(p):
    global maxit
    z = p
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z ** 2 + p
        diverge = z * np.conj(z) > 2 ** 2  # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i  # note when
        z[diverge] = 2  # avoi ddiverg. too much

    return divtime


# TO DO: sprawdzić czy to tak ma być
def readJSON():
    import json
    import sys
    print(type(sys.argv[1]))
    print(sys.argv[1])
    data = json.loads(sys.argv[1].replace('\'', '"'))
    # data = input("JSON ze strony w formacie({ \"name\": \"julia\", \"maxIt\":200, \"re\":-0.10, \"im\":0.65, \"h\":300, \"w\":300, \"p1\":-1.5, \"p2\":-1.5, \"k1\":1.5, \"k2\":1.5 }): ")

    # with urllib.request.urlopen("jakis adres") as url:
    #    data = json.loads(url.read().decode())

    return data


# TO DO: sprawdzić czy to tak ma być
def sendJSON(jsonData):
    import requests
    myurl = "nasz url"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post('http://35.238.239.157:8000/results/', data=jsonData, headers=headers)

    # req = urllib.request.Request(myurl)
    # req.add_header('Content-Type', 'application/json; charset=utf-8')
    # response = urllib.request.urlopen(req, jsonData)


# name - nazwa fraktala, x,y- rozdzielczość, re,im - dla jakiej liczby zespolonej policzono fraktal, maxIt - maksymalna liczba iteracji, img - w formacie base64
def dataToJSON(name, x, y, liczbaZesp, maxIt, img):
    data = {
        "name": name,
        "x": x,
        "y": y,
        # "liczbaZespolona": liczbaZesp.__str__(),
        "maxit": maxIt,
        "image": img
    }

    jsonData = json.dumps(data)

    return jsonData


if __name__ == "__main__":

    y = {"name": "julia", "maxIt": 200, "re": -0.10, "im": 0.65, "h": 300, "w": 300, "p1": -1.5, "p2": -1.5, "k1": 1.5,
         "k2": 1.5}

    # y = readJSON()

    # zmienne, które będą wczytywane z jsona
    liczbaZesp = 0 + 0j
    liczbaZesp += y["re"]
    liczbaZesp += y["im"] * 1j
    fractalOption = y["name"]  # "mandelbrot" / "julia"#
    c = liczbaZesp  # liczba zespolona
    maxit = y["maxIt"]
    h = y["h"]  # rozdzielczosc y
    w = y["w"]  # rozdzielczosc x
    p1 = y["p1"]  # obszary generowania obrazu
    p2 = y["p2"]
    k1 = y["k1"]
    k2 = y["k2"]
    # dodatkowo ewentualnie jakieś kolory
    ##########

    context = SparkContext("local", "first app")

    y, x = np.ogrid[p1:k1:h * 1j, p2:k2:w * 1j]
    grid = x + y * 1j  # gridh x w punktow

    t0 = time.time()

    grid_rdd = context.parallelize(grid, 2)  # stworzenie RDD z 2 partycjami

    if fractalOption == "julia":
        grid_rdd2 = grid_rdd.map(
            julia_calculate)  # stworzenie kolejnego RDD na podstawie istniejącego RDD, dla każdego elementu z grid_rdd wykonywana jest funkcja julia_calculate
    elif fractalOption == "mandelbrot":
        grid_rdd2 = grid_rdd.map(mandelbrot_calculate)

    fractal = grid_rdd2.collect()  # collect() --zbieramy wyniki do drivera

    t1 = time.time()

    context.stop()

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("\n\nElapsedtime: {} s\n\n".format(t1 - t0))

    plt.imshow(fractal)
    plt.show()
    plt.axis('off')
    fractal.axes.get_xaxis().set_visible(False)
    fractal.axes.get_yaxis().set_visible(False)
    plt.savefig("fraktal.png", bbox_inches='tight', pad_inches=0)

    with open("fraktal.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('ascii')  # obraz do base64

        print("obraz po enkodzie:", encoded_string)

        jsonToSend = dataToJSON(fractalOption, w, h, liczbaZesp, maxit, encoded_string)

        print("Json do wysłania:", jsonToSend)

        # wysłanie JSONA
        sendJSON(jsonToSend)
