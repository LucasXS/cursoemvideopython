#motra na tela uma contagem regressiva para o estouro de fogos de artificio. Indo de 10 até 0. Com uma pause
#de 1 segundo entre eles.

from time import sleep

for c in range(10, 0, -1):
    print('\033[1;031m', c)
    sleep(1)
print('\033[1:33mFELIZ ANO NOVOOOOOOO!')