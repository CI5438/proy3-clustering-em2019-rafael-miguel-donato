import pandas
from kmeans import *
# Se lee el archivo con la entrada.
print("Leyendo Dataset...")
data = pd.read_csv("iris.data", sep=",", header=None)


# Separamos el target y lo transformamos a String.
target = pd.DataFrame(data.iloc[:,-1]).astype(str)
data = data.drop(data.columns[-1], axis=1)

clusters = KMeans(data, target, k=5)

# print(clusters)

distribucion = {}
for k in range(len(clusters)):
    distribucion["clusters_"+str(k)] = {"Iris-setosa": 0, 
                                        "Iris-versicolor": 0,
                                        "Iris-virginica": 0}

for i in range(len(clusters)):
    for k in clusters[i]:
        distribucion["clusters_"+str(i)][target.iloc[k.name][4]] += 1

print(distribucion)