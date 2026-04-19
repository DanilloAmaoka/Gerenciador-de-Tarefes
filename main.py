import tkinter as tk

contador = 1

def janelaAdicionarTarefa():
    janela = tk.Toplevel()
    janela.title("Adicionar Tarefa")
    janela.geometry("300x150")
    janela.configure(bg="#ffeded")

    label_titulo = tk.Label(janela, text="Adicionar Tarefa", font=("Arial", 16))
    label_titulo.pack(pady=10)

    entry_tarefa = tk.Entry(janela, width=190)
    entry_tarefa.pack(pady=10)

    def SalvarTarefa(tarefa):
        global contador

        if tarefa == "":
            return
        frame_Tarefa = tk.Frame(scrollable_frame, bg="white", width=280, height=30)
        max_chars = 20
        texto = tarefa[:max_chars] + ("..." if len(tarefa) > max_chars else "")
        label_tarefa = tk.Label(frame_Tarefa, text=f"{contador} - {texto}", bg="white")
        contador += 1
        label_tarefa.pack(side="left", padx=10)
        check = tk.Checkbutton(frame_Tarefa, text="Concluído", bg="white")
        check.pack(side="right")
        bt_deletar = tk.Button(frame_Tarefa, text="Delete", bg="#febebe", width=6, command=lambda: frame_Tarefa.destroy())
        bt_deletar.pack(side="right", padx=5)
        frame_Tarefa.pack(pady=5, anchor="w")
        janela.destroy()
    
    bt_Salvar = tk.Button(janela, text="Salvar", width=280, bg="#febebe", command=lambda: SalvarTarefa(entry_tarefa.get()))
    bt_Salvar.pack()

    bt_Cancelar = tk.Button(janela, text="Cancelar", width=280, bg="#febebe", command=janela.destroy)
    bt_Cancelar.pack()

janelaInicial = tk.Tk()
janelaInicial.title("Gerenciador de Tarefas")
janelaInicial.geometry("350x400")
janelaInicial.configure(bg="#ffeded")

#-#
frame_superior = tk.Frame(janelaInicial, bg="#ffeded", width=350, height=50)
frame_superior.pack()
frame_superior.pack_propagate(False)

frame_central = tk.Frame(janelaInicial, bg="white", width=350, height=300)
frame_central.pack()
frame_central.pack_propagate(False)

frame_inferior = tk.Frame(janelaInicial, bg="#ffeded", width=350, height=50)
frame_inferior.pack()
frame_inferior.pack_propagate(False)
#-#

label_titulo = tk.Label(frame_superior, text="Menu", font=("Arial", 16))
label_titulo.pack(pady=5)

label_tarefas = tk.Label(frame_central, text="Tarefas:", font=("Arial", 12))
label_tarefas.pack(pady=10, anchor="w")

# Lista de tarefas
frame_Tarefas = tk.Frame(frame_central, bg="white")
frame_Tarefas.pack(anchor="w", padx=5)

canvas = tk.Canvas(frame_Tarefas, bg="white", width=320, height=250)
scrollbar = tk.Scrollbar(frame_Tarefas, orient="vertical", command=canvas.yview)

scrollable_frame = tk.Frame(canvas, bg="white")

# Scrollbar
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left")
scrollbar.pack(side="right", fill="y")
#-#

bt_Adicionar = tk.Button(frame_inferior, text="Adicionar Tarefa", width=280, height=50, bg="#febebe", command=janelaAdicionarTarefa)
bt_Adicionar.pack()

janelaInicial.mainloop()