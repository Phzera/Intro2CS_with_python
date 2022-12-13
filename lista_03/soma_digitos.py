"""
Exercício 3
Escreva um programa que receba um número
inteiro na entrada, calcule e imprima a 
soma dos dígitos deste número na saída
"""

entrada = int(input('Digite um numero inteiro positivo: '))

soma = 0

if entrada < 0 :
    exit("Erro! O número deve ser positivo")

while entrada > 0:
    soma = soma + entrada % 10
    entrada = entrada // 10
print(soma)

