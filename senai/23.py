PRECO_DIA = 60.00
PRECO_KM = 0.15

dias_alugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))
km_percorridos = float(input("Digite a quantidade de km percorridos: "))

custo_dias = dias_alugados * PRECO_DIA
custo_km = km_percorridos * PRECO_KM
preco_total = custo_dias + custo_km

print(f"\nCusto total pelo aluguel:")
print(f"Custo por dias: R$ {custo_dias:.2f}")
print(f"Custo por km: R$ {custo_km:.2f}")
print(f"Preço total a pagar: R$ {preco_total:.2f}")
