def reverter_numero(numero):
    """Retorna o reverso de um número inteiro."""
    return int(str(numero)[::-1])

numero_inteiro = int(input("Digite um número inteiro: "))

reverso = reverter_numero(numero_inteiro)

print(f"O reverso de {numero_inteiro} é: {reverso}")
