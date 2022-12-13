"""
Exercício 3
Escreva um programa que receba um número
inteiro na entrada, calcule e imprima a
soma dos dígitos deste número na saída
"""
import sys

entrada = int(input('Digite um numero inteiro positivo: '))

SOMA = 0

if entrada < 0 :
    sys.exit("Erro! O número deve ser positivo")

while entrada > 0:
    SOMA = SOMA + entrada % 10
    entrada = entrada // 10
print(SOMA)
