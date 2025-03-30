# Entrada
numero = int(input('Número: '))

# Processamento
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10 

inverso = (unidade * 100) + (dezena * 10) + centena

# Saída
print(f'Inverso do número: {inverso}')