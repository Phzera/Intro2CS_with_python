""" Exercício 1 - Distância entre dois pontos
Receba 4 números na entrada, um de cada vez.
Os dois primeiros devem corresponder, respectivamente,
às coordenadas x e y de um ponto em um plano cartesiano.
Os dois últimos devem corresponder, respectivamente, às 
coordenadas x e y de um outro ponto no mesmo plano.
Calcule a distância entre os dois pontos. Se a distância
for maior ou igual a 10, imprima 'longe' na saída. 
Caso o contrário, quando a distância for menor que 10,
imprima 'perto' """

import math


num1 = float(input("Entre com o valor X do primeiro ponto: "))
num2 = float(input("Entre com o valor Y do primeiro ponto: "))
num3 = float(input("Entre com o valor X do segundo ponto: "))
num4 = float(input("Entre com o valor Y do segundo ponto: "))

distancia = math.sqrt((num1 - num3) ** 2 + (num2 - num4) ** 2)

if distancia >= 10:
    print("longe")
else:
    print("perto")