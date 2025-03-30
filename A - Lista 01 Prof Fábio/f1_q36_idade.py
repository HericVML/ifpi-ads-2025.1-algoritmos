# Entrada
anos = int(input('Anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))

# Processamento
anos_dias = anos * 365
meses_dias = meses * 30

soma = anos_dias + meses_dias + dias

# Saída
resultado = f'Sua idade é de {soma} dias.'
print(resultado)