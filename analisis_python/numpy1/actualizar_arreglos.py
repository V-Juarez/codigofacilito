# coding: utf-8
import numpy as np
a = np.arange(0, 10)
a
a[5] = 100 #modificando al arreglo 
a
a[0:4] = 20  # modificando varios arrreglos
a
a[ [4, 6, 7] ] = 10 #Remplazar mediante una lista de indices
a
np.append(a, 50)
a = np.append(a, 50) #agregar elementos a nuestro arreglo
a
np.delete(a, 5) 
a = np.delete(a, 5) #Elimina elementos del arreglo
a
np.append(a, 80) #agrega un nuevo elemento, pero no nodifica el arreglo
np.append(a, [500, 400] ) #agrega nuevos elementos y modifica el arreglo
