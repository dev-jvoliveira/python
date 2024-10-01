def calcular_media(notas):
    notas.remove(max(notas)) 
    notas.remove(min(notas))  
    media = sum(notas) / len(notas)  
    return media

nome_atleta = input("Digite o nome do atleta: ")

notas = []

for i in range(1, 8):  
    nota = float(input(f"Nota {i}: "))
    notas.append(nota)

media = calcular_media(notas)


melhor_nota = max(notas)
pior_nota = min(notas)

print("\nResultado final:")
print(f"Atleta: {nome_atleta}")
print(f"Melhor nota: {melhor_nota:.1f}")
print(f"Pior nota: {pior_nota:.1f}")
print(f"Média: {media:.2f}")
