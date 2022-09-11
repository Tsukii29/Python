"""
Esse programa valida um CPF com base no algoritmo
de soma para os 2 ulimos digitos do mesmo.
Ex de cpf válido: 16899535009
"""

print('Bem vindo ao validador de cpf!')
cpf = input('Digite seu cpf: ').strip()

if not cpf.isdigit():
    print("Voce precisa digitar apenas numeros. ")
elif len(cpf) != 11:
    print('O cpf deve ser constituido de 11 digitos.')
else:
    cpfi = cpf
    cpf = list(cpf)

    a_somar = []
    for cnt, r in enumerate(range(10, 1, -1)):
        a_somar.append(int(cpf[cnt]) * r)

    soma = 0
    for valor in a_somar:
        soma += valor

    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0

    a_somar.clear()
    for cnt, r in enumerate(range(11, 1, -1)):
        a_somar.append(int(cpf[cnt]) * r)

    soma = 0
    for valor in a_somar:
        soma += valor

    digito_2 = 11 - (soma % 11)
    if digito_2 > 9:
        digito_2 = 0

    if int(cpf[-2]) == digito_1 and int(cpf[-1]) == digito_2:
        print('O cpf {} é válido'.format(cpfi))
    else:
        print('O cpf {} ñ é válido'.format(cpfi))
