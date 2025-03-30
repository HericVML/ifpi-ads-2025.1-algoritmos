# Entrada
metro = int(input('Metros: '))

# Processamento
km = metro // 1000
m = metro - (km*1000)

# Saída
resultado = f'{metro}m equivalem a {km}km e {m}m'
print(resultado)