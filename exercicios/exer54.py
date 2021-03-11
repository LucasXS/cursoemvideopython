from datetime import date
currentYear = date.today().year     # variável geral para receber o ano atula

cont = 0
cont2 = 0
for c in range(1, 8):
    YearOfBirth = int(input(f'{c} Type the year of birth: '))
    age = (currentYear - YearOfBirth)
    #print(f'Who was born in {YearOfBirth}, is {age} years old in {currentYear}')
    if age < 21:
        cont += 1
    else:
        cont2 += 1
print(f'Altogether we had {cont2} older people!')
print(f'Altogether ww had {cont} underage people!')
