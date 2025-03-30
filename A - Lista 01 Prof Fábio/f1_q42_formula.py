# Entrada
x1,y1 = int(input('X1: ')), int(input('Y1: '))
x2,y2 = int(input('X2: ')), int(input('Y2: '))

# Processamento
d = ((x2 - x1)**2 + (y2-y1)**2) ** (1/2)

# Saída
print(f'A distância entre os dois pontos é: {d}')