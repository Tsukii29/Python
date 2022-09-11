nome = 'Braga'
idade = 20
altura = 1.83
peso = 65
ano_atual = 2022
ano_nascimento = 2022-idade
imc = peso/altura**2
print('{} tem {} anos, {} de altura e peso {}kg.'.format(nome, idade, altura, peso))
print('o IMC de {} é {:.2f}'.format(nome, imc))
print('{} nasceu em {}'.format(nome, ano_nascimento))
