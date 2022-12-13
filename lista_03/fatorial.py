"""
Exercício 1
Escreva um programa que receba um número natural n
na  entrada e imprima  n! (fatorial) na saída
"""

input = int(input('Digite o valor de n: '))

i = 1
output = 1

while i <= input:
    output = output * i
    i += 1

print(output)