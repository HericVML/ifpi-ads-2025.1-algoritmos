# Entrada
dias = int(input('Dias: '))

# Processamento
semanas = dias // 7
days = dias % 7

# Saída
resultado = f'{dias} dias equivalem a {semanas} semana(s) e {days} dia(s).'
print(resultado)