# coding: utf-8
import numpy as np 
lista = [10, 20, 30, 40, 50, 60]
type(lista)
np.array( lista )
a = np.array( lista )
a
type(a)
get_ipython().run_line_magic('clear', '')
a
a.ndim
a.size
a.itemsize
a.shape
a
a[0]
a[5]
a[a.size - 1]
a[55]
a[1:5]
a[1:5:2]
a[::-1]
lista = [0, 3, 4, 5 ]
for i in lista:
    print(a[i])
    
a[ lista ]
a[ [0, 0, 3, 4] ]
a
a * 10
((a * 10) - 10) / 2
a[0]
a[ [0, 0, 1, 2, 3] ]
