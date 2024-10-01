valor_hora = float(input("Digite o valor da hora: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

ir = 0.0
inss = salario_bruto * 0.10  
fgts = salario_bruto * 0.11  

if salario_bruto <= 900:
    ir = 0.0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

total_descontos = ir + inss

salario_liquido = salario_bruto - total_descontos


print("\n--- Folha de Pagamento ---")
print(f"Salário Bruto: (R$ {valor_hora:.2f} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({int(ir/salario_bruto*100)}%) : R$ {ir:.2f}")
print(f"(-) INSS (10%) : R$ {inss:.2f}")
print(f"FGTS (11%) : R$ {fgts:.2f}")
print(f"Total de Descontos : R$ {total_descontos:.2f}")
print(f"Salário Líquido : R$ {salario_liquido:.2f}")
