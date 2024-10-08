import tkinter as tk
from typing import List


def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('CALCULADORA DO JOÃO')
    root.config(padx=10, 
    pady=10, 
    background='#000')
    root.resizable(False, False)
    return root


def make_label(root, **grid_options) -> tk.Label:
    label = tk.Label(
        root, 
        text='Sem conta ainda',
        anchor='e', 
        justify='right', 
        background='#000',
        foreground='#fff'
    )
    label.grid(**grid_options)
    return label


def make_display(root, **grid_options) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(**grid_options)
    display.config(
        font=('Helvetica', 30, 'bold'),
        justify='right',
        bd=1,
        relief='flat',
        highlightthickness=1,
        highlightcolor='#fff',
        background='#000',  
        foreground='white',  
        insertbackground='white'  
    )
    display.bind('<Control-a>', _display_control_a)
    return display



def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

#FUNÇÃO PARA ADICIONAR EFEITO DE HOVER
def on_enter(event):
    event.widget.config(background='#e0e0e0')  #cor do (hover)

def on_leave(event):
    if event.widget['text'] == 'C':
        event.widget.config(background='#EA4335')  #vermelho claro botão 'C'
    elif event.widget['text'] == '=':
        event.widget.config(background='#4785F4')  #azul botão '='
    else:
        event.widget.config(background='#f1f2f3')  #cor padrão para os outros botões

def make_button(root, text, **grid_options) -> tk.Button:
    if text == 'C':
        background_color = '#ff6961'  #vermelho claro para o botão 'C'
    elif text == '=':
        background_color = '#61a0ff'  #azul para o botão '='
    else:
        background_color = '#f1f2f3'  #cor padrão para os outros botões
    
    btn = tk.Button(root, text=text)
    btn.grid(**grid_options)
    btn.config(
        font=('Helvetica', 20, 'normal'),
        pady=15, width=1, 
        background=background_color,  #cor inicial do botão
        bd=0,
        cursor='hand2', 
        highlightthickness=0,
        highlightcolor='#ccc', 
        activebackground='#ccc',
        highlightbackground='#ccc'
    )
    
    # Bind de hover
    btn.bind("<Enter>", on_enter)  # Ao passar o mouse
    btn.bind("<Leave>", on_leave)  # Ao retirar o mouse
    
    return btn

def make_buttons(root, starting_row) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    buttons: List[List[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=starting_row):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = make_button(
                root, 
                text=col_value,
                row=row, 
                column=col_index, 
                sticky='news', 
                padx=2, 
                pady=2
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons
