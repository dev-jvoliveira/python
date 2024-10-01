def soma(a, b):
    return a + b

def diferenca(a, b):
    return a - b

def produto(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        return a / b

while True:

    print("\nEscolha a opção:")
    print("1 - Soma de 2 números")
    print("2 - Diferença entre 2 números (maior pelo menor)")
    print("3 - Produto entre 2 números")
    print("4 - Divisão entre 2 números (o denominador não pode ser zero)")
    print("5 - Sair")

    escolha = input("Digite sua escolha (1/2/3/4/5): ")
    
    if escolha in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if escolha == "1":
            resultado = soma(num1, num2)
            print(f"Soma: {resultado}")
        
        elif escolha == "2":
            resultado = diferenca(max(num1, num2), min(num1, num2))
            print(f"Diferença: {resultado}")
        
        elif escolha == "3":
            resultado = produto(num1, num2)
            print(f"Produto: {resultado}")
        
        elif escolha == "4":
            resultado = divisao(num1, num2)
            print(f"Divisão: {resultado}")

    elif escolha == "5":
        print("Saindo do programa. Até logo!")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
