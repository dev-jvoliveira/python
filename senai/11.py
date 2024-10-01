preco_morango_ate_5kg = 2.50  
preco_morango_acima_5kg = 2.20  
preco_maca_ate_5kg = 1.80  
preco_maca_acima_5kg = 1.50  

qtd_morango = float(input("Digite a quantidade de morangos (em Kg): "))
qtd_maca = float(input("Digite a quantidade de maçãs (em Kg): "))

if qtd_morango <= 5:
    preco_morango = qtd_morango * preco_morango_ate_5kg
else:
    preco_morango = qtd_morango * preco_morango_acima_5kg

if qtd_maca <= 5:
    preco_maca = qtd_maca * preco_maca_ate_5kg
else:
    preco_maca = qtd_maca * preco_maca_acima_5kg

total_compra = preco_morango + preco_maca

if (qtd_morango + qtd_maca) > 8 or total_compra > 25:
    total_compra *= 0.90  

print(f"O valor total a ser pago pelo cliente é: R$ {total_compra:.2f}")
