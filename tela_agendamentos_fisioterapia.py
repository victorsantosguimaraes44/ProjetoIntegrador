import customtkinter as ctk
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
from tela_agendar_consultas import agendar_consultas
from crud_agendamentos_fisioterapia import buscar_agendamento_f, deletar_agendamento_f, atualizar_agendamento

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
    trash_img = ctk.CTkImage(Image.open("trash.png"), size=(25, 25))
    btn_deletar = ctk.CTkButton(
    frame_top_,
    width=130, height=30,
    corner_radius=2,
    text="Deletar",
    font=('Arial',20),image=trash_img,
    fg_color="#FF0000",
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

    def on_row_click(event):
        # Verifica o item selecionado
        selected_item = tabela.focus()
        if not selected_item:
            return

        # Obtém os dados da linha
        values = tabela.item(selected_item, "values")
        if values:
            id = int(values[0])
            informacoes(id)
    
    tabela.bind("<Double-1>", on_row_click)

    def informacoes(ID):
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')

        janela = ctk.CTk()
        janela.geometry("500x500")
        janela.resizable(False, False)
        janela.title('INFO')

        frame = ctk.CTkFrame(master=janela, width=500, height=500)
        frame.place(relx=0.5, rely=0.5, anchor='center')
        frame.pack_propagate(False)

        Nome_consulta = Data_consulta = Hora_consulta = None

        for agendamento in agendamentos:
           if agendamento["ID_Consulta"] == ID:
                Nome_consulta = agendamento['Nome_Consulta'],
                Data_consulta = agendamento['Data_Consulta'],
                Hora_consulta = agendamento['Hora_Consulta']

        ctk.CTkLabel(frame, text="Consulta:", font=('Arial',19)).pack(padx=2)
        cmp_nome = ctk.CTkEntry(frame, placeholder_text="", font=('Arial', 15), width=300, height=20)
        cmp_nome.pack(pady=5)
        cmp_nome.insert(0,Nome_consulta)

        ctk.CTkLabel(frame, text="Data:", font=('Arial',19)).pack(padx=2)
        cmp_data = ctk.CTkEntry(frame, placeholder_text="", font=('Arial', 15), width=300, height=20)
        cmp_data.pack(pady=5)
        cmp_data.insert(0,Data_consulta)

        ctk.CTkLabel(frame, text="Hora:", font=('Arial',19)).pack(padx=2)
        cmp_hora = ctk.CTkEntry(frame, placeholder_text="", font=('Arial', 15), width=200, height=20)
        cmp_hora.pack(pady=5)
        cmp_hora.insert(0,Hora_consulta)

        def atualizar():
            nome_atualizado = cmp_nome.get()
            data_atualizado = cmp_data.get()
            hora_atualizado = cmp_hora.get()

            for agendamento in agendamentos:
                if not nome_atualizado or not data_atualizado or not hora_atualizado:
                    messagebox.showwarning('Atenção','Preencha todos os campos!')
                else:
                    for agendamento in agendamentos:
                        if agendamento["ID_Consulta"] == ID:
                                agendamento['Nome_Consulta'] = nome_atualizado,
                                agendamento['Data_Consulta'] = data_atualizado,
                                agendamento['Hora_Consulta'] = hora_atualizado

                        atualizar_agendamento(ID,nome_atualizado,data_atualizado,hora_atualizado)

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

        janela.mainloop()   

        




    
