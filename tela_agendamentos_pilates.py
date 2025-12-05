import customtkinter as ctk
from PIL import Image
from tkinter import ttk
from tela_agendar_aula import obter_agendamentos_pilates
from tela_agendar_aula import agendar_aula_pilates
import tkinter.font as tkFont
import tela_gerenciador_clínica

def tela_agendamentos_pilates(JANELA):

    frame_top_ = ctk.CTkFrame(master=JANELA, width=1550, height=50, corner_radius=2, border_width=2,border_color="#646464")
    frame_top_.pack(side='top')
    frame_top_.pack_propagate(False)
    agendar_img = ctk.CTkImage(Image.open("agendar_img.png"), size=(25, 25))
    btn_agendar = ctk.CTkButton(frame_top_, width=130, height=30, image=agendar_img,text="Agendar", font=('Arial',20),fg_color=("#2E8B57"), 
                                corner_radius=2, command=lambda:agendar_aula_pilates(atualizar_tabela))
    btn_agendar.pack(side='left',padx=10)

    frame = ctk.CTkFrame(master=JANELA, width=1550, height=750, corner_radius=2)
    frame.place(relx=0.5, rely=0.5,anchor='center')
    frame.pack_propagate(False)

    campo_pesquisar = ctk.CTkEntry(master=frame, placeholder_text="Pesquisar", font=('Arial', 15), width=250, height=30, corner_radius=10, border_color="#BFBFBF")
    campo_pesquisar.place(x=10,y=10)

    list_label = ctk.CTkLabel(master=frame,text="Agendamentos", font=('Arial', 25, 'bold'))
    list_label.pack(pady=(10,10))

    frame_btn_name = ctk.CTkScrollableFrame(master=JANELA, width=1530, height=650, corner_radius=0, fg_color="#FFFFFF")
    frame_btn_name.place(relx=0.5, rely=0.5,anchor='center')
    
    ####################### BOTÃO DELETAR AGENDAMENTOS ######################
    btn_deletar = ctk.CTkButton(
    frame_top_,
    text="DELETAR",
    fg_color="#990000",
    command=lambda: atualizar_tabela()
    )
    btn_deletar.pack(side="left", padx=10)
    ####################### BOTÃO DELETAR AGENDAMENTOS ######################

    style = ttk.Style()
    style.theme_use("default")

    # Fonte para as células
    font_cells = tkFont.Font(family="Arial", size=10)
    style.configure("Custom.Treeview", font=font_cells, rowheight=30)

    # Fonte para o cabeçalho
    font_header = tkFont.Font(family="Arial", size=15, weight="bold")
    style.configure("Custom.Treeview.Heading", font=font_header)

    colunas = ("Nome", "Data", "Hora","Paciente")
    tabela = ttk.Treeview(frame_btn_name, columns=colunas, show="headings", style="Custom.Treeview")
    tabela.pack(fill="both", expand=True)

    # Definindo os títulos das colunas
    tabela.heading("Nome", text="Nome")
    tabela.heading("Data", text="Data")
    tabela.heading("Hora", text="Hora")
    tabela.heading("Paciente", text="Paciente")

    # Largura das colunas
    tabela.column("Nome",width=25, anchor="center")
    tabela.column("Data", width=25, anchor="center")
    tabela.column("Hora", width=25, anchor="center")
    tabela.column("Paciente", width=100, anchor="center")


    # Inserindo dados
    dado = []
    for i in range(len(obter_agendamentos_pilates())):
        dado.append((obter_agendamentos_pilates()[i]['nome'], obter_agendamentos_pilates()[i]['data'], obter_agendamentos_pilates()[i]['hora']))

    for item in dado:
        tabela.insert("", "end", values=item)
    
    def atualizar_tabela():
        tabela.delete(*tabela.get_children())  # limpa todas as linhas

        cad = []
        for i in range(len(obter_agendamentos_pilates())):
            cad.append((
                obter_agendamentos_pilates()[i]['nome'],
                obter_agendamentos_pilates()[i]['data'],
                obter_agendamentos_pilates()[i]['hora'],
                # obter_agendamentos_fisio()[i]['telefone']
            ))

        for item in cad:
            tabela.insert("", "end", values=item)