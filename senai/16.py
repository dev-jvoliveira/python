numero = int(input("Digite um número: "))

soma = 0

for i in range(1, numero + 1):
    soma += i

print(f"A soma de todos os números de 1 até {numero} é: {soma}")
