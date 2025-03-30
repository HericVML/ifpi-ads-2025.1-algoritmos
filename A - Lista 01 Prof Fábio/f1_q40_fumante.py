# Entrada
anos = int(input('Anos que fuma: '))
cigarros_dia = int(input('Cigarros por dia: '))
carteira_preco = float(input('Preço da carteira: '))

# Processamento
carteira_ano = (cigarros_dia / 20) * 365
carteira_vida = carteira_ano * anos
dinheiro_vida = carteira_vida * carteira_preco

# Saída
resultado = f'O dinheiro gasto em toda sua vida de fumante foi de R${dinheiro_vida:.2f}.'
print(resultado)