# Entrada
minutos = int(input('Minutos: '))

# Processamento
horas = minutos // 60
minutos_rest = minutos % 60

# Saída
print(f'{horas} horas(s) e {minutos_rest} minuto(s).')