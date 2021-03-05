# ler uma frase qualquer e dizer se ela é um palindromo, desconsiderando os espaços
# ex: APOS A SOPA - A SACADA DA CASA #A TORRE DA DERROTA #O LOBO AMA O BOLO #ANOTARAM A DATA DA MARATONA

frase = str(input('FRASE: ')).lower().strip().split()
print(len(frase))
print(frase)
print(frase[::-1])

