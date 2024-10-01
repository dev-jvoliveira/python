votos_candidatos = [0, 0, 0, 0] 
votos_nulos = 0
votos_branco = 0


while True:
    voto = int(input("Digite o código do voto (1-4 para candidatos, 5 para nulo, 6 para branco, 0 para encerrar): "))
    
    if voto == 0:
        break
    elif 1 <= voto <= 4:
        votos_candidatos[voto - 1] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_branco += 1
    else:
        print("Código de voto inválido. Tente novamente.")

total_votos = sum(votos_candidatos) + votos_nulos + votos_branco


print("\nResultados da Eleição:")
for i in range(4):
    print(f"Total de votos para o candidato {i + 1}: {votos_candidatos[i]}")

print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_branco}")


if total_votos > 0:
    porcentagem_nulos = (votos_nulos / total_votos) * 100
    porcentagem_brancos = (votos_branco / total_votos) * 100
    print(f"Percentagem de votos nulos: {porcentagem_nulos:.2f}%")
    print(f"Percentagem de votos em branco: {porcentagem_brancos:.2f}%")
else:
    print("Nenhum voto foi computado.")
