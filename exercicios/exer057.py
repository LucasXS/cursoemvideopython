# vai tirar os espaços, caixa alto e vai pegar só a primeira letra
sexo = str(input('Informe seu sexo: [F/M} ')).strip().upper()[0]
while sexo not  in 'MnFf':      # enquanto sexto não estiver em masc-fem.
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')