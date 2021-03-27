num = cont = total = 0
num = int(input('Digite um número: '))
while num != 999:
    cont += 1
    total += num
    num = int(input('Digite um número: '))
print(f'Você'
      f' digitou {cont} números e a soma entre eles foi {total} ')