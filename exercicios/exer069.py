idadeCont = sexoMas = mulherCont = 0
continuar = 'S'

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().split()
    continuar = str(input('Quer continuar? [S/N] ')).upper().split()

    if idade > 18:
        idadeCont += 1
    elif sexo == 'M':
        sexoMas += 1
    elif sexo == 'F' and idade > 20:
        mulherCont += 1
    elif continuar == 'N':
        print(f'Total de pessoas com mais de 18 anos: {idadeCont}')
        print(f'Ao todo temos {sexoMas} homens cadastrados')
        print(f'E temos {mulherCont} mulheres com menos de 20 anos')
        break
print(f'2Total de pessoas com mais de 18 anos: {idadeCont}')
print(f'2Ao todo temos {sexoMas} homens cadastrados')
print(f'2E temos {mulherCont} mulheres com menos de 20 anos')
