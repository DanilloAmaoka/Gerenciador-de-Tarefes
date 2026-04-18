from ui.ui_main import ui_telaPrincipal
from ui.ui_adicionarTarefa import ui_janelaAdicionarTarefa


def adicionarTarefa():
    ui_janelaAdicionarTarefa()

janela = ui_telaPrincipal(adicionarTarefa)
janela.mainloop()