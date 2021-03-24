print('='*25)
print('   10 TERMOS DE UMA PA  ')
print('='*25)
primTermo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
termo = primTermo   # mostra o termo
cont = 1    # contador de termos
while cont <= 10:
    print('{}→ '.format(termo), end='')     # Alt 26
    termo += razao
    cont += 1
print('FIM')

