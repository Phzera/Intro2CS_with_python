"""
Exercício 2
Receba um número inteiro positivo na entrada
e imprima os n primeiros números ímpares naturais.
"""
import sys

entrada = int(input('Digite um numero inteiro positivo: '))

if entrada < 0 :
    sys.exit("Erro! O número deve ser positivo")

i = 0
IMPAR = 1

while i < entrada:
    print(IMPAR)
    IMPAR += 2
    i += 1
