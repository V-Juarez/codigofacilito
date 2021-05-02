# coding: utf-8
import pandas as pd
pd.Series( [10, 20, 30, 40, 50] )
a = pd.Series( [10, 20, 30, 40, 50] )
a
import numpy as np
a = pd.Series( [10, 20, 30, 40, 50], dtype=np.integer)
a
a = pd.Series( [10, 20, 30, 40, 50], dtype=np.float32)
a
a[0]
a[ a.size -1 ]
a[0] = 90.0
a
a = pd.Series( [10, 20, 30, 40, 50], dtype=np.float32, index=['a', 'b', 'c', 'd', 'e'])
a['a']
a
a [ ['a', 'c', 'd' ]]
diccionario = {
'a': 10,
'b': 200,
'c': 3000
}
b = pd.Series( diccionario ) 
b
b['a']
# Creacion de series
#nueva serie
a = pd.Series( np.arange(4) )
a
a = pd.Series( np.arange(4), index=['a', 'b', 'c', 'd'] )
a
a = pd.Series( np.arange(4), index=['a', 'b', 'c', 'd'], dtype=np.float32 )
a
a['a']
a[0]
a.name = 'numeros'   #Colocarle un nombre a indice
a
a.index
a.index.values
a.index.tolist()
a.index.name = 'indices'  #la columna de poseera un nombre
a
b = a * 10 
b
b[ b > 15]
b[ (b > 15) | (b == 0) ]
