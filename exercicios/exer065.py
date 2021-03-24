resp = 's'.lower()
cont = media = soma = maiorNumero = 0
menorNumero = 999
while resp != 'n':
    num = int(input('Digite um número: '))
    resp = str(input('Deseja continuar? [S/N] '))
    soma += num
    cont += 1
    media = soma / cont
    if cont == 0:
        maiorNumero = num
        menorNumero = num
    else:
        if num > maiorNumero:
            maiorNumero = num
        if num < menorNumero:
            menorNumero = num
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior número foi {maiorNumero} e o menor número foi {menorNumero}')