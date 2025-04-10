def calc_juros_comp(saldo_devedor, taxa_mensal, meses):
    return saldo_devedor * (1 + taxa_mensal / 100) ** meses


def simular_plano_pagamento(nome_plano, valor_fatura, valor_pago, meses_atraso):
    saldo_devedor = valor_fatura - valor_pago
    if saldo_devedor <= 0:
        print(f"\n{nome_plano}: Pagamento feito, sem juros ou multa.")
        return valor_fatura, valor_fatura, 0

    taxa_total = 12 + 2 + 1
    valor_corrigido = calc_juros_comp(saldo_devedor, taxa_total, meses_atraso)
    crescimento_percentual = ((valor_corrigido - saldo_devedor) / saldo_devedor) * 100

    print(f"\n{nome_plano} - Resultado após {meses_atraso} meses de atraso:")
    print(f"- Valor original da fatura: R$ {valor_fatura:.2f}")
    print(f"- Valor pago inicialmente: R$ {valor_pago:.2f}")
    print(f"- Saldo devedor: R$ {saldo_devedor:.2f}")
    print(f"- Valor da fatura após {meses_atraso} meses: R$ {valor_corrigido:.2f}")
    print(f"- Crescimento do saldo devedor: {crescimento_percentual:.2f}%")
    
    return saldo_devedor, valor_corrigido, crescimento_percentual


def simulador_cartao():
    print("----> Simulador de Fatura de Cartão de Crédito <----")

    valor_fatura = float(input("Valor total da fatura do mês: R$ "))

    valor_pago_p1 = float(input("Quanto deseja pagar no plano P1? R$ "))
    
    valor_pago_p2 = float(input("Quanto deseja pagar no plano P2? R$ "))

    meses = int(input("\nQuantos meses se passaram sem pagar o restante da fatura?: "))

    simular_plano_pagamento("Plano P1", valor_fatura, valor_pago_p1, meses)
    simular_plano_pagamento("Plano P2", valor_fatura, valor_pago_p2, meses)

simulador_cartao()
