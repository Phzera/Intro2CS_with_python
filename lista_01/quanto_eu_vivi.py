""" Quantos segundos eu já vivi?"""

idade_anos  = int(input("Entre com sua idade em anos:"))
idade_meses = int(input("Entre com o restante de sua idade em meses:"))
idade_dias  = int(input("Entre com o restante de sua idade em dias:"))


def dias2segundos(dias):
    segundos = (60 * 60 * 24 * dias)
    return (segundos)

def meses2segundos(meses):
    segundos = (60 * 60 * 24 * 30 * meses)
    return (segundos)

def anos2segundos(anos):
    segundos = (60 * 60 * 24 * 30 * 12 * anos)
    return (segundos)


print("Você já viveu aproximadamente ", dias2segundos(idade_dias) + meses2segundos(idade_meses)
                                     + anos2segundos(idade_anos), "segundos.")