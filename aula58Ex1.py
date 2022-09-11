"""
Crie uma função que recebe uma função como parametro
e retorne o valor da função dois executada.
"""


def f1(func2):
    return func2


def f2():
    return 31


a = f1(f2())
print(a)
