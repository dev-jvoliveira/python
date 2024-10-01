def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperaturas_fahrenheit = []


print("Digite as temperaturas em Fahrenheit (deixe em branco para encerrar):")
while True:
    entrada = input("Temperatura em °F: ")
    if entrada == "": 
        break
    try:
        temperatura = float(entrada)
        temperaturas_fahrenheit.append(temperatura)
    except ValueError:
        print("Por favor, insira um número válido.")

print("\nTemperaturas convertidas:")
for temperatura_f in temperaturas_fahrenheit:
    temperatura_c = fahrenheit_para_celsius(temperatura_f)
    print(f"{temperatura_f:.1f} °F corresponde a {temperatura_c:.1f} °C")
