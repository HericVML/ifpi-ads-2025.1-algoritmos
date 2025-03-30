# Entrada
valor_inicial = float(input('Valor inicial: '))
desconto = int(input('Percentual de desconto: '))

# Processamento
valor_final = valor_inicial - ((valor_inicial/100) * 10)

# Saída
print(f'Valor final: R${valor_final:.1f}')