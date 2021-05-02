def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number-1) + fibonacci(number-2)

def palindromo(sentence):
    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]

def factorial(number):
    if number == 0: return 1
    else: return number * factorial(number-1)
