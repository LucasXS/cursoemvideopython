import random
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('=-'*10)
print('     SUAS OPÇÕES     ')
print('=-'*10)
print('[0] - PEDRA')
print('[1] - PAPEL')
print('[2] - TESOURA')

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
    if itens[computador] == 'Pedra':
        print('Empate')
    elif itens[computador] == 'Papel':
        print('Você Perdeu!')
    elif itens[computador] == 'Tesoura':
        print('Você Ganhou!')

elif jogador == 1:
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    if itens[computador] == 'Pedra':
        print('Você Ganhou!')
    elif itens[computador] == 'Papel':
        print('Empate!')
    elif itens[computador] == 'Tesoura':
        print('Você Perdeu!')

elif jogador == 2:
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    if itens[computador] == 'Pedra':
        print('Você perdeu!!')
    elif itens[computador] == 'Papel':
        print('Você Ganhou!')
    elif itens[computador] == 'Tesoura':
        print('Empate!')
else:
    print('OPÇÃO INVALIDA!')
