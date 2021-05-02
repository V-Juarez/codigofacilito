# coding: utf-8
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
