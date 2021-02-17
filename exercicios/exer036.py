valorCasa = float(input('Qual o valor da casa? '))
salarioComprador = float(input('Qual o valor de seu salário mensal? '))
mesesPagar = int(input('Em quantos meses você vai pagar? '))

valorPrestacao = valorCasa / mesesPagar
salarioLiberado = (salarioComprador * 0.30)

if valorPrestacao <= salarioLiberado:
    print(f'\033[1:31mPARABÉNS!\033[mEmprestimo Aprovado!! O valor de R${salarioLiberado}'
          f' é suficiente para aproação do emprestimo')
else:
    print(f'\033[1:33m\033[1:31mREPROVADO!\033[m Infelizmente o valor de R${salarioLiberado}'
      f' não é suficiente para a liberação do emprestimo.')
