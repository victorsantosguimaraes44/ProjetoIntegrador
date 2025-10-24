import customtkinter as ctk
from tela_cadastro_usuario_pilates import obter_cadastros
# from gerador_de_dados_aleatorios import obter_dados_aleatorios

def tela_lista_alunos_pilates(JANELA):
    
    
    frame = ctk.CTkFrame(master=JANELA, width=1200, height=750)
    frame.place(relx=0.5, rely=0.5,anchor='center')
    frame.pack_propagate(False)

    campo_pesquisar = ctk.CTkEntry(master=frame, placeholder_text="Pesquisar", font=('Arial', 15), width=300, height=30, corner_radius=10, border_color="#BFBFBF")
    campo_pesquisar.place(x=10,y=10)

    list_label = ctk.CTkLabel(master=frame,text="Lista de pacientes", font=('Arial', 25, 'bold'))
    list_label.pack(pady=(10,10))
    
    frame_btn_name = ctk.CTkScrollableFrame(master=JANELA, width=1185, height=600, corner_radius=0, fg_color="#FFFFFF")
    frame_btn_name.place(relx=0.5, rely=0.5,anchor='center')

    for i in range(len(obter_cadastros())):
        frame_cadastro = ctk.CTkFrame(master=frame_btn_name, width=1150, height=40, corner_radius=5, fg_color="#E3E3E3", border_width=2, border_color="#D8D8D8")
        frame_cadastro.pack_propagate(False)
        frame_cadastro.pack(pady=2)

        btn_name = ctk.CTkButton(master=frame_cadastro, text=obter_cadastros()[i]["nome"], font=('Arial', 25), 
                                width=1100, height=40, corner_radius=0, text_color="#000000",
                                fg_color="#FFFFFF", hover_color="#929090", command=lambda nome=obter_cadastros()[i]["nome"]: informacoes(nome))
        btn_name.pack(pady=2)

    def atualizar_lista(filtro=""):
            # Limpa o frame antes de repopular
            for widget in frame_btn_name.winfo_children():
                widget.destroy()
            cadastros = obter_cadastros()
            for cadastro in cadastros:
                nome = cadastro["nome"]
                if filtro.lower() in nome.lower():  # Filtra pelo texto digitado
                    frame_cadastro = ctk.CTkFrame(master=frame_btn_name, width=1150, height=40, corner_radius=5,fg_color="#E3E3E3", 
                                                  border_width=2, border_color="#D8D8D8"
                    )
                    frame_cadastro.pack_propagate(False)
                    frame_cadastro.pack(pady=2)

                    btn_name = ctk.CTkButton(
                        master=frame_cadastro, text=nome, font=('Arial', 20),width=1100, height=40, corner_radius=0, text_color="#000000",
                        fg_color="#FFFFFF", hover_color="#929090",command=lambda n=nome: informacoes(n)
                    )
                    btn_name.pack(pady=2)

        # Atualiza a lista toda no início
    atualizar_lista()

        # --- Detecta digitação e filtra ---
    def ao_digitar(event):
            texto = campo_pesquisar.get()
            atualizar_lista(texto)

    campo_pesquisar.bind("<KeyRelease>", ao_digitar)

def informacoes(nome):
    ctk.set_appearance_mode('light')
    ctk.set_default_color_theme('blue')

    janela = ctk.CTk()
    janela.geometry("800x300")
    janela.resizable(False, False)
    janela.title('Infos')

    frame = ctk.CTkFrame(master=janela, width=800, height=300)
    frame.place(relx=0.5, rely=0.5, anchor='center')
    frame.pack_propagate(False)

    for cadastro in obter_cadastros():
        if cadastro["nome"] == nome:
            email = cadastro['email']
            cpf = cadastro['cpf']
            data_nascimento = cadastro['data_nascimento']
            telefone = cadastro['telefone']
            opcao_pagamento = cadastro['opcao_pagamento']
            valor_pagar = cadastro['valor_pagar']
            endereco = cadastro['endereco']
            break

    ctk.CTkLabel(frame, text=f"Nome: {nome}", font=('Arial', 15)).grid(row=0,column=0, sticky='w',padx=10, pady=2)
    ctk.CTkLabel(frame, text=f"CPF: {cpf}", font=('Arial', 15)).grid(row=0,column=1, sticky='w',padx=10, pady=2)
    ctk.CTkLabel(frame, text=f"Data de nascimento: {data_nascimento}", font=('Arial', 15)).grid(row=1,column=0, sticky='w',padx=10, pady=2)
    ctk.CTkLabel(frame, text=f"Email: {email}", font=('Arial', 15)).grid(row=1,column=1, sticky='w',padx=10, pady=2)
    ctk.CTkLabel(frame, text=f"Telefone: {telefone}", font=('Arial', 15)).grid(row=2,column=0, sticky='w',padx=10, pady=2)
    ctk.CTkLabel(frame, text=f"Endereço: {endereco}", font=('Arial', 15)).grid(row=2,column=1, sticky='w',padx=10, pady=2)
    ctk.CTkLabel(frame, text=f"Opção de pagamento: {opcao_pagamento}", font=('Arial', 15)).grid(row=3,column=0, sticky='w',padx=10, pady=2)
    ctk.CTkLabel(frame, text=f"Valor a pagar: {valor_pagar}", font=('Arial', 15)).grid(row=3,column=1, sticky='w',padx=10, pady=2)


    janela.mainloop()