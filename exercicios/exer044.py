produto = str(input('Nome do produto: ')).upper().strip()
preco = float(input('Valor do produto: '))

print('='*30)
print('     OPÇÕES DE PAGAMENTO     ')
print('='*30)
print('1 - Á VISTA DINHEIRO/CHEQUE - 10% DESCONTO')
print('2 - Á VISTA NO CARTÃO - 5% DESCONTO')
print('3 - EM 2X NO CARTÃO - PREÇO NORMAL')
print('4 - EM 3X OU MAIS NO CARTÃO - 20% DE JUROS')
print('='*30)

meioPagamento = int(input('Meio de pagamento: '))

if meioPagamento == 1:
    novoPreco = preco - (preco * 0.10)
    print(f'O Valor da {produto} saiu de R${preco} para R${novoPreco:.2F}!')
elif meioPagamento == 2:
    novoPreco = preco - (preco * 0.05)
    print(f'O Valor da {produto} saiu de R${preco} para R${novoPreco:.2F}!')
elif meioPagamento == 3:
    print(f'O Valor da {produto} custa R${preco}, não há Desconto para pagamento no cartão de credito!')
elif meioPagamento == 4:
    novoPreco = preco + (preco * 0.20)
    print(f'O Valor da {produto} saiu de R${preco} para R${novoPreco:.2F}!')
else:
    print('Digite um valor valido!')
print('OBRIGADO POR COMPRAR CONOSCO - VOLTE SEMPRE!!')