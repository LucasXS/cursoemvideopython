operador = 0
num1 = float(input('Valor A: '))
num2 = float(input('Valor B: '))
while operador != 5:
    print('=-'*30)
    print(' [1] - Somar\n [2] - Multiplicar\n [3] - Maior\n [4] - Novos números\n [5] - Sair do progrma')
    print('=-' * 30)
    operador = int(input('Qual é a sua opção? '))
    if operador == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é {soma}')
    elif operador == 2:
        multiplicacao = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é {multiplicacao}')
    elif operador == 3:
        if num1 > num2:
            print(f'O número {num1} é maior que o número {num2}')
        elif num2 > num1:
            print(f'O número {num2} é maior que o número {num1}')
        else:
            print(f'Os números são iguais!')
    elif operador == 4:
        # informe o número novamente
        num1 = float(input('Valor A: '))
        num2 = float(input('Valor B: '))
    elif operador == 5:
        print('FIM DO PROGRAMA...')
    else:
        print('Opção invalida!')
print('ATÉ A PRÓXIMA!!')