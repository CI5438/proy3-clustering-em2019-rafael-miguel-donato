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
def calcularCentro(cluster, centroActual):
    centro = []
    if len(cluster) > 0:
        for i in range(len(cluster[0])):
            punto = 0
            for k in range(len(cluster)):
                punto += cluster[k][i]
            centro.append(punto/len(cluster))
        return centro
    # Si el cluster esta vacio
    else:
        return centroActual

def KMeans(data, k=2):

	# Iniciamos los centros a puntos aleatorios del conjunto de datos
	centros = [ np.ndarray.tolist(data.iloc[randint(0,len(data)-1)].values) for i in range(k) ]

	# Iteramos hasta que los centros no cambien
	centrosCambian = True
	while(centrosCambian):
	    centrosCambian = False

	    clusters = [ [] for i in range(k) ]

	    # Calculo el cluster al que pertenece cada dato
	    for dato in range(len(data)):
	        cluster = calcularCluster(data.iloc[dato], centros)
	        clusters[cluster].append(data.iloc[dato])

	    # Recalculo los centros
	    nuevosCentros = [ calcularCentro(clusters[cluster], centros[cluster]) for cluster in range(len(clusters)) ]

	    if nuevosCentros != centros:
	        centrosCambian = True
	        centros = nuevosCentros

	return clusters, centros