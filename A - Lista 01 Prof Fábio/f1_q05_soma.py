# Entrada
numero = int(input('Número (3 dígitos): '))

# Processamento
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10
soma = centena + dezena + unidade

# Saída
print(f'A soma dos algarismos é: {soma}')