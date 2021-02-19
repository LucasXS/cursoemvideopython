num = int(input('Digite um Número Inteiro: '))
print('='*30)
print('     OPÇÕES DE CONVERSÃO     ')
print('='*30)
print('1 - para BINÁRIO')
print('2 - para OCTAL')
print('3 - para HEXADECIMAL')
print('='*30)
baseConversao = int(input('Digite o valor escolhido de conversão da tabela: '))

if baseConversao == 1:
    binario = bin(num)
    print(f'A representação de {num} em BINÁRIO é {binario[2:]}') #desconsiderar o '0b'
elif baseConversao == 2:
    octal = oct(num)
    print(f'A representação de {num} em OCTAL é {octal[2:]}') #desconsiderar o '0o'
elif baseConversao == 3:
    hexadecimal = hex(num)
    print(f'A representação de {num} em HEXADECIMAL é {hexadecimal[2:]}') #desconsiderar o '0x'
else:
    print('Digite um valor valido da tabela!')