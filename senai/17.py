precos = {
    'Filé Duplo': (4.90, 5.80),
    'Alcatra': (5.90, 6.80),
    'Picanha': (6.90, 7.80)
}

tipo_carne = input("Digite o tipo de carne (Filé Duplo, Alcatra, Picanha): ")
quantidade_kg = float(input("Digite a quantidade em Kg: "))
tipo_pagamento = input("Digite o tipo de pagamento (Cartão ou Dinheiro): ")


if tipo_carne in precos:

    if quantidade_kg <= 5:
        preco_kg = precos[tipo_carne][0]
    else:
        preco_kg = precos[tipo_carne][1]


    total = preco_kg * quantidade_kg
    desconto = 0


    if tipo_pagamento.lower() == "cartão":
        desconto = total * 0.05
        total -= desconto


    print("\nCupom Fiscal")
    print("Tipo de Carne:", tipo_carne)
    print("Quantidade (Kg):", quantidade_kg)
    print("Preço Total: R$ {:.2f}".format(preco_kg * quantidade_kg))
    print("Tipo de Pagamento:", tipo_pagamento)
    print("Valor do Desconto: R$ {:.2f}".format(desconto))
    print("Valor a Pagar: R$ {:.2f}".format(total))
else:
    print("Tipo de carne inválido.")
