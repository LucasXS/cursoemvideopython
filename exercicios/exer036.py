valorCasa = float(input('Valor da casa? R$'))
salarioComprador = float(input('Valor de seu salário mensal? R$'))
anosPagar = int(input('Quantos anos de financiamento? '))

valorPrestacao = valorCasa / (anosPagar * 12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorCasa, anosPagar), end='')
print(' a prestação será de R${:.2f}'.format(valorPrestacao))

minimo = (salarioComprador * 0.30)

if valorPrestacao <= minimo:
    print(f'\033[1:31mPARABÉNS!\033[mEmprestimo Aprovado!! O valor de R${minimo}'
          f' é suficiente para aproação do emprestimo')
else:
    print(f'\033[1:33m\033[1:31mREPROVADO!\033[m Infelizmente o valor de R${minimo}'
      f' não é suficiente para a liberação do emprestimo.')
