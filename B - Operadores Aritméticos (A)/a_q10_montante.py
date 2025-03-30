# Entrada
capital = float(input('Capital: '))
taxa = float(input('Taxa de juros: '))
tempo = int(input('Tempo em meses: '))

# Processamento
montante = capital * (1 + taxa * tempo)

# Saída
print(f'Montante final = R${montante:.1f}')