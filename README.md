### CI5438 - EM2019

# Proyecto 3

## Clustering

### Resumen

El clustering o aglomeración  es una un subconjunto de algoritmos de aprendizaje no supervisado. Hay dos tipos de clustering: el jerárquico el no jerárquico. El algoritmo k-means es el más usado del los no jerarquicos. El objetivo de este proyecto es que el estudiante implemente dicho algoritmo y se familiarice con su uso. Para ello se pide que implementen k-means en el lenguaje imperativo de su preferencia; para luego evaluar esa implementación sobre 2 problemas: la compresión de una imágen , y el como separa los ejemplos (con etiquetas conocidas) del Iris Dataset .


### Actividades

1. Implemente el algoritmo de k-means en el lenguaje imperativo de su preferencia.

2. Pruebe su algoritmo sobre los siguientes dominios de aplicación:

	- 2.1. Para explorar los datos del conjunto Iris Data Set (http://archive.ics.uci.edu/ml/datasets/Iris).

		Pruebe para K = {2,3,4, 5}. Visualice si los clusters encontrados coinciden con las etiquetas de los ejemplos. Qué observa?

		Para K = 2 y K = 3, Calcule la diferencia entre los clusters y las etiquetas reales. Qué observa?

		Recuerden que el resultado de K-means depende a la inicialización, por lo que deben probar varias corridas para el mismo K (mínimo 5). Deben reportar los resultados de cada corrida, los promedios, el mejor caso y el peor caso.

	- 2.2. Para realizar la compresión de una imagen de su preferencia.

		En este caso cada pixel en la imagen original es un ejemplo, que será asignado en la imagen comprimida al cluster k_i . K será el número de colores en la imagen comprimida. Pruebe para K= {2, 4, 8, 16, 32, 64, 128}. Guarde las imagenes resultantes (y la original) en una carpeta. Si el nombre de la original es Imagen.png , el de las resultantes debe ser Imagen K[NumeroK].png



### Entrega

La fecha de entrega *tentativa* es el día Miércoles 4 de Junio, a media noche.

En el directorio de github de su grupo deberán incluir: su código, la carpeta de imágenes (con las imágenes dentro) y su informe. 


El informe debe ser breve y conciso, debe incluir:

- Resumen. 
- Detalles de implementación/experimentación. (Lenguaje usado, detalles del algoritmo, etc). 
- Presentación y discusión de los resultados (En base a los elementos requeridos para cada conjunto de datos) 
- Conclusiones 
- Referencias
