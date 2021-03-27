# mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.
num = 1
cont = 1
print('='* 40)
num = int(input('Você quer ver a tabuada de que valor? '))
print('='* 40)
while True:
    while cont < 11:
        if num > 0:
            print(f'{num} x {cont} = {num*cont}')
            cont += 1
            if cont == 11:
                cont = 1
                print('-' * 40)
                num = int(input('Você quer ver a tabuada de que valor? '))
                print('-' * 40)
        if num < 0:
            break
print('PROGRAMA ENCERRADO!')


