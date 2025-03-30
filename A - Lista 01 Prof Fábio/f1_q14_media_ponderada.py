# Entrada
nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
nota3 = float(input('Nota 3:'))
peso1 = int(input('Peso da nota 1:'))
peso2 = int(input('Peso da nota 2:'))
peso3 = int(input('Peso da nota 3:'))

# Processamento
media_ponderada = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)

# Saída
print(f'Média ponderada das notas: {media_ponderada:.2f}') 