def calcular_salario_atual(salario_inicial):
    ano_inicial = 1995
    salario_atual = salario_inicial
    percentual_aumento = 1.5 / 100  

    for ano in range(1996, 2024):  
        salario_atual += salario_atual * percentual_aumento
        percentual_aumento *= 2  

    return salario_atual

while True:
    try:
        salario_inicial = float(input("Digite o salário inicial do funcionário (R$): "))
        if salario_inicial < 0:
            raise ValueError("O salário inicial deve ser um valor positivo.")

        salario_atual = calcular_salario_atual(salario_inicial)
        print(f"\nO salário atual do funcionário é: R$ {salario_atual:.2f}")
        break
    except ValueError as e:
        print(f"Erro: {e}. Tente novamente.")
