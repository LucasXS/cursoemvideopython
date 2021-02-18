#ler o ano de nascimento de um jovem e informar de acordo com sua idade:
#se ele ainda vai se alistar ao serviço militar. #se é a hora de se alistar #se já passou do tempo do alistamento
#o programa também deve mostrar o quanto que faltou ou passou do prazo
from datetime import date

nome = str(input('Qual o seu nome: '))
anoNascimento = int(input('Qual o ano de seu nascimento: '))

anoAtual = date.today().year
idadeAtual = (anoAtual - anoNascimento)
tempoParaAlist =

if idadeAtual <= 17:
    print(f'Você não precisa se alistar ainda!Falta {} para o alistamento')
elif idadeAtual == 18:
    print('Você precisa se alistar')
else:
    print('Você passou da epoca de se alistar')




