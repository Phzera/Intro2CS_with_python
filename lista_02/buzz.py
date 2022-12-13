""" Exercícios 3 - FizzBuzz parcial, parte 2
Receba um número inteiro na entrada e imprima Buzz
se o número for divisível por 5. Caso contrário,
imprima o mesmo número que foi dado na entrada. """

is_buzz = int(input("Entre com um inteiro: "))

if is_buzz % 5 == 0:
    print("Buzz")
else:
    print(is_buzz)
