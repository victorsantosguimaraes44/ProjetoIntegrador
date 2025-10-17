from tkinter import messagebox
from turtle import left
import customtkinter as ctk

cadastros = []
cadastro = " "
def adicionar_cadastros(nome, email, telefone, endereco, data_nascimento, especialidade):
    cadastro = f"{nome}, {email}, {telefone}, {endereco}, {data_nascimento}, {especialidade}"
    cadastros.append(cadastro)

def obter_cadastros():
    return cadastros

def tela_cadastrar_profissional(JANELA):
    #FRAME PRINCIPAL
    menu_aba = ctk.CTkFrame(master=JANELA, width=1600, height=900, fg_color="transparent", corner_radius=0)
    menu_aba.place(relx=0.5,rely=0.5,anchor="center")
    menu_aba.pack_propagate(False)

    frame_principal = ctk.CTkFrame(master=menu_aba, width=1200, height=750, corner_radius=10)
    frame_principal.place(relx=0.5, rely=0.5,anchor='center')
    frame_principal.pack_propagate(False)

    #TITULO
    titulo = ctk.CTkLabel(master=frame_principal, text="Cadastro de profissional", font=('Arial', 30, 'bold'))
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

    # CAMPO ENDEREÇO
    cmp_end = ctk.CTkEntry(master=frame_campos, placeholder_text="Endereço", font=('Arial',20), width=350, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_end.pack(pady=(10,10))
    cmp_end.grid(row=2, column=0, padx=2, pady=2)


    cmp_esp_titulo = ctk.CTkLabel(master=frame_campos,text="Especialidade: ",font=('Arial',20))
    cmp_esp_titulo.grid(row=3, column=0, padx=0.5, pady=0.5)

    cmp_esp = ctk.CTkComboBox(master=frame_campos, values=["-Selecione-","Fiosiaterapia", "Pilates"],font=('Arial',20), width=150, height=20 )
    cmp_esp.pack(pady=(1,1))
    cmp_esp.grid(row=4, column=0, padx=0.5, pady=0.5)

    #================== BOTÕES ==================
    # FRAMEBOTOES
    frame_btn = ctk.CTkFrame(master=frame_principal, width=400, height=450, fg_color="transparent")
    frame_btn.place(relx=0.5, rely=0.8,anchor='n')

    # BOTAO SALVAR
    def salvar():
        nome = cmp_nome.get()
        email = cmp_email.get()
        data_nascimento = cmp_dataNascimento.get()
        telefone = cmp_tel.get()
        endereco = cmp_end.get()
        especialidade = cmp_esp.get()
        
        if not nome or not email or not data_nascimento or not telefone:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
        elif especialidade == "-Selecione-":
            messagebox.showwarning("Atenção", "Selecione uma especidalidade!")
            return
        else:
            messagebox.showinfo("INFO", f"O(A) Profissional '{nome}', especialidade '{especialidade}', foi cadastrado(a) com sucesso!")
            adicionar_cadastros(nome, email, telefone, data_nascimento, endereco, especialidade)

    btn_salvar = ctk.CTkButton(master=frame_btn, text='Salvar', text_color="#000000",width=150,height=40, 
                                corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049", command=salvar)
    btn_salvar.pack(pady=(10,10), side = 'left', padx = 5)
