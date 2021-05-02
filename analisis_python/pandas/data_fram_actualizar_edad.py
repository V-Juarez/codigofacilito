# coding: utf-8
# %load remonbrar.py
np.arange(12)
np.arange(12).reshape(3, 4)
a = np.arange(12).reshape(3, 4)
a
df = pd.DataFrame(a)
df
df = pd.DataFrame(a, columns=['A', 'B', 'C', 'D'])
df
df = pd.DataFrame(a, columns=['A', 'B', 'C', 'D'], index=['a', 'b', 'c', 'd'])
df = pd.DataFrame(a, columns=['A', 'B', 'C', 'D'], index=['a', 'b', 'c'])
df
df.columns = 'AB', 'BB', 'CB', 'DB' #remonbrar las columnas
df
df.index= '1a', '2b', '3c' #renombrar las filas
df
df.rename( columns={'AB': 'ab'} )
df.rename(index={'1a': '1A'} )
df.columns
df.index
get_ipython().run_line_magic('clear', '')
get_ipython().run_line_magic('load', 'data_frame.py')
# %load data_frame.py
# pd.DataFrame()
usuarios = {
'nombre': ['Victor', 'Carlos', 'Eduardo', 'Edy'],
'calificaciones': [9, 10, 8.5, 9.5],
'edad': [27, 25, 30, 22]
'aprobado': [True, True, False, True]
}
usuarios = {
'nombre': ['Victor', 'Carlos', 'Eduardo', 'Edy'],
'calificaciones': [9, 10, 8.5, 9.5],
'edad': [27, 25, 30, 22],
'aprobado': [True, True, False, True]
}
usuarios
ps.DataFrame(usuarios)
import pandas as pd
pd.DataFrame(usuarios)
pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd'])
usuarios = {
'nombre': ['Victor', 'Carlos', 'Eduardo', 'Edy'],
'calificacion': [9, 10, 8.5, 9.5],
'edad': [27, 25, 30, 22],
'aprobado': [True, True, False, True]
}
pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd'])
a = pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd'])
a
a['nombre']
a.nombre
a
a.calificacion
a.calificacion.values
a.colums
a.columns
a.index
a.values
a.values
a.values.admin
a.values.adim
a.values.ndim
a
usuarios = { 
'nombre': ['Victor', 'Carlos', 'Eduardo', 'Edy'], 
'calificacion': [9, 10, 8.5, 9.5], 
'edad': [27, 25, 30, 22], 
'aprobado': [True, True, False, True] 
} 
pd.DataFrame(usuarios)
pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd']) 
df = pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd']) 
df
df
cler
get_ipython().run_line_magic('clear', '')
df
# apply
df.apply(lambda row['edad'] + 1, axis=1)
df.apply(lambda row: row['edad'] + 1, axis=1)
df.edad = df.apply(lambda row: row['edad'] + 1, axis=1)  #actualizar los datos  de la tabla
df
