"""
Crie uma função1 que recebe uma função2 como parametro
e retorne o valor da função2 executada.
Faça a função1 executar funções que recebam um numero
diferente de argumentps
"""


def f1(*args):
    return args


def f2():
    return 34


def f3():
    return 23, 41


a = f1(f2())
b = f1(f3())
print(*a)
print(*b)
