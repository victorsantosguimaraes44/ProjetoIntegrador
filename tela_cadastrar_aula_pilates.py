import customtkinter as ctk
from tkinter import messagebox
from turtle import left
from tela_lista_alunos_pilates import tela_lista_alunos_pilates

agendamentos = []
agendamento = " "
def adicionar_agendamentos(Nome_aula, Data_aula, Hora_aula):
    agendamento = f"Nome da aula: {Nome_aula}, Data da aula: {Data_aula}, Hora da aula: {Hora_aula}"

    from tela_gerenciador_clínica import agendamentos_totais
    agendamentos_totais(agendamento)
    agendamentos.append(agendamento)

def obter_agendamentos_pilates():
    return agendamentos

def tela_cadastrar_aula_pilates(JANELA):
    #FRAME PRINCIPAL
    frame_principal = ctk.CTkFrame(master=JANELA, width=1200, height=750, corner_radius=10)
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
    frame_campos = ctk.CTkFrame(master=JANELA, width=400, height=450 ,corner_radius=5, fg_color="#C8C8C8")
    frame_campos.place(relx=0.5, rely=0.5,anchor='s')
    frame_campos.pack_propagate(False)

    # CAMPO NOME DA AULA
    cmp_nome_aula = ctk.CTkEntry(master=frame_campos, placeholder_text="Nome da aula", font=('Arial',20) , width=200, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_nome_aula.pack(pady=(10,10))
    cmp_nome_aula.grid(row=0, column=0, padx=2, pady=2)

    # CAMPO NOME DA AULA
    cmp_sala = ctk.CTkEntry(master=frame_campos, placeholder_text="Sala", font=('Arial',20) , width=100, height=40, corner_radius=10, border_color="#BFBFBF")
    cmp_sala.pack(pady=(10,10))
    cmp_sala.grid(row=0, column=1, padx=2, pady=2)

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

    frame_btn = ctk.CTkFrame(master=frame_principal, width=400, height=450, fg_color="transparent")
    frame_btn.place(relx=0.5, rely=0.8,anchor='n')

    # ESCOLHA DO ALUNO
    
    # def escolher_aluno():
    #     frame_cmp_aluno = ctk.CTkFrame(master=frame_principal, width=300, height=40 ,corner_radius=0, fg_color="transparent")
    #     frame_cmp_aluno.grid(row=4, column=0, columnspan=2, padx=2, pady=2)
    #     tela_lista_alunos_pilates(frame_cmp_aluno)
        
    # btn_escolher_aluno = ctk.CTkButton(master=frame_campos, text='Escolher aluno', text_color="#000000",width=150,height=40, 
    #                                    corner_radius=0, fg_color= "#BABABA" , hover_color= "#4b4b4b", 
    #                                    border_width=2, border_color="#5A5A5A", command=escolher_aluno)
    # btn_escolher_aluno.grid(row=3, column=1, padx=2, pady=2)


    def salvar_aula():
        nome_aula = cmp_nome_aula.get()
        dia = cmp_dia.get()
        mes = cmp_mes.get()
        ano = cmp_ano.get()
        hora = cmp_hora_aula.get()
        minuto = cmp_min_aula.get()

        data = f"{dia}/{mes}/{ano}"
        hora_aula = f"{hora}:{minuto}"

        if not nome_aula or not dia or not mes or not ano or not hora or not minuto:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return
        else:
            messagebox.showinfo("Sucesso", "Agendamento realizado com sucesso!")
            adicionar_agendamentos(nome_aula, data, hora_aula)
        
    btn_salvar = ctk.CTkButton(master=frame_btn, text='Salvar', text_color="#000000",width=150,height=40, 
                                corner_radius=20, fg_color= "#00B179" , hover_color= "#007651", command=salvar_aula)
    btn_salvar.pack(pady=(10,10))
    