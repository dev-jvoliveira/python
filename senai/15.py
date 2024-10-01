aluno_mais_alto = None
altura_mais_alta = 0
aluno_mais_baixo = None
altura_mais_baixa = float('inf')  

for i in range(10):

    numero_aluno = int(input(f"Digite o número do aluno {i + 1}: "))
    altura_aluno = float(input(f"Digite a altura do aluno {i + 1} (em cm): "))


    if altura_aluno > altura_mais_alta:
        altura_mais_alta = altura_aluno
        aluno_mais_alto = numero_aluno

    if altura_aluno < altura_mais_baixa:
        altura_mais_baixa = altura_aluno
        aluno_mais_baixo = numero_aluno


print(f"\nAluno mais alto: Número {aluno_mais_alto}, Altura: {altura_mais_alta} cm")
print(f"Aluno mais baixo: Número {aluno_mais_baixo}, Altura: {altura_mais_baixa} cm")
