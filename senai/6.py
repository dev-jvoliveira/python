def tipo_triangulo(lado1, lado2, lado3):
    """Determina o tipo de triângulo baseado nos lados."""
    if lado1 == lado2 == lado3:
        return "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "isósceles"
    else:
        return "escaleno"

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    tipo = tipo_triangulo(lado1, lado2, lado3)
    print(f"Os lados formam um triângulo {tipo}.")
else:
    print("Os valores informados não formam um triângulo.")
