# Entrada
segundos = int(input('Segundos: '))

# Processamento
horas = segundos // 3600
segundos_restantes = segundos % 3600

minutos = segundos_restantes // 60
segundos_finais = segundos_restantes % 60

# Saída
resultado = f'{segundos}seg equivalem a {horas}h, {minutos}min e {segundos_finais}seg.'
print(resultado)