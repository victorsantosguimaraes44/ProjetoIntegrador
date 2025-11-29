import customtkinter as ctk

# Função que abre a janela de seleção
def abrir_janela_selecao(master, callback):
    # Cria uma nova janela
    selecao_window = ctk.CTkToplevel(master)
    selecao_window.title("Selecionar item")
    selecao_window.geometry("300x300")
    selecao_window.grab_set()  # deixa a janela "em foco" até o usuário fechar

    # Lista de opções
    opcoes = ["Fisioterapia", "Pilates", "Musculação", "Nutrição"]

    # Cria um botão para cada opção
    for opcao in opcoes:
        botao = ctk.CTkButton(
            selecao_window, 
            text=opcao, 
            command=lambda nome=opcao: (
                callback(nome),  # retorna o valor selecionado
                selecao_window.destroy()  # fecha a janela
            )
        )
        botao.pack(pady=8, padx=20, fill="x")

# Função principal
def main():
    app = ctk.CTk()
    app.geometry("400x300")
    app.title("Tela Principal")

    # Variável para armazenar o item selecionado
    item_selecionado = ctk.StringVar(value="Nenhum item selecionado")

    # Label que mostra o item escolhido
    label = ctk.CTkLabel(app, textvariable=item_selecionado, font=("Arial", 16))
    label.pack(pady=20)

    # Função que atualiza o texto da label
    def atualizar_item(nome):
        item_selecionado.set(f"Selecionado: {nome}")

    # Botão para abrir a tela de seleção
    botao_abrir = ctk.CTkButton(
        app,
        text="Selecionar Item",
        command=lambda: abrir_janela_selecao(app, atualizar_item)
    )
    botao_abrir.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    main()