#!/usr/bin/env python
# -*- coding: utf-8 -*-


lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
print(len(lista_cursos))

lista_cursos_2 = ['C', 'C++', 'Heruko']

lista_cursos.append('JavaScript')
lista_cursos.append('JavaScript')
lista_cursos.append('C#')
lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'PyGame')

lista_cursos.extend(lista_cursos_2)


print(lista_cursos)
print(lista_cursos_2)
print(len(lista_cursos))

#  eliminar

lista_cursos.remove('Ruby')
del lista_cursos[0]
lista_cursos.clear()
print(lista_cursos)
print(lista_cursos)

