from datetime import date
anoAtual = date.today().year

sexo = str(input('Sexo - F/M: '))

if sexo == 'M':
    nome = str(input('Seu nome: '))
    anoNascimento = int(input('Ano de nascimento: '))
    idade = (anoAtual - anoNascimento)
    print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}')

    if idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos para o alistamento')
        ano = anoAtual + saldo
        print(f'Seu alistamento será em {ano}')
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!r')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você já devia ter se alistado há {saldo} anos')
        ano = anoAtual - saldo
        print(f'Seu alistamento foi em {ano}')
else:
    print('Você não tem obrigações militares!')


