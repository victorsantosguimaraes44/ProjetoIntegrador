from tkinter import messagebox
from turtle import left
import customtkinter as ctk
# from gerador_de_dados_aleatorios import obter_dados_aleatorios
# from gerador_de_dados_aleatorios import gerar_dados_aleatorios

cadastros = []
cadastro = " "
def adicionar_cadastros(nome, email, telefone, opcao_pagamento, valor_pagar):
    cadastro = f"nome: {nome}, email: {email}, tel: {telefone}, pagamento: {opcao_pagamento}, valor a pagar: {valor_pagar}"
    cadastros.append(cadastro)

def obter_cadastros():
    return cadastros

def abrir_cadastro_fisioterapia(JANELA):
    #FRAME PRINCIPAL
    frame_principal = ctk.CTkFrame(master=JANELA, width=1200, height=750, corner_radius=10, fg_color="transparent")
    frame_principal.place(relx=0.5, rely=0.5,anchor='center')
    frame_principal.pack_propagate(False)

    #TITULO
    titulo = ctk.CTkLabel(master=frame_principal, text="Cadastro de usuário", font=('Arial', 30, 'bold'))
    titulo.pack(pady=(10,10))

    #SUBTITULO
    subtitulo = ctk.CTkLabel(master=frame_principal, text="Digite os campos necessários abaixo", font=('Arial', 20, 'bold'))
    subtitulo.pack(pady=(2,10))

    ##================== CAMPOS ==================

    #FRAME CAMPOS
    frame_campos = ctk.CTkFrame(master=JANELA, width=400, height=450 ,corner_radius=5, fg_color="transparent")
    frame_campos.place(relx=0.5, rely=0.5,anchor='s')
    frame_campos.pack_propagate(False)

    # CAMPO NOME
    cmp_nome = ctk.CTkEntry(master=frame_campos, placeholder_text="Nome completo", font=('Arial',20) , width=350, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_nome.pack(pady=(10,10))
    cmp_nome.grid(row=0, column=0, padx=2, pady=2)

    # CAMPO DATA DE NASCIMENTO
    cmp_dataNascimento = ctk.CTkEntry(master=frame_campos, placeholder_text="Data de Nascimento", font=('Arial',20), width=350, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_dataNascimento.pack(pady=(10,10))
    cmp_dataNascimento.grid(row=0, column=1, padx=2, pady=2)

    # CAMPO EMAIL
    cmp_email = ctk.CTkEntry(master=frame_campos, placeholder_text="Email", font=('Arial',20) , width=350, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_email.pack(pady=(10,10))
    cmp_email.grid(row=1, column=0, padx=2, pady=2)

    # CAMPO TELEFONE
    cmp_tel = ctk.CTkEntry(master=frame_campos, placeholder_text="Telefone", font=('Arial',20), width=350, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_tel.pack(pady=(10,10))
    cmp_tel.grid(row=1, column=1, padx=2, pady=2)

    # OPÇÃO DE PAGAMENTO
    subtitulo = ctk.CTkLabel(master=frame_campos,text="Opção de pagamento: ",font=('Arial',20))
    subtitulo.grid(row=2, column=0, padx=0.5, pady=0.5)

    opc_pgt = ctk.CTkComboBox(master=frame_campos, values=["-Selecione-","Pix", "Débito", "Crédito"],font=('Arial',20) )
    opc_pgt.pack(pady=(1,1))
    opc_pgt.grid(row=3, column=0, padx=0.5, pady=0.5)

    # CAMPO VALOR A PAGAR
    def formatar_para_reais(*args):
        valor = var_valor.get()

        # Remove "R$" e espaços para tratar apenas o número
        if valor.startswith("R$"):
            valor = valor[2:].strip()

        # Remove qualquer caractere não numérico exceto vírgula e ponto
        valor = ''.join(c for c in valor if c.isdigit() or c in ",.")

        # Atualiza o campo com o prefixo "R$"
        var_valor.set(f"R$ {valor}")

    cmp_valor_pagar_titulo = ctk.CTkLabel(master=frame_campos,text="valor a pagar R$: ",font=('Arial',20))
    cmp_valor_pagar_titulo.grid(row=2, column=1, padx=0.5, pady=0.5)
    var_valor = ctk.StringVar()
    var_valor.trace_add("write", formatar_para_reais)

    cmp_valor_pagar = ctk.CTkEntry(master=frame_campos, textvariable=var_valor, font=('Arial',20), width=150, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_valor_pagar.pack(pady=(10,10))
    cmp_valor_pagar.grid(row=3, column=1, padx=2, pady=2)

    #================== BOTÕES ==================
    # FRAMEBOTOES
    frame_btn = ctk.CTkFrame(master=frame_principal, width=400, height=450, fg_color="transparent")
    frame_btn.place(relx=0.5, rely=0.8,anchor='n')

    # BOTAO SALVAR

    # def on_button_click():
        # gerar_dados_aleatorios()
        # obter_dados_aleatorios()

    def salvar(): 
        nome = cmp_nome.get()
        email = cmp_email.get()
        data_nascimento = cmp_dataNascimento.get()
        telefone = cmp_tel.get()
        opcao_pagamento = opc_pgt.get()
        valor_pagar = cmp_valor_pagar.get()
        
        if not nome or not email or not data_nascimento or not telefone:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
        elif opcao_pagamento == "-Selecione-":
            messagebox.showwarning("Atenção", "Coloque uma opção de pagamento!")
            return
        else:
            messagebox.showinfo("INFO", f"O paciente '{nome}' foi cadastrado com sucesso!")
            adicionar_cadastros(nome, email, telefone, opcao_pagamento, valor_pagar)


    btn_salvar = ctk.CTkButton(master=frame_btn, text='Salvar', text_color="#000000",width=150,height=40, 
                                corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049", command=salvar)
    btn_salvar.pack(pady=(10,10), side = 'left', padx = 5)

    # btn_dados_aleatorios = ctk.CTkButton(master=frame_btn, text='dds ale', text_color="#000000",width=150,height=40, 
    #                             corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049", command=on_button_click)
    # btn_dados_aleatorios.pack(pady=(10,10))
