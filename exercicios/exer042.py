a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

#conferindo se é um triângulo
if (a < b + c) and (b < a + c) and (c < b + a):
    print('Os segmentos acima PODEM formar um triângulo!')
        #condicionais para definir que tipo de triângulo é
    if a == b == c:
       print('É um Triângulo Equilatero - Três lados iguais')
    elif a != b != c != a:
        print('É um Triângulo Escaleno - Três lados diferentes')
    else:
        print('É um Triânulo Isósceles - Dois lados quaisquer iguais')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')