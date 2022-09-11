"""
crie uma função que recebe 3 numeros como parametro e exiba a soma entre eles
"""


def soma(a, b, c):
    d = a + b + c
    return d


x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))
resultado = soma(x, y, z)
print('O resultado da soma é:', resultado)
