# Entrada
latao = float(input('Quantidade de latão em kg: '))

# Processamento
cobre = (latao/100) * 70
zinco = (latao/100) * 30

# Saída
resultado = f'Para se obter {latao}kg de latão, deve-se possuir {cobre}kg de cobre e {zinco}kg de zinco.'
print(resultado)