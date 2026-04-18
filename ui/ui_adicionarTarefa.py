import tkinter as tk

def ui_janelaAdicionarTarefa():
    janela = tk.Toplevel()
    janela.title("Adicionar Tarefa")
    janela.geometry("300x200")
    janela.configure(bg="#ffeded")

    label_titulo = tk.Label(janela, text="Adicionar Tarefa", font=("Arial", 16))
    label_titulo.pack(pady=10)

    return janela