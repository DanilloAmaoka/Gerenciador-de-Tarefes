import tkinter as tk

def janelaAdicionarTarefa():
    janela = tk.Toplevel()
    janela.title("Adicionar Tarefa")
    janela.geometry("300x200")
    janela.configure(bg="#ffeded")

    label_titulo = tk.Label(janela, text="Adicionar Tarefa", font=("Arial", 16))
    label_titulo.pack(pady=10)

    return janela

janelaInicial = tk.Tk()
janelaInicial.title("Gerenciador de Tarefas")
janelaInicial.geometry("300x400")
janelaInicial.configure(bg="#ffeded")

#-#
frame_superior = tk.Frame(janelaInicial, bg="#ffeded", width=300, height=50)
frame_superior.pack()
frame_superior.pack_propagate(False)

frame_central = tk.Frame(janelaInicial, bg="white", width=300, height=300)
frame_central.pack()
frame_central.pack_propagate(False)

frame_inferior = tk.Frame(janelaInicial, bg="#ffeded", width=300, height=50)
frame_inferior.pack()
frame_inferior.pack_propagate(False)
#-#

label_titulo = tk.Label(frame_superior, text="Menu", font=("Arial", 16))
label_titulo.pack(pady=5)

label_tarefas = tk.Label(frame_central, text="Tarefas:", font=("Arial", 12))
label_tarefas.pack(pady=10, anchor="w")

bt_Adicionar = tk.Button(frame_inferior, text="Adicionar Tarefa", width=280, height=50, bg="#febebe", command=janelaAdicionarTarefa)
bt_Adicionar.pack()

janelaInicial.mainloop()