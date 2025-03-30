# Entrada
numero = int(input('Número: '))

# Processamento
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = ((numero % 1000) % 100) // 10
unidade = ((numero % 1000) % 100) % 10

soma = milhar + centena + dezena + unidade

# Saída
print(f"A soma dos 4 algarismos resulta em {soma}.")