# Entrada
A = int(input('Número 1 (A): '))
B = int(input('Número 2 (B): '))
C = int(input('Número 3 (C): '))

# Processamento
R = (A + B) ** 2
S = (B + C) ** 2

D = (R + S) / 2

# Saída
print(f'D = (R + S) / 2')
print(f'1. R = (A + B) ** 2')
print(f'2. S = (B + C) ** 2')
print(f'D = {D}')