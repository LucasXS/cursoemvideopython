idadeCont = sexoMas = mulherCont = 0
while True:     # condição de parada
    idade = int(input('Idade: '))
    sexo = ' '
    sexo = str(input('Sexo: [M/F] ')).upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        idadeCont += 1
    if sexo == 'M':
        sexoMas += 1
    if sexo == 'F' and idade < 20:
        mulherCont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {idadeCont}')
print(f'Ao todo temos {sexoMas} homens cadastrados')
print(f'E temos {mulherCont} mulheres com menis de 20 anos')