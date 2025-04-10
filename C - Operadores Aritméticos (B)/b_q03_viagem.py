def calc_consumo(dist_combustao, consumo_km_litro):
    return dist_combustao / consumo_km_litro


def calc_custo(litros, preco_litro):
    return litros * preco_litro


def simulador_viagem_hibrido():
    print("----> Planejador de Viagem - Carro Híbrido <----")

    dist_total = float(input("Distância total da viagem (km): "))
    percentual_eletrico = float(input("Percentual da viagem com motor elétrico (%): "))

    preco_gasolina = float(input("Valor do litro da gasolina: R$ "))
    preco_alcool = float(input("Valor do litro do álcool: R$ "))

    percentual_combustao = 100 - percentual_eletrico
    dist_combustao = (percentual_combustao / 100) * dist_total

    consumo_gasolina = 12
    consumo_alcool = 9.6

    litros_gasolina = calc_consumo(dist_combustao, consumo_gasolina)
    custo_gasolina = calc_custo(litros_gasolina, preco_gasolina)

    litros_alcool = calc_consumo(dist_combustao, consumo_alcool)
    custo_alcool = calc_custo(litros_alcool, preco_alcool)

    print("\n----> Tabela Comparativa <----")
    print(f"Distância com motor elétrico: {dist_total - dist_combustao:.2f} km")
    print(f"Distância com motor a combustão: {dist_combustao:.2f} km\n")

    print("Usando gasolina:")
    print(f"- Litros necessários: {litros_gasolina:.2f} L")
    print(f"- Custo estimado: R$ {custo_gasolina:.2f}")

    print("\nUsando álcool:")
    print(f"- Litros necessários: {litros_alcool:.2f} L")
    print(f"- Custo estimado: R$ {custo_alcool:.2f}")

simulador_viagem_hibrido()