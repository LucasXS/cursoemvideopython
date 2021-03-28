# Programa que jogue PAR ou IMPAR com o computador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
from random import randint
print('-=' * 30)
print('VAMOS JOGAR PARA OU IMPAR')
print('-=' * 30)
soma = cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    sinal = str(input('Pagar ou Impar? [P/I] ')).upper().strip()[0]
    computador = randint(1, 10)
    soma = jogador + computador
    if soma % 2 == 0 and sinal == 'P':
        cont += 1
        print(f'\033]1;31mVOCÊ GANHOU!\033[m Sequencia de vitorias {cont}')
    elif soma % 2 == 1 and sinal == 'I':
        cont += 1
        print(f'\033[1;31mVOCÊ GANHOU!\033[m Sequencia de vitorias {cont}')
    else:
        print(f'\033[1;33mVOCÊ PERDEU!\033[m Sua sequencia de vitoria era de {cont}'
              f'Computador escolheu {computador}')
        break
print('FIM')
