def calc_cdb(valor_investido, taxa_anual, anos):
    montante = valor_investido * (1 + taxa_anual / 100) ** anos
    return montante


def calc_parcela_cdc(valor_emprestado, taxa_mensal, meses):
    i = taxa_mensal / 100
    parcela = valor_emprestado * (i * (1 + i) ** meses) / ((1 + i) ** meses - 1)
    return parcela


def calc_total_cdc(parcela, meses):
    return parcela * meses


def simulador():
    print("----> Simulador CDB e CDC <----\n")

    valor = float(input("Valor a ser investido: R$"))
    taxa_cdb = float(input("Taxa de juros do CDB (% ao ano): "))
    ano_final = int(input("Ano de vencimento do CDB: "))
    ano_atual = 2025
    anos = ano_final - ano_atual

    mont_cdb = calc_cdb(valor, taxa_cdb, anos)
    print(f"\nInvestidor receberá R$ {mont_cdb:.2f} ao final de {anos} anos")

    taxa_cdc = float(input("\nTaxa de juros do CDC (% ao mês): "))
    meses = int(input("Número de parcelas: "))

    parcela = calc_parcela_cdc(valor, taxa_cdc, meses)
    total_cdc = calc_total_cdc(parcela, meses)
    juros_total = total_cdc - valor

    print(f"\nCliente pagará {meses} parcelas de R${parcela:.2f}")
    print(f"Total pago ao banco: R${total_cdc:.2f}")
    print(f"Juros pagos pelo cliente: R${juros_total:.2f}")

    lucro = total_cdc - mont_cdb
    print(f"\nLucro do banco: R${lucro:.2f}")

    print("\n----> Resumo final <----")
    print(f"Valor investido: R${valor:.2f}")
    print(f"CDB: taxa de {taxa_cdb}% ao ano | Prazo: {anos} anos | Total a pagar: R${mont_cdb:.2f}")
    print(f"CDC: taxa de {taxa_cdc}% ao mês | Prazo: {meses} meses | Total recebido: R${total_cdc:.2f}")
    print(f"Lucro final do banco: R${lucro:.2f}")


simulador()