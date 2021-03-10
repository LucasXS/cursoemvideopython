# ler nome, idade e sexo de 4 pessoas. No final mostre: A media de idade do grupo. Qual o nome do homem mais velho.
# Qyantas mulheres tem menos de 21 anos

soma = 0
for c in range(1, 5):
    print(f'=={c}ª Pessoa==')
    name = str(input('Type your name: ')).strip()
    age = int(input('Type your age: '))
    sex = str(input('Type your sex [F/M]: ')).upper().strip()
    soma += age
if sex == 'M':

mediaIdade = soma /4
print('A Média de idade do grupo é de {} anos'.format(mediaIdade))


