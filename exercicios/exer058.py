# melhor o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
# só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessarios para vencer.

from random import randint
from time import sleep

computador = randint(0, 10)     # o computador vai pensar em número entre 0 e 10
palpites = 0
acertou = False

print('START THE GAME! - VAMOS TESTAR SUA SORTE')
print('='*60)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('='*60)

while not acertou:    # condição de parada
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    sleep(0.1)
    if jogador == computador:
        sleep(0.1)
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')
print(f'\033[1:33mPARABÉNS, você ganhou!\033[m Precisou de '
      f'\033[1:31m{palpites}\033[m tentativas para acertar o que eu pensei!')


