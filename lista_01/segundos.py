""" 
Exercício opcional 2:  dada a quantidade de 
segundos, "quebre" esse valor em dias, horas,
minutos e segundos. A saída deve estar no formato:
a dias, b horas, c minutos e d segundos
"""

segundos_str = input("por favor, entre com o número de segundos que deseja converter:")
total_seg    = int(segundos_str)

# segundos por dia
dias               = int(total_seg  // (3600 * 24))
horas_restante     = int(total_seg % (3600 * 24))
# segundos por hora
horas              = int(horas_restante // 3600)
seg_restante       = int(horas_restante % 3600)
#segundos por minuto
minutos            = int(seg_restante // 60)
seg_restante_final = int(seg_restante % 60)

print(dias, "dias,", horas, "horas,", minutos, "minutos e", seg_restante_final, "segundos.")
