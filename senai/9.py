preco_alcool = 1.90  
preco_gasolina = 2.50  

litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A - álcool, G - gasolina): ").strip().upper()

desconto = 0.0
preco_final = 0.0

if tipo_combustivel == 'A':
    
    if litros_vendidos <= 20:
        desconto = 0.03  
    else:
        desconto = 0.05  
    preco_final = litros_vendidos * preco_alcool * (1 - desconto)

elif tipo_combustivel == 'G':
    if litros_vendidos <= 20:
        desconto = 0.04  
    else:
        desconto = 0.06 
    preco_final = litros_vendidos * preco_gasolina * (1 - desconto)

else:
    print("Tipo de combustível inválido.")

if tipo_combustivel in ['A', 'G']:
    print(f"O valor a ser pago é: R$ {preco_final:.2f}")
