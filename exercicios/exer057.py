# ler o sexo de uma pessoa [M/F]. Caso entre com outro valor informar para digitar o valor correto

sexo = 'M'
while sexo == 'F' or sexo == 'M':
    sexo = str(input('Informe seu sexo: [F/M} ')).upper()
    if sexo == 'F':
        print('Sexo Feminino')
    elif sexo == 'M':
        print('Sexo Masculino')
    else:
        print('Digite um valor valido!')
