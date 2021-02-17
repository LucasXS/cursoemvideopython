#ler dois numeros inteiros e compralos, mostrando na tela uma mensagem:
#-O primeiro valor é maior
#-O Segundo valor pe maior
#-Não existe valor maior, os dois são iguais

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))

if num1 > num2:
    print(f'O Número \033[1:31m{num1}\033[m é maior que \033[1:33m{num2}')
elif num2 > num1:
    print(f'O Número \033[1:33m{num2}\033[m é maior que \033[1:31m{num1}')
else:
    print('Não existe valor maior, os dois são iguais')