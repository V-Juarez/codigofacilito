# coding: utf-8
pd.DataFrame( np.arange(16).reshape(4,4) )
pd.DataFrame( np.arange(16).reshape(4,4), columns=list('abcd') )
pd.DataFrame( np.arange(16).reshape(4,4), columns=list('ABCD') )
pd.DataFrame( np.arange(16).reshape(4,4), columns=list('ABCD'), index=list('abcd') )
df = pd.DataFrame( np.arange(16).reshape(4,4), columns=list('ABCD'), index=list('abcd') )
df
df['B']
df.B
df.B['b']
df.B[1]
df.B['b'] = 50
df
# actualizar una columna completa
df
df.B = 10, 20, 30, 40
df
# Eliminar una columna
df.drop('D', axis=1)
df
# Eliminar una fila
df.drop('b', axis=1)
df.drop('b', axis=0)
df.insert(1, 'Z', [100, 200, 300, 400]) #Insertar una columna
df
# inser modifica los elementos
df.assign(z=[100, 200, 300, 500])
#assign genera un nuevo datafram y no modifica
