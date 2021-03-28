# Simule um caixa eletronico. Perguntar o valor da ser sacado (INT) o
# programa vai informar quantas cédulas de cada valor serão entregyes. Condierar 50, 20, 10 e 1     c
soma = res = notas1 = notas10 = notas20 = notas50 = 0
while True:
    sacar = int(input('Que valor você quer sacar? R$'))
    u = sacar // 1 % 10
    d = sacar // 10 % 10
    c = sacar // 100 % 10
    m = sacar // 1000 % 10
    if u >= 1:
        notas1 = u*1
        print(f'Serão {notas1} notas de R$1.00')
    if d >= 1:
        if d % 2 == 0:   # PAR
            notas20 = d / 2
            print(f'Serão {notas20} notas de R$20.00')

        elif d % 2 == 1:    # corrigir
            notas20 = d//2
            notas10 = notas20 - d
            print(f'Será 1 nota de R$10.00')
    if c >= 1:
        centena = c*2
    if m >= 1:
       milhar = m*20
    nota50 = centena + milhar
    print(f'Serão {nota50} notas de R$50.00')




