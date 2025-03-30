# Eu não soube deixar o númerador final em int então botei tudo float logo.
# Entrada
num_1 = float(input('Numerador 1: '))
den_1 = float(input('Denominador 1: '))
num_2 = float(input('Numerador 2: '))
den_2 = float(input('Denominador 2: '))

# Processamento
# fração 1 = num_1 / den_1
# fração 2 = num_2 / den_2

denominador_final = den_1 * den_2

num_final_1 = (denominador_final / den_1) * num_1
num_final_2 = (denominador_final / den_2) * num_2

numerador_final = num_final_1 + num_final_2

# Saída
resultado = f'A fração final é: {numerador_final}/{denominador_final}.'
print(resultado)