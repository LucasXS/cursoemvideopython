somaCompra = cont = contadorMenorPreco = 0
menorPreco = 0
nomeMenorProduto = ' '
while True:
    nomeProduto = str(input('Nome do Produto: '))
    precoProduto = float(input('Preço: R$'))
    somaCompra += precoProduto
    contadorMenorPreco += 1
    if precoProduto >= 1000:
        cont += 1

    if contadorMenorPreco == 1 or precoProduto < menorPreco:
        menorPreco = precoProduto
        nomeMenorProduto = nomeProduto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? ')).upper().strip()[0]
    if continuar == 'N':    # condição de parada
        break
print(f'O Valor total da compra foi de R{somaCompra:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMenorProduto} que custou R${menorPreco:.2f}')