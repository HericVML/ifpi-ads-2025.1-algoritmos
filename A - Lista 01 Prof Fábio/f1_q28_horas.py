# Entrada
horas = int(input('Horas: '))

# Processamento
semanas = horas // 168
horas_sem = horas % 168

dias = horas_sem // 24
horas_dia = horas_sem % 24

# Saída
resultado = f'{horas}h equivalem a {semanas} semana(s), {dias} dia(s) e {horas_dia} hora(s).'
print(resultado)
