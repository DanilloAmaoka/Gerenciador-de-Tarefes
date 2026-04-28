from src.main import adicionar_tarefa, concluir_tarefa, deletar_tarefa

def test_adicionar():
    tarefas = []
    contador = 1

    tarefas, contador = adicionar_tarefa(tarefas, contador, "Estudar")

    assert len(tarefas) == 1
    assert tarefas[0]["texto"] == "Estudar"
    assert contador == 2

def test_concluir():
    tarefas = [{"id": 1, "texto": "Estudar", "concluida": False}]

    resultado = concluir_tarefa(tarefas, 1)

    assert resultado == True
    assert tarefas[0]["concluida"] == True

def test_deletar():
    tarefas = [{"id": 1, "texto": "Estudar", "concluida": False}]
    lixeira = []

    resultado = deletar_tarefa(tarefas, lixeira, 1)

    assert resultado == True
    assert len(tarefas) == 0
    assert lixeira[0] == "Estudar"

def test_adicionar_vazio():
    tarefas = []
    contador = 1

    tarefas, contador = adicionar_tarefa(tarefas, contador, "")

    assert len(tarefas) == 0
    assert contador == 1

def test_concluir_inexistente():
    tarefas = [{"id": 1, "texto": "Estudar", "concluida": False}]

    resultado = concluir_tarefa(tarefas, 2)

    assert resultado == False
    assert tarefas[0]["concluida"] == False