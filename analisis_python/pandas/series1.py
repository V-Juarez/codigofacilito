# coding: utf-8
import pandas as pd
import numpy as np
#pn.NaN
a = pd.Series( [10, 20, pn.NaN, 40, np.NaN] )
a = pd.Series( [10, 20, np.NaN, 40, np.NaN] )
a
pd.isnull(a)
pd.notnull(a)
a.isnull()
a.dropna()
a.dropna()   #crea una nueva serie, y no modifica la serie.
a = a.dropna()   #Eliminamos los valores NaN de la serie
a
a = pd.Series( [10, 20, pn.NaN, 40, np.NaN] )
a = pd.Series( [10, 20, np.NaN, 40, np.NaN] )
a
a.fillna(99)    #Genera una nueva serie
a[ a.notnull() ]  #obtenermos todos los elementos nulos
