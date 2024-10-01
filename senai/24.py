def calcular_area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2

while True:
    try:
        base_maior = float(input("Digite o valor da base maior (deve ser maior que zero): "))
        if base_maior <= 0:
            raise ValueError("A base maior deve ser um número maior que zero.")
        
        base_menor = float(input("Digite o valor da base menor (deve ser maior que zero): "))
        if base_menor <= 0:
            raise ValueError("A base menor deve ser um número maior que zero.")
        
        altura = float(input("Digite o valor da altura do trapézio: "))
        if altura <= 0:
            raise ValueError("A altura deve ser um número maior que zero.")

    
        area = calcular_area_trapezio(base_maior, base_menor, altura)
        print(f"\nA área do trapézio é: {area:.2f}")

        break  
    except ValueError as e:
        print(f"Erro: {e}. Tente novamente.")
