#refazer o exercicio 09 mostrando a tabuada de um número que o usuário escolher, só que agora utlizando um laço FOR.

num = int(input('Digite um valor da tabuada: '))
res = 0
for c in range(0, 11):
    res = num * c
    print('{} X {} = {}'.format(num, c, res))