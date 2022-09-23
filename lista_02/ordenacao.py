""" Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima
crescente se eles forem dados em ordem crescente.
Caso contrário, imprima 'não está em ordem crescente' """

num1 = int(input("Entre com o primeiro número inteiro: "))
num2 = int(input("Entre com o primeiro número inteiro: "))
num3 = int(input("Entre com o primeiro número inteiro: "))

if (num1 < num2) & (num2 < num3):
    print("crescente")
else:
    print("não está em ordem crescente")
