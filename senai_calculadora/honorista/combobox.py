import tkinter as tk
from tkinter import messagebox, ttk

def calcular_salario():
    try:
        horas_aula = float(entry_horas.get())
        valor_hora = float(entry_valor.get())
        tipo_professor = combo_tipo.get()
        
        if tipo_professor == "Honorista":  # Honorista
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
    combo_tipo.set("Honorista")  # Resetar para o valor padrão

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Salário")

# Combobox para selecionar tipo
label_tipo = tk.Label(root, text="Selecione o tipo:")
label_tipo.pack()
combo_tipo = ttk.Combobox(root, values=["Honorista", "Professor"])
combo_tipo.set("Honorista")  # Valor padrão
combo_tipo.pack()

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
