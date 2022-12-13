"""
Exercício 2
Receba um número inteiro positivo na entrada
e imprima os n primeiros números ímpares naturais.
"""

entrada = int(input('Digite um numero inteiro positivo: '))

if entrada < 0 :
    exit("Erro! O número deve ser positivo")

i = 0
impar = 1

while i < entrada:
    print(impar)
    impar += 2
    i += 1



