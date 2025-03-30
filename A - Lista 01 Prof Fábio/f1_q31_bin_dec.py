# Entrada
binario_1 = int(input('Primeiro dígito binário: '))
binario_2 = int(input('Segundo dígito binário: '))
binario_3 = int(input('Terceiro dígito binário: '))
binario_4 = int(input('Quarto dígito binário: '))

# Processamento
bin_pot_1 = binario_1 * 2**3
bin_pot_2 = binario_2 * 2**2
bin_pot_3 = binario_3 * 2**1
bin_pot_4 = binario_4 * 2**0

binario = bin_pot_1  + bin_pot_2 + bin_pot_3 + bin_pot_4

# Saída
resultado = f'A conversão de binário para decimal resulta em: {binario}.'
print(resultado)