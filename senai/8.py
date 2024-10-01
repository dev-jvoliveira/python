salario_atual = float(input("Digite o salário atual do funcionário: R$ "))

if salario_atual < 500:
    reajuste = 0.15  
elif 500 <= salario_atual <= 1000:
    reajuste = 0.10  
else:
    reajuste = 0.05  

novo_salario = salario_atual + (salario_atual * reajuste)

print(f"O novo salário reajustado é: R$ {novo_salario:.2f}")
