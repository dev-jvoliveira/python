def reverter_numero(numero):
    return int(str(numero)[::-1])

numero_informado = int(input("Digite um número inteiro: "))

numero_reverso = reverter_numero(numero_informado)

print(f"O reverso do número {numero_informado} é: {numero_reverso}")
