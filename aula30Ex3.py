nome = input('Digite seu primeiro nome: ')
nome = nome.capitalize()
qnt = len(nome)

if qnt < 5:
    print('{} é um nome muito curto'.format(nome))
if qnt == 5 or qnt == 6:
    print('{} é um nome normal'.format(nome))
if qnt > 6:
    print('{} é um nome muito grande'.format(nome))
