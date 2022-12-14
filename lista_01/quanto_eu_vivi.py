""" Quantos segundos eu já vivi?"""

idade_anos  = int(input("Entre com sua idade em anos:"))
idade_meses = int(input("Entre com o restante de sua idade em meses:"))
idade_dias  = int(input("Entre com o restante de sua idade em dias:"))

# Não é esperado que seja utilizado funções nesta seção, mas fiz de teimoso XD
def dias2segundos(dias):
    """Converte dias para segundos"""
    segundos = (60 * 60 * 24 * dias)
    return segundos

def meses2segundos(meses):
    """Converte meses para segundos"""
    segundos = (60 * 60 * 24 * 30 * meses)
    return segundos

def anos2segundos(anos):
    """Converte anos para segundos"""
    segundos = (60 * 60 * 24 * 30 * 12 * anos)
    return segundos

print("Você já viveu aproximadamente ", dias2segundos(idade_dias) + meses2segundos(idade_meses)
                                     + anos2segundos(idade_anos), "segundos.")
