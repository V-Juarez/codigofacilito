#!/usr/bin/env python
# -*- coding: utf-8 -*-

def promedio(*args):
    return sum(args) / len(args)


def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))


#  usuarios(eduardo=[10, 10, 8], fernando=[9, 10, 10])

def conbinacion(*args, **kwargs):
    print(args)
    print(kwargs)

conbinacion(1, 2, 3, 4, 5, cody=True, curso='Python')
