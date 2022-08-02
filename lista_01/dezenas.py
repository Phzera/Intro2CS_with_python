""" Exercício opcional 3:  recebe um número inteiro e imprime
    o dígito das dezenas"""

numero = int(input("Digite um número inteiro:"))
# realiza uma divisão inteira por 10
div_10 = numero // 10
# obtém resto da divisão inteira novamente por 10 
reminder = div_10 % 10

print("O dígito das dezenas é", reminder)
