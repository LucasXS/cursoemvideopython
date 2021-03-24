# 63 - ler um número N inteiro e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#   É uma sucessão de números que, misteriosamente, aparece em muitos fenômenos da natureza.
#   Descrita no final do século 12 pelo italiano Leonardo Fibonacci, ela é infinita e começa
#   com 0 e 1. Os números seguintes são sempre a soma dos dois números anteriores.
#   0-1-1-2-3-5-8-13...n
num = int(input('Quantos termos você quer mostrar?  '))
cont = 0
fibonacci = 0
anterior = 0
atual = 0
while cont != num:     # condição de parada
    if cont == 1:
        fibonacci = 1
        anterior = 0
        atual = fibonacci
    else:
        fibonacci = anterior + atual
        anterior = atual
        atual = fibonacci
    print('{} → '.format(fibonacci), end='')
    cont += 1
print('Fim')