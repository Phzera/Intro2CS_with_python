""" Dado uma quantidade de segundos,
    esse programa converte a quantidade para horas,
    minutos e segundos
"""

segundos_str = input("por favor, entre com o número de segundos:\n")
total_seg    = int(segundos_str)

horas = total_seg // 3600
seg_restante = total_seg % 3600
minutos = seg_restante // 60
seg_restante_final = seg_restante % 60

print(horas, "horas, ", minutos, "minutos e", seg_restante_final, "segundos.")
