# Entrada
minutos = int(input('Minutos: '))

# Processamento
dias = minutos // 1440
minutos_dias = minutos % 1440

horas = minutos_dias // 60
minutos_restantes = minutos_dias % 60

# Saída
resultado = f'{minutos}min equivalem a {dias} dia(s), {horas}h e {minutos_restantes}min.'
print(resultado)