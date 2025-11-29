from tkinter import messagebox
from turtle import left
import customtkinter as ctk

cadastros = []
cadastro = " "
def adicionar_cadastros(nome, cpf, email, telefone, data_nascimento, endereco):
    # cadastro = f"{nome}, {email}, {telefone}, {opcao_pagamento}, {valor_pagar}, {endereco}"
    DADOS_CADASTRAIS = {"nome":nome, 'cpf':cpf,"email":email, "telefone":telefone, "data_nascimento": data_nascimento, "endereco":endereco}
    cadastros.append(DADOS_CADASTRAIS)
def obter_cadastros():
    return cadastros

def abrir_cadastro_fisioterapia(atualizar_callback=None):

    ctk.set_appearance_mode('light')
    ctk.set_default_color_theme('blue')

    janela = ctk.CTk()
    janela.geometry("800x600")
    janela.resizable(False, False)
    janela.title('Fisioterapia - Cadastro')
    janela.attributes("-topmost", True)
    #FRAME PRINCIPAL
    frame_principal = ctk.CTkFrame(master=janela, width=800, height=600, corner_radius=10)
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
    frame_campos = ctk.CTkFrame(master=janela, width=400, height=450 ,corner_radius=5, fg_color="transparent")
    frame_campos.place(relx=0.5, rely=0.5,anchor='s')
    frame_campos.pack_propagate(False)

    # CAMPO NOME
    nome_lbl = ctk.CTkLabel(frame_campos, text='Nome Completo', font=('Arial',20))
    nome_lbl.grid(row=0, column=0, padx=20, pady=2, sticky='w')
    cmp_nome = ctk.CTkEntry(master=frame_campos, placeholder_text="", font=('Arial',20) , width=350, height=20, corner_radius=10, border_color="#BFBFBF")
    cmp_nome.pack(pady=(10,10))
    cmp_nome.grid(row=1, column=0, padx=20, pady=2)

    # CAMPO DATA DE NASCIMENTO
    data_nsc_lbl = ctk.CTkLabel(frame_campos, text='Data de Nascimento', font=('Arial',20))
    data_nsc_lbl.grid(row=0, column=1, padx=20, pady=2, sticky='w')
    cmp_dataNascimento = ctk.CTkEntry(master=frame_campos, placeholder_text="", font=('Arial',20), width=350, height=20, corner_radius=10, border_color="#BFBFBF")
    cmp_dataNascimento.pack(pady=(10,10))
    cmp_dataNascimento.grid(row=1, column=1, padx=20, pady=2)

    # CAMPO EMAIL
    email_lbl = ctk.CTkLabel(frame_campos, text='Email', font=('Arial',20))
    email_lbl.grid(row=2, column=0, padx=20, pady=2, sticky='w')
    cmp_email = ctk.CTkEntry(master=frame_campos, placeholder_text="", font=('Arial',20) , width=350, height=20, corner_radius=10, border_color="#BFBFBF")
    cmp_email.pack(pady=(10,10))
    cmp_email.grid(row=3, column=0, padx=20, pady=2)

    # CAMPO TELEFONE
    tel_lbl = ctk.CTkLabel(frame_campos, text='Telefone', font=('Arial',20))
    tel_lbl.grid(row=2, column=1, padx=20, pady=2, sticky='w')
    cmp_tel = ctk.CTkEntry(master=frame_campos, placeholder_text="", font=('Arial',20), width=350, height=20, corner_radius=10, border_color="#BFBFBF")
    cmp_tel.pack(pady=(10,10))
    cmp_tel.grid(row=3, column=1, padx=20, pady=2)

    #CAMPO ENDEREÇO
    end_lbl = ctk.CTkLabel(frame_campos, text='Endereço', font=('Arial',20))
    end_lbl.grid(row=4, column=0, padx=20, pady=2, sticky='w')
    cmp_endereco = ctk.CTkEntry(master=frame_campos, placeholder_text="", font=('Arial',20), width=350, height=20, corner_radius=10, border_color="#BFBFBF")
    cmp_endereco.pack(pady=(10,10))
    cmp_endereco.grid(row=5, column=0, padx=20, pady=2)

    #CAMPO CPF
    cpf_lbl = ctk.CTkLabel(frame_campos, text='CPF', font=('Arial',20))
    cpf_lbl.grid(row=4, column=1, padx=20, pady=2, sticky='w')
    cmp_cpf = ctk.CTkEntry(master=frame_campos, placeholder_text="", font=('Arial',20), width=350, height=20, corner_radius=10, border_color="#BFBFBF")
    cmp_cpf.pack(pady=(10,10))
    cmp_cpf.grid(row=5, column=1, padx=20, pady=2)

    #================== BOTÕES ==================
    # FRAMEBOTOES
    frame_btn = ctk.CTkFrame(master=frame_principal, width=400, height=450, fg_color="transparent")
    frame_btn.place(relx=0.5, rely=0.8,anchor='n')

    def salvar(): 
        nome = cmp_nome.get()
        email = cmp_email.get()
        data_nascimento = cmp_dataNascimento.get()
        telefone = cmp_tel.get()
        # opcao_pagamento = opc_pgt.get()
        # valor_pagar = cmp_valor_pagar.get()
        endereco = cmp_endereco.get()
        cpf = cmp_cpf.get()

        if not nome or not cpf or not email or not telefone or not data_nascimento or not endereco:
            messagebox.showwarning("Atenção", "Preencha todos os campos!", parent=janela)
            return
        elif len(nome) < 3:
            messagebox.showwarning("Atenção", "Nome precisa ter no minimo 3 caracteres", parent=janela)
        elif len(cpf) < 11: 
            messagebox.showwarning("Atenção", "CPF precisa ter 11 caracteres", parent=janela)
        elif len(email) < 11: 
            messagebox.showwarning("Atenção", "Email curto demais", parent=janela)
        elif len(telefone) < 8: 
            messagebox.showwarning("Atenção", "Número de telefone está incompleto!", parent=janela)
        elif len(data_nascimento) < 8:
            messagebox.showwarning("Atenção", "Data de nascimento incompleta!", parent=janela)   
        elif len(endereco) < 8:
            messagebox.showwarning("Atenção", "Endereço muito curto!", parent=janela)
        else:
            janela.destroy()
            messagebox.showinfo("INFO", f"O(A) paciente '{nome}' foi cadastrado(a) com sucesso!")
            adicionar_cadastros(nome, cpf, email, telefone, data_nascimento, endereco)

            if atualizar_callback:
                atualizar_callback()

    btn_salvar = ctk.CTkButton(master=frame_btn, text='Salvar', text_color="#000000",width=150,height=40, 
                                corner_radius=20, fg_color= "#00B179" , hover_color= "#016D4B", command=salvar)
    btn_salvar.pack(pady=(10,10), side = 'left', padx = 5)
    
    janela.mainloop()
