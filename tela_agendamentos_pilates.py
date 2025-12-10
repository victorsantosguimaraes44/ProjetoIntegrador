import customtkinter as ctk
from PIL import Image
from tkinter import ttk
from tela_agendar_aula import agendar_aula_pilates
import tkinter.font as tkFont
from tkinter import messagebox
import tela_gerenciador_clínica
from crud_agendamento_pilates import buscar_agendamentos_p
from crud_agendamento_pilates import deletar_agendamento_p

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
    
    ####################### DELETAR AGENDAMENTOS ######################

    def deletar_agend():
        item = tabela.focus()

        if not item:
            messagebox.showwarning("Atenção", "Selecione.")
            return
        
        value = tabela.item(item, 'values')
        id_aula = value[0]

        confirmar = messagebox.askyesno("Confirme", f"Tem certeza que deseja excluir o {id_aula}?")
        if confirmar:
            if deletar_agendamento_p(id_aula):
                messagebox.showinfo('Sucesso', 'Excluido com sucesso!')
                atualizar_tabela()
            else:
                messagebox.showerror('ERRO', 'Falha ao excluir.')

    btn_deletar = ctk.CTkButton(
    frame_top_,
    text="Deletar",
    fg_color="#990000",
    command=lambda: deletar_agend()
    )
    btn_deletar.pack(side="left", padx=10)
            
    ####################### DELETAR AGENDAMENTOS ######################

    style = ttk.Style()
    style.theme_use("default")

    # Fonte para as células
    font_cells = tkFont.Font(family="Arial", size=10)
    style.configure("Custom.Treeview", font=font_cells, rowheight=30)

    # Fonte para o cabeçalho
    font_header = tkFont.Font(family="Arial", size=15, weight="bold")
    style.configure("Custom.Treeview.Heading", font=font_header)

    colunas = ("ID","Nome", "Data", "Hora","Aluno")
    tabela = ttk.Treeview(frame_btn_name, columns=colunas, show="headings", style="Custom.Treeview")

    # Definindo os títulos das colunas
    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.heading("Data", text="Data")
    tabela.heading("Hora", text="Hora")
    tabela.heading("Aluno", text="Aluno")

    # Largura das colunas
    tabela.column("ID", width=25, anchor="center")
    tabela.column("Nome",width=25, anchor="center")
    tabela.column("Data", width=25, anchor="center")
    tabela.column("Hora", width=25, anchor="center")
    tabela.column("Aluno", width=100, anchor="center")

    # Inserindo dados
    agendamentos = buscar_agendamentos_p()

    for agendamento in agendamentos:
        tabela.insert("", "end", values=(
                    agendamento['ID_Aula'],
                    agendamento['Nome_Aula'],
                    agendamento['Data_Aula'],
                    agendamento['Hora_Aula'],
                    agendamento['ID_Aluno']))
    
    tabela.pack(fill="both", expand=True)
    
    def atualizar_tabela():
        agendamentos = buscar_agendamentos_p()

        tabela.delete(*tabela.get_children())  # limpa todas as linhas

        for agendamento in agendamentos:
            tabela.insert("", "end", values=(
                        agendamento['ID_Aula'],
                        agendamento['Nome_Aula'],
                        agendamento['Data_Aula'],
                        agendamento['Hora_Aula'],
                        agendamento['ID_Aluno']))