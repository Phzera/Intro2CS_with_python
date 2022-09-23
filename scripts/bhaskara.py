"""" Calcua as raízes de uma equação de 2° grau """
import math

print("Entre com os coeficientes da equação: ax² + bx + c = 0 \n")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c
raiz1 = (-b  + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)

if delta == 0:
    print("A única raiz é: ", raiz1)
else:
    if (delta < 0):
        print("Esta equação não possuí raízes reais")
    else:
        print("A primeira raiz é: ", raiz1)
        print("A segunda raiz é: ", raiz2)