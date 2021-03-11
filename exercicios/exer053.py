# ler uma frase qualquer e dizer se ela é um palindromo, desconsiderando os espaços
# ex: APOS A SOPA - A SACADA DA CASA #A TORRE DA DERROTA #O LOBO AMA O BOLO #ANOTARAM A DATA DA MARATONA

letra = 0
frase = str(input('FRASE: ')).upper().strip()
palavra = frase.split()     # ['lucas', 'e', 'cara']
junto = frase.replace(' ', '') # Remover os espaços internos -> junto = ''.join(palavra)
inverso = ''    # print(junto[::-1]) #Invesrso

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'Frase \033[31m{junto}\033[m e seu inverso \033[33m{inverso}\033[m é um Palindromo!')
else:
    print(f'Frase \033[31m{junto}\033[m e seu inverso \033[33m{inverso}\033[m NÃO é um Palindromo')