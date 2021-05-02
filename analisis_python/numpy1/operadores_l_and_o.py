# coding: utf-8
a = np.arange(10)
a
b = a
a
b
b[0] = 100 #Referencia de a, ambos se ejecutan
a
id(a)
id(b)
# a y b se tratan del mismo objeto
a is b
b[1] = 50
a[4] = 345
a
a.view()
c = a.view()
c
c # vista
id(c)
id(a)
a is c
c[0] = 200
a
c.base
b.base is a
c.base is a
id(c.base)
id(a)
a[0] = 90
c
c.base
a.flags
c.flags
c[0] = 50
a
a[1:7]
d = a[1:7]
d[0] =55
a
d.base
d.flags
s.copy()
e = a.copy()
e is a
e.base
e.flags
e[0] = 90
a
b
c
d
e
i
j
k
c.base is a
d 
d.base is a
e
es is a
e is a
e.base
e.flags
