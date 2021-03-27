# ler vários números inteiros. O programa só vai parar quando digitar 999 (condição de parada)
# No final mostre quantos números foram digitados e qual foi a soma eles eles. Desconsiderar o 999.

num = cont = somar = 0
while True:
    num = int(input('Número: '))
    if num == 999:
        break   # o break para o loop
    somar += num
    cont += 1
print(f"Form digitados {cont} números\n"
      f"A Soma total deu: {somar}")
