# Entrada
meses = int(input('Meses: '))

# Processamento
anos = meses // 12
meses_restantes = meses % 12

# Saída
resultado = f'{meses} mês(es) equivalem a {anos} ano(s) e {meses_restantes} mês(es).'
print(resultado)