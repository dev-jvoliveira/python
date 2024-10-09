import tkinter as tk
from tkinter import messagebox

def calcular_salario():
    try:
        horas_aula = float(entry_horas.get())
        valor_hora = float(entry_valor.get())
        
        if honorista_var.get() == 1:  # Honorista
            salario = horas_aula * valor_hora
        else:  # Professor
            salario = (horas_aula * valor_hora) * 1.25
        
        label_resultado.config(text=f"Salário é: R$ {salario:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def limpar():
    entry_horas.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    label_resultado.config(text="")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Salário")

# Variáveis para o input radio
honorista_var = tk.IntVar(value=1)

# Botões de opção
radio_honorista = tk.Radiobutton(root, text="Honorista", variable=honorista_var, value=1)
radio_honorista.pack()

radio_professor = tk.Radiobutton(root, text="Professor", variable=honorista_var, value=2)
radio_professor.pack()

# Entradas de texto
label_horas = tk.Label(root, text="Digite a quantidade de horas/aula:")
label_horas.pack()
entry_horas = tk.Entry(root)
entry_horas.pack()

label_valor = tk.Label(root, text="Digite o valor da hora/aula:")
label_valor.pack()
entry_valor = tk.Entry(root)
entry_valor.pack()

# Botões
button_calcular = tk.Button(root, text="Calcular Salário Bruto", command=calcular_salario)
button_calcular.pack()

button_limpar = tk.Button(root, text="Limpar", command=limpar)
button_limpar.pack()

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack()

# Iniciar a aplicação
root.mainloop()
