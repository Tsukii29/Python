"""
utilizando o WHILE
cnt_prog = 0
cnt_regr = 10

while cnt_regr >= 0:
    print('Contador progressivo = {} \nContador regressivo = {} \n'.format(cnt_prog, cnt_regr))
    cnt_regr -= 1
    cnt_prog += 1
"""

for prog, regr in enumerate(range(10, 1, -1)):
    print(prog, regr)
