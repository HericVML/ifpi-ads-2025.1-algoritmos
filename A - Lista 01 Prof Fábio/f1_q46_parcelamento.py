# Entrada
valor_bem = float(input('Valor do bem (R$) :'))

# Processamento
parcela = valor_bem // 3
entrada = (valor_bem % 3) + parcela

# Saída
print(f'Entrada = R${entrada:.2f}')
print(f'+ 2 parcelas de R${parcela:.2f}')