"""
Exercício 1
Escreva um programa que receba um número natural n
na  entrada e imprima  n! (fatorial) na saída
"""

entrada = int(input('Digite o valor de n: '))

i = 1
SAIDA = 1

while i <= entrada:
    SAIDA = SAIDA * i
    i += 1
print(SAIDA)
