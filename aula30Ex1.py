num = input('Digite um numero inteiro: ')

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print('{} é um número par'.format(num))
    else:
        print('{} é um número ímpar'.format(num))
else:
    print('O valor digitado não é válido.')
