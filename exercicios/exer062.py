print('='*25)
print('   10 TERMOS DE UMA PA  ')
print('='*25)
primTermo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
termo = primTermo   # mostra o termo
cont = 1    # contador de termos
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}→ '.format(termo), end='')     # Alt 26
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos')
