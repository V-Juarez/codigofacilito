# coding: utf-8
import numpy as np 
import pandas as pd
# loc
usuarios = {
'nombre': ['Eduardo', 'Victor', 'Alex', 'Fernando', 'Raul'],
'edad': np.random.randint(15, 30, 5),
'calificacion': np.random.randint(5, 10, 5),
'email': ['eduardo@puntocrea.com', 'victor@puntocrea.com', 'alex@puntocrea.com', 'feer@puntocrea.com', 'raul@puntocrea.com']
}
pd.DataDrame(usuarios)
pd.DataFrame(usuarios)
pd.DataFrame(usuarios, index=list('abcde'))
df
df = pd.DataFrame(usuarios, index=list('abcde'))
df
df['edad']
df.loc['a']
df.loc['b']
df.loc['a':'c']
df.loc['a':'c', 'nombre']
df.loc['a':'c', ['nombre', 'edad'] ]
df.loc[ df.calificacion > 5 ]
df.loc[ df.calificacion > 5 'nombre' ]
df.loc[ df.calificacion > 5, 'nombre' ]
df.loc[ df.calificacion > 5, ['nombre', 'edad'] ]
# consultas
df.loc[ df.calificacion > 5, ['nombre', 'edad', 'calificacion'] ]
df.loc[ df.calificacion > 5, ['nombre', 'edad', 'calificacion'] ].sort_values('calificacion')
df.loc[ df.calificacion > 5, ['nombre', 'edad', 'calificacion'] ].sort_values('calificacion', ascending=False)
df.loc[ df.calificacion > 5, ['nombre', 'edad', 'calificacion'] ].sort_values('calificacion', ascending=False).head(3)
df
#iloc -> obtener informacion
df.loc['a']
df.iloc['a']
df.iloc[0]
df.iloc[a]
df.iloc3
a]
df.iloc[0:4]
df.iloc[0:4, 0]
df.iloc[0:4, [0, 2] ]
#usar loc 
