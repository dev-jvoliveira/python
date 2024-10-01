notas = []
for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)


media = sum(notas) / len(notas)


print(f"A média final é: {media:.2f}")

if media >= 7:
    print("APROVADO")
else:
    nota_final = float(input("Digite a nota da prova final: "))
    
    nova_media = (media + nota_final) / 2
    print(f"A nova média é: {nova_media:.2f}")

    if nova_media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")
