"""
Crie uma função que exibe umas saudação
com os parametros saudação e nome
"""


def saud(saudacao, nome):
    print(saudacao, nome, sep=', ')


a = input('Digite uma saudação: ')
b = input('Digite um nome: ')
saud(a, b)
