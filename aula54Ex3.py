"""
Crie uma função que receba 2 números.
O primeiro é um valor e o segundo é um percentural
Retorne o valor do primeiro numero somado do aumento do percentural do mesmo
"""


def aumento(num, taxa):
    num += num*taxa/100
    return num


a = float(input('Digite um numero: '))
b = float(input('Digite uma porcentagem: '))
novo_num = aumento(a, b)
print('O numero acrescido de sua porcentagem é:', novo_num)
