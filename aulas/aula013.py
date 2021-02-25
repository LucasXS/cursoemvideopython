for c in range(0, 6): #(1, 6) ele print 5, o último não é considerado.
    print(c)
print('FIM')

for c in range(6, 0, -1): #Esse '-1' é a iteração, ela faz com que a sequencia seja descrescente
    print(c)
print('Fim')

for c in  range(0, 7, 2): #Esse '2' é a iteração, faz com que o prog. pule de 2 em 2 até o 7
    print(c)
print('FIM')

i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 3):
    n = int(input('Digite um número: '))
print('Fim')

s = 0
for c in  range(0, 4):
    n = int(input('Número: '))
    s += n #s = s + n
print('O somatorio de todos os valores foi {}'.format(s))
