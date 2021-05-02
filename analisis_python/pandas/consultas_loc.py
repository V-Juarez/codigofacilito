# coding: utf-8
import numpy as np
import pandas as pd
pd.read_csv('users.csv')
pd.read_csv('users.csv', usecols=['nombre', 'edad', 'genero', 'pais', 'email'])
df = pd.read_csv('users.csv', usecols=['nombre', 'edad', 'genero', 'pais', 'email'])
df
df[ df.edad > 20 ]
df[ df.edad > 20 ].nombre
df.loc[ df.edad > 20, 'nombre' ] #consulta con el atributo loc, recomendable. ya que se lee de una mejor manera
df.loc[ (df.edad > 20) & (df.genero == 'female') ]
df.loc[ (df.edad > 20) & (df.genero == 'female'), 'nombre' ]
df.loc[ df.email.str.endswith('@gmail.com') ]
df.loc[ ~ df.email.str.endswith('@gmail.com') ]
df.loc[ df.pais.isin(['Germany', 'Finland', 'Canada']) ]
df.loc[ (df.genero == 'female') ]
df.loc[ (df.genero == 'female') & (df.edad > 20) ]
df.loc[ (df.genero == 'female') ]
df.loc[ (df.genero == 'female') ]
df.loc[ (df.genero == 'female') & (df.edad > 20) & (df.pais.isin(['Germany', 'Finland', 'Canada'])) ]
df.loc[ (df.genero == 'female') ]
df.loc[ (df.genero == 'female') & (df.edad > 20) & (df.pais.isin(['Germany', 'Finland', 'Canada'])) ] 
df.loc[ (df.genero == 'female') & (df.edad > 20) & (df.pais.isin(['Germany', 'Finland', 'Canada'])), ['nombre', 'email'] ] 
df.sort_values('edad', ascending=False)
df.sort_values('edad', ascending=False).head(10)
