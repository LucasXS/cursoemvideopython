from datetime import date
anaAtual = date.today().year

nome = str(input('Digite seu nome: ')).upper()
anoNascimento = int(input('Ano de nascimento: '))
idadeAtual = anaAtual - anoNascimento

if idadeAtual <= 9:
    print(f'NOME: {nome} - IDADE: {idadeAtual} - CATEGORIA: MIRIM')
elif idadeAtual <= 14:
    print(f'NOME: {nome} - IDADE: {idadeAtual} - CATEGORIA: INFANTIL')
elif idadeAtual <=19:
    print(f'NOME: {nome} - IDADE: {idadeAtual} - CATEGORIA: JUNIOR')
elif idadeAtual <=20:
    print(f'NOME: {nome} - IDADE: {idadeAtual} - CATEGORIA: SÊNIOR')
else:
    print(f'NOME: {nome} - IDADE: {idadeAtual} - CATEGORIA: MASTER')