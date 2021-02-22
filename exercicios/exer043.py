nome = str(input('Seu nome: '))
peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))

imc = peso / (altura**2)

if imc <18.5:
    print(f'\033[1;33m{nome}\033[m, seu IMC \033[1;31m{imc:.2f}\033[m e você está ABAIXO DO PESO!')
elif imc <25:
    print(f'\033[1;33m{nome}\033[m, seu IMC \033[1;31m{imc:.2f}\033[m e você está no PESO IDEAL')
elif imc <30:
    print(f'\033[1;33m{nome}\033[m, seu IMC \033[1;31m{imc:.2f}\033[m e você está no SOBREPESO!')
elif imc <40:
    print(f'\033[1;33m{nome}\033[m, seu IMC \033[1;31m{imc:.2f}\033[m e você está na OBESIDADE!')
else:
    print(f'\033[1;33m{nome}\033[m, seu IMC \033[1;31m{imc:.2f}\033[m e você está na OBESIDADE MORBIDA')