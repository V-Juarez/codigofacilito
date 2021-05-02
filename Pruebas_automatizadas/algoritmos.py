"""
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120

>>> recursivo.factorial(13)
6227020800
"""

def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number-1)+ fibonacci(number-2)

def palindromo(sentence):
    """Retorna verdadero si el palindromo es un palindromo
    en caso contrario retorna flaso

    sentence -- String o entero

    >>> palindromo("anita lava la tina")
    True

    >>> palindromo(12321)
    True

    >>> palindromo("codigofacilito")
    False
    """

    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]


class Recursivo:
    def factorial(self, number):
        if number == 0: return 1
        else: return number*self.factorial(number-1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile("test1.txt")
