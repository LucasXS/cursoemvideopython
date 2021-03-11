# Calc. a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 #acumulador
cont = 0 #contador
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c        # acumulo valores (somando/multiplicando)
        cont += + 1  # um contador conta +1
print('A soma de todos os {} valores impares e multiplos de 3 é {}'.format(cont, soma))
