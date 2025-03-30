# Entrada
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
e = int(input('e: '))
f = int(input('f: '))

# Processamento
x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

# Saída
print(f'Valor de x = {x}')
print(f'Valor de y = {y}')