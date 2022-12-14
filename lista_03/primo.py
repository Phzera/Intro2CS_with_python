"""
Escreva adicional 1
escrevea um programa que receba um número
inteiro positivo na entrada e verifique
se é primo. Se o número for primo, imprima
"primo". Caso contrário, imprima "não primo".
"""
import sys

entrada = int(input('Digite um numero inteiro positivo: '))

if entrada <= 1 :
    sys.exit("Erro! O número deve ser positivo maior que 1")

fator = 2
resto = 0

if entrada == 2:
    sys.exit('primo')

while fator < entrada:
    resto = entrada % fator
    fator += fator
    if resto == 0:
        print("não primo")
    else:
        print("primo")
