# coding: utf-8
pd.read_csv('users.csv')
df = pd.read_csv('users.csv')
df
df.head()
df.head(10)
df.tail()
df.tail(10)
df.head()   #Obtenemos los primeros registros
df.tail()  #obtenemos los ultimos registros
df = pd.read_csv('users.csv', delimiter=';')
df = pd.read_csv('users.csv', delimiter=';', header=5)
df
usersdf = pd.read_csv('users.csv', delimiter=';', header=5)
pd.read_csv('paises.csv')
pd.read_csv('paises.csv', usecols=['pais', 'poblacion', 'long', 'lat'])
pd.read_csv('paises.csv', usecols=['pais', 'poblacion', 'long', 'lat'], na_values=['N/S'])
paisesdf = pd.read_csv('paises.csv', usecols=['pais', 'poblacion', 'long', 'lat'], na_values=['N/S'])    #na_values=[] los archivos N/S a NaN
pisesdf
paisesdf
paisesdf[ paisesdf.poblacion.notnull() ]
paisesdf.poblacion
paisesdf.poblacion.values
paisesdf
paisesdf.apply( lambda row: row['problacion'], axis=1 )
paisesdf.apply( lambda row: row['problacion'] , axis=1)
paisesdf.apply( lambda row: row['poblacion'] , axis=1)
paises = paisesdf[ paisesdf.poblacion.notnull() ]
paises
paises.apply( lambda row: int(str(row['poblacion']).replace('.', '.')) , axis=1)
paises.apply( lambda row: int(str(row['poblacion']).replace('.', '')) , axis=1)
paises.poblacion = paises.apply( lambda row: int(str(row['poblacion']).replace('.', '')) , axis=1)
paises
