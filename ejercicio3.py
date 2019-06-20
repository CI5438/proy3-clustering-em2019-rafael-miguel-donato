from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from kmeans import *

# Nombre de la imagen, sin extension
img_name = 'gohan'

# Leemos la Imagen y la guardamos el color de cada pixel y su posicion como un ndarray 
colourImg = Image.open("%s.png"%img_name)
colourPixels = colourImg.convert("RGB")
colourArray = np.array(colourPixels.getdata()).reshape(colourImg.size + (3,))
indicesArray = np.moveaxis(np.indices(colourImg.size), 0, 2)
allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 5))

size = colourArray.shape

data = pd.DataFrame(allArray, columns=["y", "x", "red", "green", "blue"])

ks = [2, 4, 8, 16, 32, 64, 128]
for k in ks:
	print("K =", k)
	data = pd.DataFrame(allArray, columns=["y", "x", "red", "green", "blue"])

	print("Creando los clusters...")
	clusters, centros = KMeans(data, k=k)


	# Repintamos la imagen segun los centros de los clusters.
	for i in range(len(clusters)):
	    for j in clusters[i]:
	    	data.iloc[j.name] = centros[i]

	comp_img = np.reshape( data[['red', 'green', 'blue']].values, size ).astype('uint8') 

	# comp_img.resize((img.shape))


	img = Image.fromarray(comp_img, 'RGB')


	img.save('%s K%s.png'%(img_name, k))

