import customtkinter as ctk
from PIL import Image
from tela_cadastro_usuario_pilates import obter_cadastros
from tela_cadastro_usuario_pilates import abrir_cadastro_pilates
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
import mysql.connector 


#=================
#Conexão com o banco de dados MySQL
#=================

def conectar_banco(): 
    return mysql.connector.connect(
            host = "localhost" , 
            user = "root" , 
            password = "" , 
            database = "clinica_retratafisio"
    )

def tela_lista_alunos_pilates(JANELA):
    
    frame_top = ctk.CTkFrame(master=JANELA, width=1550, height=40, corner_radius=2, border_width=2,border_color="#646464")
    frame_top.pack(side='top')
    frame_top.pack_propagate(False)
    
    add_user_img = ctk.CTkImage(Image.open("add-user.png"), size=(25, 25))
    
    btn_cadastrar = ctk.CTkButton(frame_top, width=130, height=30, image=add_user_img,text="Cadastrar", font=('Arial',20),fg_color=("#2E8B57"), 
                                  corner_radius=2, command=lambda: abrir_cadastro_pilates(atualizar_tabela))
    btn_cadastrar.pack(side='left',padx=10)

    frame = ctk.CTkFrame(master=JANELA, width=1550, height=750, corner_radius=2)
    frame.place(relx=0.5, rely=0.5,anchor='center')
    frame.pack_propagate(False)

    campo_pesquisar = ctk.CTkEntry(master=frame, placeholder_text="Pesquisar", font=('Arial', 15), width=250, height=30, corner_radius=10, border_color="#BFBFBF")
    campo_pesquisar.place(x=10,y=10)

    list_label = ctk.CTkLabel(master=frame,text="Alunos", font=('Arial', 25, 'bold'))
    list_label.pack(pady=(10,10))
    
    frame_btn_name = ctk.CTkScrollableFrame(master=JANELA, width=1530, height=650, corner_radius=0, fg_color="#FFFFFF")
    frame_btn_name.place(relx=0.5, rely=0.5,anchor='center')

    style = ttk.Style()
    style.theme_use("default")

    # Fonte para as células
    font_cells = tkFont.Font(family="Arial", size=10)
    style.configure("Custom.Treeview", font=font_cells, rowheight=30)

    # Fonte para o cabeçalho
    font_header = tkFont.Font(family="Arial", size=15, weight="bold")
    style.configure("Custom.Treeview.Heading", font=font_header)

    tabela_paciente = ttk.Treeview(frame_btn_name, columns=("Nome",'Data_nascimento' ,"CPF", "Endereço","Telefone","Email"), show="headings", style="Custom.Treeview")
    tabela_paciente.pack(fill="both", expand=True)
    # Definindo os títulos das colunas
    tabela_paciente.heading("Nome", text="Nome")
    tabela_paciente.heading("Data_nascimento", text="Data de nascimento")
    tabela_paciente.heading("CPF", text="CPF")
    tabela_paciente.heading("Endereço", text="Endereço")
    tabela_paciente.heading("Telefone", text="Telefone")
    tabela_paciente.heading("Email", text="Email")

    # Largura das colunas
    tabela_paciente.column("Nome", width=25, anchor="center")
    tabela_paciente.column("Data_nascimento", width=25, anchor="center")
    tabela_paciente.column("CPF", width=25, anchor="center")
    tabela_paciente.column("Endereço",width=25, anchor="center")
    tabela_paciente.column("Telefone", width=100, anchor="center")
    tabela_paciente.column("Email", width=100, anchor="center" )

    # Inserindo dados
    cad = []
    for i in range(len(obter_cadastros())):
        cad.append((obter_cadastros()[i]['nome'], obter_cadastros()[i]['cpf'], obter_cadastros()[i]['data_nascimento'], obter_cadastros()[i]['endereco'], obter_cadastros()[i]['telefone'], obter_cadastros()[i]['email']))

    for item in cad:
        tabela_paciente.insert("", "end", values=item)

    tabela_paciente.pack(fill="both", expand=True)

        # --- Vincula o clique simples ---

    def on_row_click(event):
        # Verifica o item selecionado
        selected_item = tabela_paciente.focus()
        if not selected_item:
            return

        # Obtém os dados da linha
        values = tabela_paciente.item(selected_item, "values")
        if values:
            nome = values[0]
            informacoes(nome)
    
    tabela_paciente.bind("<Double-1>", on_row_click)
    def atualizar_tabela():
        tabela_paciente.delete(*tabela_paciente.get_children())  # limpa todas as linhas

        cad = []
        for i in range(len(obter_cadastros())):
            cad.append((
                obter_cadastros()[i]['nome'],
                obter_cadastros()[i]['cpf'],
                obter_cadastros()[i]['data_nascimento'],
                obter_cadastros()[i]['endereco'],
                obter_cadastros()[i]['telefone'],
                obter_cadastros()[i]['email']
            ))

        for item in cad:
            tabela_paciente.insert("", "end", values=item)

    def informacoes(nome):
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')

        janela = ctk.CTk()
        janela.geometry("500x500")
        janela.resizable(False, False)
        janela.title('INFO')

        frame = ctk.CTkFrame(master=janela, width=500, height=500)
        frame.place(relx=0.5, rely=0.5, anchor='center')
        frame.pack_propagate(False)

        for cadastro in obter_cadastros():
            if cadastro["nome"] == nome:
                email = cadastro['email']
                cpf = cadastro['cpf']
                data_nascimento = cadastro['data_nascimento']
                telefone = cadastro['telefone']
                endereco = cadastro['endereco']
                break

        ctk.CTkLabel(frame, text="Nome:", font=('Arial',19)).pack(padx=2)
        cmp_nome = ctk.CTkEntry(frame, placeholder_text="", font=('Arial', 15), width=300, height=20)
        cmp_nome.pack(pady=5)
        cmp_nome.insert(0,nome)

        ctk.CTkLabel(frame, text="CPF:", font=('Arial',19)).pack(padx=2)
        cmp_cpf = ctk.CTkEntry(frame, placeholder_text="", font=('Arial', 15), width=300, height=20)
        cmp_cpf.pack(pady=5)
        cmp_cpf.insert(0,cpf)

        ctk.CTkLabel(frame, text="Data de nascimento:", font=('Arial',19)).pack(padx=2)
        cmp_dtns = ctk.CTkEntry(frame, placeholder_text="", font=('Arial', 15), width=200, height=20)
        cmp_dtns.pack(pady=5)
        cmp_dtns.insert(0,data_nascimento)

        ctk.CTkLabel(frame, text="Email:", font=('Arial',19)).pack(padx=2)
        cmp_email = ctk.CTkEntry(frame, placeholder_text="", font=('Arial', 15), width=300, height=20)
        cmp_email.pack(pady=5)
        cmp_email.insert(0,email)

        ctk.CTkLabel(frame, text="Telefone:", font=('Arial',19)).pack(padx=2)
        cmp_telefone = ctk.CTkEntry(frame, placeholder_text="", font=('Arial', 15), width=300, height=20)
        cmp_telefone.pack(pady=5)
        cmp_telefone.insert(0,telefone)

        ctk.CTkLabel(frame, text="Endereço:", font=('Arial',19)).pack(padx=2)
        cmp_endereco = ctk.CTkEntry(frame, placeholder_text="", font=('Arial', 15), width=300, height=20)
        cmp_endereco.pack(pady=5)
        cmp_endereco.insert(0,endereco)

        def atualizar():
            nome_atualizado = cmp_nome.get()
            cpf_atualizado = cmp_cpf.get()
            dtns_atualizado = cmp_dtns.get()
            email_atualizado = cmp_email.get()
            tel_atualizado = cmp_telefone.get()
            endereco_atualizado = cmp_endereco.get()

            for cadastro in obter_cadastros():
                if not nome_atualizado or not cpf_atualizado or not dtns_atualizado or not email_atualizado or not tel_atualizado or not endereco_atualizado:
                    messagebox.showwarning('Atenção','Preencha todos os campos!')
                else:
                    if cadastro["nome"] == nome:
                        cadastro["nome"] = nome_atualizado
                        cadastro['email'] = email_atualizado
                        cadastro['cpf'] = cpf_atualizado
                        cadastro['data_nascimento'] = dtns_atualizado
                        cadastro['telefone'] = tel_atualizado
                        cadastro['endereco'] = endereco_atualizado
                        messagebox.showinfo('Sucesso','Perfil atualizado com sucesso!')
                        atualizar_tabela()
                        janela.destroy()
                        break
        def cancelar():
            janela.destroy()                    
        btn_atualizar = ctk.CTkButton(frame, text="Atualizar", font=('Arial',15),text_color="#FFFFFF", 
                                    width=100, height=25, fg_color="#059200", command=atualizar)
        btn_atualizar.pack(pady=5)

        btn_cancelar = ctk.CTkButton(frame, text="Cancelar", font=('Arial',15),text_color="#FFFFFF", 
                                    width=100, height=25, fg_color="#920000", command=cancelar)
        btn_cancelar.pack(pady=5)

        janela.mainloop()