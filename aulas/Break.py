num = cont = somar = 0
while True:
    num = int(input('Número: '))
    if num == 999:
        break   # o break para o loop
    somar += num
    cont += 1
print(f'{cont} - {somar}' )
