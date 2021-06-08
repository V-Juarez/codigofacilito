#!/usr/bin/env python
# -*- coding: utf-8 -*-

def primedio(*args):
    return sum(args) / len(args)


def combinacion(p1, p2, *args, p4=5000):
    print(p1)
    print(p2)
    print(args)
    print(p4)


combinacion(10, 2, 5, 2, 6, 2, 20, 50, 30, p4=1000)
