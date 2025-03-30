# Entrada
peso = float(input('Peso em kg: '))
altura = float(input('Altura em metros: '))

# Processamento
imc = peso / (altura**2)

# Saída
print(f'IMC = {imc:.2f}')