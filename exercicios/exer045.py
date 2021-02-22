#crie um programa que faça o computador jogar JOKENPÔ com você!
import random
from  time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('=-'*10)
print('     SUAS OPÇÕES     ')
print('=-'*10)
print('[1] - PEDRA')
print('[2] - PAPEL')
print('[3] - TESOURA')
print('=-'*10)
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KE')
sleep(0.5)
print('PO!!!')
sleep(0.5)
if jogador == 0:
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    if itens[computador] == itens[jogador]:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
elif jogador == 1:
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    if itens[computador] == itens[jogador]:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
elif jogador == 2:
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    if itens[computador] == itens[jogador]:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
else:
    print('OPÇÃO INVALIDA!')