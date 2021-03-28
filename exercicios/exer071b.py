sacar = int(input('Que valor você quer sacar? R$'))
total = sacar   # montante, inicialmente recebe o valor que entrou pelo teclado
ced = 50    # cedula atual
totalCedulas = 0
while True:
    if total >= ced:
        total -= ced    # tirando cinquenta do valor total
        totalCedulas += 1
    else:
        if totalCedulas > 0:
           print(f'Total de {totalCedulas} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            totalCedulas = 0
        if total == 0:
            break
