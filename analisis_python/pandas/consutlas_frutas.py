# coding: utf-8
frutas = {
'nombre': ['Naranja', 'Manzana', 'Manzana', 'Pera', 'Naranja', 'Pera', 'Naranja', 'Sandia'],
'color': ['Naranaja', 'Rojo', 'Rojo', 'Verde', 'Naranja', 'Verde', 'Naranja', 'Rojo'],
'cantidad': np.random.randint(5, 10, 8),
'precio': np.random.randint(1, 5, 8)
}
df = pd.DataFrame(frutas)
df
# registros duplicados
df.groupby('nombre')
df.groupby('nombre').cantidad.sum()
df.groupby('nombre').cantidad.sum().to_frame('cantidad')
df
df.groupby('nombre')
df.groupby('nombre').filter( lambda fruta: fruta.cantidad.sum() > 5  )
df.groupby('nombre').filter( lambda fruta: fruta.cantidad.sum() > 10  )
df.groupby('nombre').filter( lambda fruta: fruta.cantidad.sum() > 12  )
df.groupby('nombre').filter( lambda fruta: fruta.cantidad.sum() > 15  )
df.groupby('nombre').filter( lambda fruta: fruta.cantidad.sum() > 15  ).groupby('nombre').cantidad.sum()
df.groupby('nombre').filter( lambda fruta: fruta.cantidad.sum() > 10  ).groupby('nombre').cantidad.sum()
df[ df.nombre == 'manzana'  ]
df[ df.nombre == 'Manzana'  ]
df[ df.nombre == 'Manzana'  ].group('color')
df[ df.nombre == 'Manzana'  ].groupby('color')
df[ df.nombre == 'Manzana'  ].groupby('color').cantidad.sum()
