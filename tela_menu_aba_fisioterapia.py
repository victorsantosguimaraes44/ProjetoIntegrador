import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from tkinter import ttk
from tela_cadastro_usuario_fisioterapia import abrir_cadastro_fisioterapia
from tela_cadastro_usuario_fisioterapia import obter_cadastros
from tela_lista_pacientes_fisioterapia import tela_lista_pacientes_fisio
from tela_agendar_consultas import agendar_consultas
from tela_agendamentos_fisioterapia import tela_agendamentos_fisio
from tela_agendar_consultas import obter_agendamentos_fisio


def abrir_menu_aba_fisioterapia(JANELA):
    # === CONFIGURAÇÃO INICIAL ===

    menu_aba = ctk.CTkFrame(master=JANELA, width=1600, height=850, fg_color="transparent")
    menu_aba.place(relx=0.5,rely=0.5,anchor='center')

    fisio_lbl = ctk.CTkLabel(menu_aba, text="Fisioterapia",font=('Arial',20))
    fisio_lbl.pack(side='top')

    tabview = ctk.CTkTabview(master=menu_aba, width=1600, height=850, segmented_button_fg_color="#00B179",
                             segmented_button_selected_color="#005B3E",
                             segmented_button_unselected_color="#00B179",segmented_button_unselected_hover_color="#00B179")
    tabview.pack(padx=5)

    tabview.add('Geral')
    tabview.add('Cadastro')
    tabview.add('Agendar')

    tabview._segmented_button.configure(
    height=35,   # altura
    width=150,   # largura de cada aba
    corner_radius=2)

    tabview._segmented_button.configure(font=ctk.CTkFont(size=18))  
    #=========
    #  GERAL
    #=========

    frame_tb_f = ctk.CTkFrame(master=tabview.tab('Geral'), width=787, height=850, fg_color="#FFFFFF")
    frame_tb_f.place(relx=0.5,rely=0.55,anchor='e')
    frame_tb_f.pack_propagate(False)

    campo_pesquisar = ctk.CTkEntry(master=frame_tb_f, placeholder_text="Pesquisar", font=('Arial', 15), width=250, height=30, corner_radius=10, border_color="#BFBFBF")
    campo_pesquisar.place(x=10,y=10)

    list_label = ctk.CTkLabel(master=frame_tb_f,text="Agendamentos", font=('Arial', 25, 'bold'))
    list_label.pack(pady=(10,10))

    frame_btn_name = ctk.CTkScrollableFrame(master=frame_tb_f, width=750, height=650, corner_radius=0, fg_color="#FFFFFF")
    frame_btn_name.pack(pady=(10,10))
    tabela_agendamento = ttk.Treeview(frame_btn_name, columns=("Nome", "Data", "Hora","Paciente"), show="headings")

    tabela_agendamento.heading("Nome", text="Nome")
    tabela_agendamento.heading("Data", text="Data")
    tabela_agendamento.heading("Hora", text="Hora")
    tabela_agendamento.heading("Paciente", text="Paciente")

    tabela_agendamento.column("Nome",width=25, anchor="center")
    tabela_agendamento.column("Data", width=25, anchor="center")
    tabela_agendamento.column("Hora", width=25, anchor="center")
    tabela_agendamento.column("Paciente", width=100, anchor="center")

    # Inserindo dados
    dado = []
    for i in range(len(obter_agendamentos_fisio())):
        dado.append((obter_agendamentos_fisio()[i]['nome'], obter_agendamentos_fisio()[i]['data'], obter_agendamentos_fisio()[i]['hora']))

    for item in dado:
        tabela_agendamento.insert("", "end", values=item)

    tabela_agendamento.pack(fill="both", expand=True)

    
    #==========================================================================================================================
    frame_tb_p= ctk.CTkFrame(master=tabview.tab('Geral'), width=787, height=850, fg_color="#FFFFFF")
    frame_tb_p.place(relx=0.5,rely=0.55,anchor='w')
    frame_tb_p.pack_propagate(False)

    list_pac = ctk.CTkLabel(master=frame_tb_p,text="Pacientes", font=('Arial', 25, 'bold'))
    list_pac.pack(pady=(10,10))

    campo_pesquisar = ctk.CTkEntry(master=frame_tb_p, placeholder_text="Pesquisar", font=('Arial', 15), width=250, height=30, corner_radius=10, border_color="#BFBFBF")
    campo_pesquisar.place(x=10,y=10)

    frame_tb_name = ctk.CTkScrollableFrame(master=frame_tb_p, width=750, height=650, corner_radius=0, fg_color="#FFFFFF")
    frame_tb_name.pack(pady=(10,10))

    tabela_paciente = ttk.Treeview(frame_tb_name, columns=("Nome", "CPF", "Endereço","Telefone"), show="headings")
    tabela_paciente.pack(fill="both", expand=True)


    # Definindo os títulos das colunas
    tabela_paciente.heading("Nome", text="Nome")
    tabela_paciente.heading("CPF", text="CPF")
    tabela_paciente.heading("Endereço", text="Endereço")
    tabela_paciente.heading("Telefone", text="Telefone")

    # Largura das colunas
    tabela_paciente.column("Nome", width=25, anchor="center")
    tabela_paciente.column("CPF", width=25, anchor="center")
    tabela_paciente.column("Endereço",width=25, anchor="center")
    tabela_paciente.column("Telefone", width=100, anchor="center")

    # Inserindo dados
    cad = []
    for i in range(len(obter_cadastros())):
        cad.append((obter_cadastros()[i]['nome'], obter_cadastros()[i]['cpf'], obter_cadastros()[i]['endereco'], obter_cadastros()[i]['telefone']))

    for item in cad:
        tabela_paciente.insert("", "end", values=item)

    tabela_paciente.pack(fill="both", expand=True)
    #============
    # CADASTRAR
    #============
    
    frame_tl_ls_p_f = ctk.CTkFrame(master=tabview.tab('Cadastro'), width=1550, height=850, fg_color="transparent")
    frame_tl_ls_p_f.place(relx=0.5,rely=0.55,anchor='center')
    frame_tl_ls_p_f.pack_propagate(False)
    tela_lista_pacientes_fisio(frame_tl_ls_p_f)

    #================
    #  AGENDAMENTOS
    #================
    frame_tl_ag_f= ctk.CTkFrame(master=tabview.tab('Agendar'), width=1550, height=850, fg_color="transparent")
    frame_tl_ag_f.place(relx=0.5,rely=0.55,anchor='center')
    frame_tl_ag_f.pack_propagate(False)
    tela_agendamentos_fisio(frame_tl_ag_f)

    return menu_aba








