"""
Fizz Buzz
se o parametro da função for divisisvel por 3, retorne fizz
se o parametro da função for divisisvel por 5, retorne buzz
se o parametro da função for divisisvel por 3 e 5, retorne fizzbuzz
caso contrario, retorne o numero enviado
"""


def fb(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'Fizz Buzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    return numero


num = float(input('Digite um numero: '))
resultado = fb(num)
print(resultado)
