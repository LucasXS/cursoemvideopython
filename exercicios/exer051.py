print('='*25)
print('   10 TERMOS DE UMA PA  ')
print('='*25)
primTermo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
decimo = primTermo + 10 * razao
for c in range(primTermo, decimo, razao):
    print('{}'.format(c), end=' ->')
print('FIM')