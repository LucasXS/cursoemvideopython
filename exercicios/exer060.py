# ler número qualquer e mostre o seu fatorial

num = int(input('Digite um número: '))
# o contador recebe o número que será o fatorial
contador = num
# uso o 1 pq qualquer número multiplicado por 1 dá ele mesmo.
fatorial = 1

print('Calculando {}! = '.format(num), end='')
# o contador vai somente até o 1
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}.'.format(fatorial))
