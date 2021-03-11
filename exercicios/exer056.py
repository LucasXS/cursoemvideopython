soma = 0
bigger = 0
cont = 0
mediaIdade = 0
for c in range(1, 5):
    print(f'=={c}ª Pessoa==')
    name = str(input('Type your name: ')).strip().upper()
    age = int(input('Type your age: '))
    sex = str(input('Type your sex [F/M]: ')).upper().strip()
    soma += age
    mediaIdade = soma / 4
    if c == 1 and sex == 'M':
        bigger = age
        mName = name
    if sex in 'M' and age > bigger:
        bigger = age
        mName = name
    if sex == 'F' and age < 20:
        cont += 1

print(f'A Média de idade do grupo é de {mediaIdade} anos!')
print(f'{mName} é o homem mais velho e tem {bigger} anos!')
print(f'{cont} mulher(es) tem menos de 21 anos')
