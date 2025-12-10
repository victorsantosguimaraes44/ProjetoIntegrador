import customtkinter as ctk
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
from tela_agendar_consultas import agendar_consultas
from crud_agendamentos_fisioterapia import buscar_agendamento_f
from crud_agendamentos_fisioterapia import deletar_agendamento_f

def tela_agendamentos_fisio(JANELA):

    frame_top_ = ctk.CTkFrame(master=JANELA, width=1550, height=50, corner_radius=2, border_width=2,border_color="#646464")
    frame_top_.pack(side='top')
    frame_top_.pack_propagate(False)

    agendar_img = ctk.CTkImage(Image.open("agendar_img.png"), size=(25, 25))
    btn_agendar = ctk.CTkButton(frame_top_, width=130, height=30, image=agendar_img,text="Agendar", font=('Arial',20),fg_color=("#2E8B57"), 
                                corner_radius=2, command=lambda:agendar_consultas(atualizar_tabela))
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
    command=lambda: deletar_agend()
    )
    btn_deletar.pack(side="left", padx=10)

    def deletar_agend():
        item = tabela.focus()

        if not item:
            messagebox.showwarning("Atenção", "Selecione.")
            return
        
        value = tabela.item(item, 'values')
        id_consulta = value[0]

        confirmar = messagebox.askyesno("Confirme", f"Tem certeza que deseja excluir o {id_consulta}?")
        if confirmar:
            if deletar_agendamento_f(id_consulta):
                messagebox.showinfo('Sucesso', 'Excluido com sucesso!')
                atualizar_tabela()
            else:
                messagebox.showerror('ERRO', 'Falha ao excluir.')
    ####################### BOTÃO DELETAR AGENDAMENTOS ######################

    style = ttk.Style()
    style.theme_use("default")

    # Fonte para as células
    font_cells = tkFont.Font(family="Arial", size=10)
    style.configure("Custom.Treeview", font=font_cells, rowheight=30)

    # Fonte para o cabeçalho
    font_header = tkFont.Font(family="Arial", size=15, weight="bold")
    style.configure("Custom.Treeview.Heading", font=font_header)

    colunas = ("ID", "Nome", "Data", "Hora","Paciente")
    tabela = ttk.Treeview(frame_btn_name, columns=colunas, show="headings", style="Custom.Treeview")
    tabela.pack(fill="both", expand=True)

    # Definindo os títulos das colunas
    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.heading("Data", text="Data")
    tabela.heading("Hora", text="Hora")
    tabela.heading("Paciente", text="Paciente")

    # Largura das colunas
    tabela.column("ID",width=25, anchor="center")
    tabela.column("Nome",width=25, anchor="center")
    tabela.column("Data", width=25, anchor="center")
    tabela.column("Hora", width=25, anchor="center")
    tabela.column("Paciente", width=100, anchor="center")

    agendamentos = buscar_agendamento_f()

    for agendamento in agendamentos:
        tabela.insert('','end', values=(
            agendamento['ID_Consulta'], 
            agendamento['Nome_Consulta'],
            agendamento['Data_Consulta'],
            agendamento['Hora_Consulta'],
            agendamento['ID_Paciente']
        ))

    def atualizar_tabela():
        tabela.delete(*tabela.get_children())

        agendamentos = buscar_agendamento_f()

        for agendamento in agendamentos:
            tabela.insert('','end', values=(
                agendamento['ID_Consulta'], 
                agendamento['Nome_Consulta'],
                agendamento['Data_Consulta'],
                agendamento['Hora_Consulta']
            ))




    
