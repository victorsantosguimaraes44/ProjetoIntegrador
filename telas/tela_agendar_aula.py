import customtkinter as ctk
from tkinter import messagebox, ttk
import tkinter.font as tkFont
from turtle import left
from database.crud_agendamento_pilates import inserir_agendamento_p
from database.crud_alunos import buscar_alunos
def agendar_aula_pilates(atualizar_callback=None):

    ctk.set_appearance_mode('light')
    ctk.set_default_color_theme('blue')

    janela = ctk.CTk()
    janela.geometry("500x500")
    janela.resizable(False, False)
    janela.title('Fisioterapia - Agendar')
    janela.attributes("-topmost", True)

    #FRAME PRINCIPAL
    frame_principal = ctk.CTkFrame(master=janela, width=500, height=500, corner_radius=10)
    frame_principal.place(relx=0.5, rely=0.5,anchor='center')
    frame_principal.pack_propagate(False)

    #TITULO
    titulo = ctk.CTkLabel(master=frame_principal, text="Agendar aula", font=('Arial', 25, 'bold'))
    titulo.pack(pady=(10,10))

    #SUBTITULO
    subtitulo = ctk.CTkLabel(master=frame_principal, text="Digite os campos necessários abaixo", font=('Arial', 20, 'bold'))
    subtitulo.pack(pady=(2,10))

    ##================== CAMPOS ==================

    #FRAME CAMPOS
    frame_campos = ctk.CTkFrame(master=janela, width=400, height=450 ,corner_radius=5, fg_color="#C8C8C8")
    frame_campos.place(relx=0.5, rely=0.5,anchor='center')
    frame_campos.pack_propagate(False)

    # CAMPO NOME DA AULA
    aula_lbl = ctk.CTkLabel(master=frame_campos, text='Aula',font=('Arial',20))
    aula_lbl.grid(row=0,column=0,padx=2,pady=2)
    cmp_nome_aula = ctk.CTkEntry(master=frame_campos, placeholder_text="", font=('Arial',20) , width=200, height=20, corner_radius=1, border_color="#BFBFBF")
    cmp_nome_aula.pack(pady=(10,10))
    cmp_nome_aula.grid(row=1, column=0, padx=2, pady=2)

    # CAMPO DATA DA AULA
    def foco_mes(event):
        cmp_mes.focus()
    def foco_ano(event):
        cmp_ano.focus()

    
    text1 = ctk.CTkLabel(master=frame_campos, text="Data", font=('Arial',20))
    text1.pack(pady=(10,10))
    text1.grid(row=3, column=1, padx=2, pady=2)

    frame_campos_data = ctk.CTkFrame(master=frame_campos, width=120, height=40 ,corner_radius=0, fg_color="transparent")
    frame_campos_data.pack(pady=(10,10))
    frame_campos_data.grid(row=4, column=1, padx=2, pady=2)

    cmp_dia = ctk.CTkEntry(master=frame_campos_data, placeholder_text="Dia", font=('Arial',20), width=60, height=20, corner_radius=1, border_color="#BFBFBF")
    cmp_dia.pack(padx=2, pady=0, side="left")
    cmp_dia.bind("<Return>", foco_mes)

    d_pnt1 = ctk.CTkLabel(master=frame_campos_data, text=":", font=('Arial',20))
    d_pnt1.pack(padx=2, pady=0, side="left")

    cmp_mes = ctk.CTkEntry(master=frame_campos_data, placeholder_text="Mês", font=('Arial',20), width=60, height=20, corner_radius=1, border_color="#BFBFBF")
    cmp_mes.pack(padx=2, pady=0, side="left")
    cmp_mes.bind("<Return>", foco_ano)

    d_pnt2 = ctk.CTkLabel(master=frame_campos_data, text=":", font=('Arial',20))
    d_pnt2.pack(padx=2, pady=0, side="left")

    cmp_ano = ctk.CTkEntry(master=frame_campos_data, placeholder_text="Ano", font=('Arial',20), width=80, height=20, corner_radius=1, border_color="#BFBFBF")
    cmp_ano.pack(padx=2, pady=0, side="left")

    # CAMPO HORARIO DA AULA
    def foco_proximo(event):
        cmp_min_aula.focus()

    
    text2 = ctk.CTkLabel(master=frame_campos, text="Hora", font=('Arial',20))
    text2.pack(pady=(10,10))
    text2.grid(row=3, column=0, padx=2, pady=2)

    frame_campos_hora = ctk.CTkFrame(master=frame_campos, width=120, height=40 ,corner_radius=0, fg_color="transparent")
    frame_campos_hora.pack(pady=(10,10))
    frame_campos_hora.grid(row=4, column=0, padx=2, pady=2)

    cmp_hora_aula = ctk.CTkEntry(master=frame_campos_hora, placeholder_text="HH", font=('Arial',20), width=50, height=20, corner_radius=1, border_color="#BFBFBF")
    cmp_hora_aula.pack(padx=2, pady=0, side="left")
    cmp_hora_aula.bind("<Return>", foco_proximo)

    d_pnt = ctk.CTkLabel(master=frame_campos_hora, text=":", font=('Arial',20))
    d_pnt.pack(padx=2, pady=0, side="left")

    cmp_min_aula = ctk.CTkEntry(master=frame_campos_hora, placeholder_text="MM", font=('Arial',20), width=50, height=20, corner_radius=1, border_color="#BFBFBF")
    cmp_min_aula.pack(padx=2, pady=0, side="left")
    
    aluno_var = ctk.StringVar()
    btn_esc_pac = ctk.CTkButton(master=frame_campos, text='Escolher \nAluno', font=('Arial',20), fg_color='#4CAF50', hover_color= "#45a049"
                                ,width=130, height=40, corner_radius=1, command=lambda:escolher_aluno(aluno_var))
    btn_esc_pac.grid(row=5,column=0,padx=2, pady=10)
    esc_pac_lbl = ctk.CTkEntry(
    master=frame_campos,
    textvariable=aluno_var,
    font=('Arial',10),
    width=150,
    state="readonly"
)
    esc_pac_lbl.grid(row=5,column=1,padx=2, pady=10)

    frame_btn = ctk.CTkFrame(master=frame_principal, width=400, height=450, fg_color="transparent")
    frame_btn.place(relx=0.5, rely=0.8,anchor='n')

    def salvar_aula():
        nome_aula = cmp_nome_aula.get()
        dia = cmp_dia.get()
        mes = cmp_mes.get()
        ano = cmp_ano.get()
        hora = cmp_hora_aula.get()
        minuto = cmp_min_aula.get()

        data_aula = f"{dia}/{mes}/{ano}"
        hora_aula = f"{hora}:{minuto}"
        id_aluno = int(esc_pac_lbl.get())

        if not nome_aula or not dia or not mes or not ano or not hora or not minuto:
            messagebox.showwarning("Atenção", "Preencha todos os campos!", parent=janela)
            return
        else:
            janela.destroy()
            messagebox.showinfo("Sucesso", "Agendamento realizado com sucesso!")
            inserir_agendamento_p(data_aula, hora_aula, id_aluno, nome_aula)

            if atualizar_callback:
                atualizar_callback()
        
    btn_salvar = ctk.CTkButton(master=frame_btn, text='Salvar', text_color="#000000",width=150,height=40, 
                                corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049", command=salvar_aula)
    btn_salvar.pack(pady=(10,10))

    janela.mainloop()

def escolher_aluno(aluno_var):
    # Criar janela modal em relação à principal
    jan = ctk.CTkToplevel()
    jan.geometry("800x800")
    jan.resizable(False, False)
    jan.title('Escolher aluno')
    jan.attributes("-topmost", True)
    jan.grab_set()  # Bloqueia interação com a janela principal

    # FRAME topo para pesquisar
    frame_top = ctk.CTkFrame(jan, width=800, height=50, corner_radius=0)
    frame_top.pack(side="top", padx=5, pady=5)
    frame_top.pack_propagate(False)

    campo_pesquisar = ctk.CTkEntry(frame_top, placeholder_text="Pesquisar 🔍", width=300, height=40)
    campo_pesquisar.pack(padx=5, pady=5, side='left')

    # FRAME scrollable para Treeview
    frame_btn_name = ctk.CTkScrollableFrame(master=jan, width=750, height=750, corner_radius=0, fg_color="#FFFFFF")
    frame_btn_name.pack(padx=5, pady=5)

    # Configura estilo da Treeview
    style = ttk.Style()
    style.configure("Aluno.Treeview", font=("Arial", 15), rowheight=45)
    style.configure("Aluno.Treeview.Heading", font=("Arial", 18, "bold"))

    tabela = ttk.Treeview(frame_btn_name, columns=("ID","Nome"), show="headings", style="Aluno.Treeview")
    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.column("ID", width=50, anchor="center")
    tabela.column("Nome", width=200, anchor="w")

    # Preencher Treeview
    cad = buscar_alunos()
    for aluno in cad:
        tabela.insert("", "end", values=(aluno["ID_Aluno"], aluno["Nome_Aluno"]))

    tabela.pack(fill="both", expand=True)

    # Evento de clique duplo
    def on_row_click(event):
        selected_item = tabela.focus()
        if not selected_item:
            return

        values = tabela.item(selected_item, "values")
        if values:
            aluno_var.set(values[1])  # Atualiza StringVar do Entry
            # destrói a janela **depois do evento**
            jan.after(1, jan.destroy)

    tabela.bind("<Double-1>", on_row_click)

    jan.mainloop()