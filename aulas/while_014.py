#
#               ESTRUTURA WHILE
#
# Podemos usar quando já sabemos o valor final assim como no FOR
# Usamos principalmente quando NÃO sabemos o valor final.

# Exemplo1 - quando não sabemos o valor final
'''n = 1
while n != 0: #condição de parada
    n = int(input('Digite um valor: '))
print('FIM')'''

# Exemplo2
'''n = 1
r = 'S' # começa com Sim para iniciar o programa
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')'''

# Exemplo3
n = 1
par = impar = 0
while n != 0:   # condição de parada
    n = int(input('Digite um valor: '))
    if n != 0:  # desconsidera o zero na contagem, sem isso ele entraria nos PARES
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares')