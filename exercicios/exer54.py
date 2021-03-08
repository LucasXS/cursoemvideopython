#ler o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantos já são maiores

from datetime import date
currentYear = date.today().year #variável geral para receber o ano atula

cont = 0
cont2 = 0
for c in range(1, 8):
    YearOfBirth = int(input(f'{c} Type the year of birth: '))
    age = (currentYear - YearOfBirth)
    #print(f'Who was born in {YearOfBirth}, is {age} years old in {currentYear}')
    if age < 18:
        cont += 1
    else:
        cont2 += 1
print(f'Ao todo tivemos {cont2} pessoas maiores de idade!')
print(f'E também tivemos {cont} pessoas menores de idade')
