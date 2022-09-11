string = '012301230123012301230123012301230123012301230123012301230123012301230123'
# aux = ''
# lista = []
# for valor in string:
#     if len(aux) < 4:
#         aux += valor
#     if len(aux) == 4:
#         lista.append(aux)
#         aux = ''
# retorno_final = '.'.join(lista)
# print(retorno_final)
lista = [string[i:i + 4] for i in range(0, len(string), 4)]
print('.'.join(lista))
