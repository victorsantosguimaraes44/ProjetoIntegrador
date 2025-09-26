import customtkinter as ctk
from tkinter import messagebox
from turtle import left

def tela_cadastrar_aula_pilates(JANELA):
    #FRAME PRINCIPAL
    frame_principal = ctk.CTkFrame(master=JANELA, width=1200, height=750, corner_radius=10, fg_color="transparent")
    frame_principal.place(relx=0.5, rely=0.5,anchor='center')
    frame_principal.pack_propagate(False)

    #TITULO
    titulo = ctk.CTkLabel(master=frame_principal, text="Cadastro de aula", font=('Arial', 25, 'bold'))
    titulo.pack(pady=(10,10))

    #SUBTITULO
    subtitulo = ctk.CTkLabel(master=frame_principal, text="Digite os campos necessários abaixo", font=('Arial', 20, 'bold'))
    subtitulo.pack(pady=(2,10))

    ##================== CAMPOS ==================

    #FRAME CAMPOS
    frame_campos = ctk.CTkFrame(master=JANELA, width=400, height=450 ,corner_radius=5, fg_color="transparent")
    frame_campos.place(relx=0.5, rely=0.5,anchor='s')
    frame_campos.pack_propagate(False)

    # CAMPO NOME DA AULA
    cmp_nome_aula = ctk.CTkEntry(master=frame_campos, placeholder_text="Nome da aula", font=('Arial',20) , width=200, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_nome_aula.pack(pady=(10,10))
    cmp_nome_aula.grid(row=0, column=0, padx=2, pady=2)

    # CAMPO DATA DA AULA
    def foco_mes(event):
        cmp_mes.focus()
    def foco_ano(event):
        cmp_ano.focus()

    frame_campos_data = ctk.CTkFrame(master=frame_campos, width=120, height=40 ,corner_radius=0, fg_color="transparent")
    frame_campos_data.pack(pady=(10,10))
    frame_campos_data.grid(row=2, column=1, padx=2, pady=2)

    text1 = ctk.CTkLabel(master=frame_campos, text="Data da aula: ", font=('Arial',20))
    text1.pack(pady=(10,10))
    text1.grid(row=1, column=1, padx=2, pady=2)

    cmp_dia = ctk.CTkEntry(master=frame_campos_data, placeholder_text="Dia", font=('Arial',20), width=60, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_dia.pack(padx=2, pady=0, side="left")
    cmp_dia.bind("<Return>", foco_mes)

    d_pnt1 = ctk.CTkLabel(master=frame_campos_data, text=":", font=('Arial',20))
    d_pnt1.pack(padx=2, pady=0, side="left")

    cmp_mes = ctk.CTkEntry(master=frame_campos_data, placeholder_text="Mês", font=('Arial',20), width=60, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_mes.pack(padx=2, pady=0, side="left")
    cmp_mes.bind("<Return>", foco_ano)

    d_pnt2 = ctk.CTkLabel(master=frame_campos_data, text=":", font=('Arial',20))
    d_pnt2.pack(padx=2, pady=0, side="left")

    cmp_ano = ctk.CTkEntry(master=frame_campos_data, placeholder_text="Ano", font=('Arial',20), width=80, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_ano.pack(padx=2, pady=0, side="left")

    # CAMPO HORARIO DA AULA
    def foco_proximo(event):
        cmp_min_aula.focus()

    frame_campos_hora = ctk.CTkFrame(master=frame_campos, width=120, height=40 ,corner_radius=0, fg_color="transparent")
    frame_campos_hora.pack(pady=(10,10))
    frame_campos_hora.grid(row=2, column=0, padx=2, pady=2)

    
    text2 = ctk.CTkLabel(master=frame_campos, text="Hora da aula: ", font=('Arial',20))
    text2.pack(pady=(10,10))
    text2.grid(row=1, column=0, padx=2, pady=2)

    cmp_hora_aula = ctk.CTkEntry(master=frame_campos_hora, placeholder_text="HH", font=('Arial',20), width=60, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_hora_aula.pack(padx=2, pady=0, side="left")
    cmp_hora_aula.bind("<Return>", foco_proximo)

    d_pnt = ctk.CTkLabel(master=frame_campos_hora, text=":", font=('Arial',20))
    d_pnt.pack(padx=2, pady=0, side="left")

    cmp_min_aula = ctk.CTkEntry(master=frame_campos_hora, placeholder_text="MM", font=('Arial',20), width=60, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_min_aula.pack(padx=2, pady=0, side="left")
    