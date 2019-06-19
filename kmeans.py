# K means
from random import randint
from math import sqrt
import pandas as pd
import numpy as np

# Distancia euclideana entre dos puntos
def calcularDistancia(punto1, punto2):
    distancia = 0
    for i in range(len(punto1)):
        distancia += (punto1[i] - punto2[i])**2
    return  sqrt(distancia)

# Calcular el cluster al que pertenece un punto
def calcularCluster(punto, centros):
    minimo = 100000000
    cluster = -1
    for i in range(len(centros)):
        distancia = calcularDistancia(punto, centros[i])
        if distancia < minimo:
            cluster = i
            minimo = distancia
    return cluster

# Calcular el centro de un cluster
def calcularCentro(cluster):
    centro = []
    for i in range(len(cluster[0])):
        punto = 0
        for k in range(len(cluster)):
            punto += cluster[k][i]
        centro.append(punto/len(cluster))
    return centro


# Se lee el archivo con la entrada.
print("Leyendo Dataset...")
data = pd.read_csv("iris.data", sep=",", header=None)


# Separamos el target y lo transformamos a String.
target = pd.DataFrame(data.iloc[:,-1]).astype(str)
data = data.drop(data.columns[-1], axis=1)

# Numero de clusters
k = 2
# Iniciamos los centros a puntos aleatorios del conjunto de datos
centros = []
for i in range(k):
    centros.append(np.ndarray.tolist(data.iloc[randint(0,len(data)-1)].values))


# iteramos hasta que los centros no cambien
centrosCambian = True
while(centrosCambian):
    centrosCambian = False

    clusters = []
    for i in range(k):
        clusters.append([])

    # Calculo el cluster al que pertenece cada dato
    for dato in range(len(data)):
        cluster = calcularCluster(data.iloc[dato], centros)
        clusters[cluster].append(data.iloc[dato])

    # Recalculo los centros
    nuevosCentros = []
    for cluster in clusters:
        nuevosCentros.append(calcularCentro(cluster))

    if nuevosCentros != centros:
        centrosCambian = True
        centros = nuevosCentros

