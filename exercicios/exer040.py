nome = str(input('Informe seu nome: '))
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Media \033[1;31m{media}\033[m - \033[1;32m{nome}\033[m, Você está de REPROVADO!')
elif media >5 and media < 7:
    print(f'Media \033[1;31m{media}\033[m - \033[1;32m{nome}\033[m, Você está de RECUPERAÇÃO!')
else:
    print(f'Media \033[1;31m{media}\033[m - \033[1;32m{nome}\033[m, Você está de APROVADO!!')