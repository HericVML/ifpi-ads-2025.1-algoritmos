# Entrada
temperatura_f = int(input('Temperatura (F): '))

# Processamento
temperatura_c = (5 * temperatura_f - 160) / 9

# Saída
resultado = f'Temperatura: {temperatura_f}F equivalem a {temperatura_c}C'
print(resultado)