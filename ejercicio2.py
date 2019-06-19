import pandas
from kmeans import *
# Se lee el archivo con la entrada.
print("Leyendo Dataset...")
data = pd.read_csv("iris.data", sep=",", header=None)


# Separamos el target y lo transformamos a String.
target = pd.DataFrame(data.iloc[:,-1]).astype(str)
data = data.drop(data.columns[-1], axis=1)


clusters = KMeans(data, target, k=2)

print(clusters)