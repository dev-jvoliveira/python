nota1 = float(input("Digite a primeira nota (peso 2): "))
nota2 = float(input("Digite a segunda nota (peso 3): "))
nota3 = float(input("Digite a terceira nota (peso 5): "))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
    peso1 = 2
    peso2 = 3
    peso3 = 5
    media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

    print(f"Média Ponderada: {media_ponderada:.2f}")
else:
    print("As notas devem estar entre 0 e 10.0.")
