primTermo = int(input('PRIMEIRO TERMO DA PA: '))
razao = int(input('RAZÃO DA PA: '))
# mostra o termo
termo = primTermo
# contador de termos
cont = 1
total = 0
outrosTermos = 11   # Quantidade inicial de termos, o total irá receber esse valor.
while outrosTermos != 0:
    total = total + outrosTermos
    while cont < total:
        print('{}→ '.format(termo), end='')     # Alt 26
        termo += razao
        cont += 1
    print('PAUSA!')
    outrosTermos = int(input('Outros termos: '))
print('FIM')