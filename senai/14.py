notas = []

while True:
    nota = float(input("Digite uma nota (-1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

quantidade = len(notas)
print(f"\nQuantidade de valores lidos: {quantidade}")

print("Valores na ordem informada:", end=" ")
print(*notas)

print("Valores na ordem inversa:")
for nota in reversed(notas):
    print(nota)

soma = sum(notas)
print(f"\nSoma dos valores: {soma:.2f}")

media = soma / quantidade if quantidade > 0 else 0
print(f"Média dos valores: {media:.2f}")

acima_media = sum(1 for nota in notas if nota > media)
print(f"Quantidade de valores acima da média: {acima_media}")

abaixo_sete = sum(1 for nota in notas if nota < 7)
print(f"Quantidade de valores abaixo de sete: {abaixo_sete}")

print("\nPrograma encerrado. Obrigado por usar!")
