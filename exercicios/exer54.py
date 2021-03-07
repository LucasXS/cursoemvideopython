#ler o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantos já são maiores

from datetime import date
anoAtual = date.today().year

for c in range(1, 8):
    anoNascimento = int(input(f'{c} Digite o ano de seu nascimento: '))
    idade = (anoAtual - anoNascimento)
    print(f'Quem nasceu em {anoNascimento}, tem {idade} anos em {anoAtual}')
    if idade < 18:
        print('Você não atingiu a maioridade!')
    else:
        print('Você já pode ser preso!')
