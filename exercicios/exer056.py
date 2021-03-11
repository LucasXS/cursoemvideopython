soma = 0
bigger = 0
cont = 0
mediaIdade = 0
for c in range(1, 5):
    print(f'=={c}ª Pessoa==')
    name = str(input('Type your name: ')).strip()
    age = int(input('Type your age: '))
    sex = str(input('Type your sex [F/M]: ')).upper().strip()
    soma += age
    mediaIdade = soma / 4

    if sex == 'M':
        if c == 1:
            bigger = age
            mName = name
        else:
            if age > bigger:
                bigger = age
                mName = name
    if sex == 'F':
        if age < 21:
            cont += 1

print(f'A Média de idade do grupo é de {mediaIdade} anos!')
print(f'{mName} é o homem mais velho!')
print(f'{cont} mulher(es) tem menos de 21 anos')
