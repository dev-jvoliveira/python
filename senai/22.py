cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}

total_pedido = 0

print("Cardápio da Lanchonete:")
for codigo, (item, preco) in cardapio.items():
    print(f"Código: {codigo} - Item: {item} - Preço: R$ {preco:.2f}")

while True:
    codigo_item = int(input("\nDigite o código do item (ou 0 para encerrar o pedido): "))
    
    if codigo_item == 0:
        break
    
    if codigo_item in cardapio:
        quantidade = int(input("Digite a quantidade: "))
        item, preco = cardapio[codigo_item]
        
        valor_item = preco * quantidade
        total_pedido += valor_item
        
        print(f"Valor a ser pago por {quantidade} {item}(s): R$ {valor_item:.2f}")
    else:
        print("Código de item inválido. Tente novamente.")

print(f"\nTotal geral do pedido: R$ {total_pedido:.2f}")
