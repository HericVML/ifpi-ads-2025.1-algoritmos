# Entrada
idade = int(input('Dias: '))

# Processamento
anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30

# Saída
resultado = f'Sua idade é de {anos} ano(s), {meses} mês(es) e {dias} dia(s).'
print(resultado)