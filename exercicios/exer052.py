tot = 0
num = int(input('Número: '))    # digitar um número inteiro - é ou não um número primo
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!!')
else:
    print('E por isso ele NÃO É PRIMO!')