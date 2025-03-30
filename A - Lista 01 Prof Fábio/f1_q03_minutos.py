# Entrada
minutos = int(input('Minutos: '))

# Processamento
horas = minutos // 60
minutos_rest = minutos % 60

# Saída
print(f'> {minutos}min equivalem a {horas}h{minutos_rest}min')