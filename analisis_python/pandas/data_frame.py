# coding: utf-8
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
