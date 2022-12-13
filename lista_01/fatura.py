""" Exercício opcional 1: recebe
(entrada de dados através do teclado) o nome do cliente,
o dia de vencimento, o mês de vencimento e o valor da
fatura  e imprima (saída de dados) a mensagem com os dados recebidos"""

nome = input("Digite o nome do cliente:")
dia_vencimento = input("Digite o dia de vencimento:")
mes_vencimento = input("Digite o mês de vencimento:")
valor_fatura = input ("Digite o valor da fatura:")

print("Olá,", nome)
print("A sua fatura com vencimento em", dia_vencimento, "de", mes_vencimento, "no valor de R$",
     valor_fatura, "está fechada.")
