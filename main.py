contador = 1
lixeira = []
tarefas = []

def Interface():
    import tkinter as tk
    global contador
    global lixeira
    global tarefas

    def centralizar(janela, largura=300, altura=200):
        janela.update_idletasks()

        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()

        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)

        janela.geometry(f"{largura}x{altura}+{x}+{y}")

    def janelaAdicionarTarefa():
        janela = tk.Toplevel()
        janela.title("Adicionar Tarefa")
        janela.geometry("300x150")
        janela.configure(bg="#ffeded")
        centralizar(janela, 300, 150)

        label_titulo = tk.Label(janela, text="Adicionar Tarefa", font=("Arial", 16))
        label_titulo.pack(pady=10)

        entry_tarefa = tk.Entry(janela, width=190)
        entry_tarefa.pack(pady=10)

        def SalvarTarefa(tarefa):
            global contador

            def deletar(tarefa_deletada, texto_tarefa):
                global lixeira
                lixeira.append(texto_tarefa)
                tarefa_deletada.destroy()
                for r in lixeira:
                    print(r)

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
            bt_deletar = tk.Button(frame_Tarefa, text="Delete", bg="#febebe", width=6,
                                   command=lambda: deletar(frame_Tarefa, tarefa))
            bt_deletar.pack(side="right", padx=5)
            frame_Tarefa.pack(pady=5, anchor="w")
            janela.destroy()

        bt_Salvar = tk.Button(janela, text="Salvar", width=280, bg="#febebe",
                              command=lambda: SalvarTarefa(entry_tarefa.get()))
        bt_Salvar.pack()

        bt_Cancelar = tk.Button(janela, text="Cancelar", width=280, bg="#febebe", command=janela.destroy)
        bt_Cancelar.pack()

    def janelaLixeira():
        janela = tk.Toplevel()
        janela.title("Lixeira")
        janela.geometry("300x335")
        janela.configure(bg="#ffeded")
        centralizar(janela, 300, 335)

        label_titulo = tk.Label(janela, text="Lixeira", font=("Arial", 16))
        label_titulo.pack(pady=10)

        frame_Tarefas_Deletadas = tk.Frame(janela, bg="white")

        canvas = tk.Canvas(frame_Tarefas_Deletadas, bg="white", width=320, height=250)
        scrollbar = tk.Scrollbar(frame_Tarefas_Deletadas, orient="vertical", command=canvas.yview)

        bt_voltar = tk.Button(janela, text="Voltar", width=280, bg="#febebe", command=janela.destroy)

        scrollable_frame_tarefas_deletadas = tk.Frame(canvas, bg="white")

        scrollable_frame_tarefas_deletadas.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame_tarefas_deletadas, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left")
        scrollbar.pack(side="right", fill="y")

        for t in lixeira:
            label_t = tk.Label(scrollable_frame_tarefas_deletadas, text=t)
            label_t.pack(pady=5)
        frame_Tarefas_Deletadas.pack(anchor="w", padx=5)
        bt_voltar.pack()

    janelaInicial = tk.Tk()
    janelaInicial.title("Gerenciador de Tarefas")
    janelaInicial.geometry("350x460")
    janelaInicial.configure(bg="#ffeded")
    centralizar(janelaInicial, 350, 460)

    # -#
    frame_superior = tk.Frame(janelaInicial, bg="#ffeded", width=350, height=50)
    frame_superior.pack()
    frame_superior.pack_propagate(False)

    frame_central = tk.Frame(janelaInicial, bg="white", width=350, height=300)
    frame_central.pack()
    frame_central.pack_propagate(False)

    frame_inferior = tk.Frame(janelaInicial, bg="#ffeded", width=350, height=120)
    frame_inferior.pack()
    frame_inferior.pack_propagate(False)
    # -#

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
    # -#

    bt_Adicionar = tk.Button(frame_inferior, text="Adicionar Tarefa", width=280, bg="#febebe",
                             command=janelaAdicionarTarefa)
    bt_Adicionar.pack(pady=5)

    bt_Lixeira = tk.Button(frame_inferior, text="Lixeira", width=280, bg="#febebe", command=janelaLixeira)
    bt_Lixeira.pack(pady=5)

    bt_Fechar = tk.Button(frame_inferior, text="Fechar", width=280, bg="#febebe", command=janelaInicial.destroy)
    bt_Fechar.pack(pady=5)

    janelaInicial.mainloop()

def Terminal():
    global contador
    global tarefas
    global lixeira

    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Deletar tarefa")
        print("5 - Ver lixeira")
        print("6 - Sair")

        op = input("Escolha: ")

        # ADICIONAR
        if op == "1":
            tarefa = input("Digite a tarefa: ")

            if tarefa == "":
                print("Tarefa vazia!")
                continue

            tarefas.append({
                "id": contador,
                "texto": tarefa,
                "concluida": False
            })
            contador += 1

        # LISTAR
        elif op == "2":
            if not tarefas:
                print("Nenhuma tarefa.")
                continue

            print("\nTarefas:")
            for t in tarefas:
                status = "✔" if t["concluida"] else " "
                texto = t["texto"][:20] + ("..." if len(t["texto"]) > 20 else "")
                print(f'{t["id"]} - [{status}] {texto}')

        # CONCLUIR
        elif op == "3":
            try:
                num = int(input("Número da tarefa: "))
                for t in tarefas:
                    if t["id"] == num:
                        t["concluida"] = True
                        break
                else:
                    print("Não encontrada.")
            except:
                print("Entrada inválida.")

        # DELETAR
        elif op == "4":
            try:
                num = int(input("Número da tarefa: "))
                for t in tarefas:
                    if t["id"] == num:
                        lixeira.append(t["texto"])
                        tarefas.remove(t)
                        break
                else:
                    print("Não encontrada.")
            except:
                print("Entrada inválida.")

        # LIXEIRA
        elif op == "5":
            print("\n=== LIXEIRA ===")
            if not lixeira:
                print("Vazia.")
            else:
                for i, t in enumerate(lixeira, 1):
                    print(f"{i} - {t}")

        # SAIR
        elif op == "6":
            break

        else:
            print("Opção inválida.")

print("1. Interface, 2. Terminal(Docker-Para a atividade)")
escolha = input(": ")

if escolha == "1":
    Interface()
if escolha == "2":
    Terminal()