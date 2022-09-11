hora = int(input('Digite a hora atual: '))

if (hora >= 0 and hora <= 11) or hora == 24:
    print('Bom dia')
elif hora >= 12 and hora <= 17:
    print('Boa tarde')
elif hora >= 18 and hora <=23:
    print('Boa noite')
else:
    print('Horario inválido.')
