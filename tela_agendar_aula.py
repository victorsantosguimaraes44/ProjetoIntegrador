import customtkinter as ctk
from tkinter import messagebox
from turtle import left
from tela_lista_alunos_pilates import tela_lista_alunos_pilates

agendamentos = []
agendamento = " "
DADOS_CONSULTA = {}

def adicionar_agendamentos(nome_consulta, data_consulta, hora_consulta, Nome_paciente):
    agendamento = f"consulta: {nome_consulta}, Data da consulta: {data_consulta}, Hora da consulta: {hora_consulta},paciente:{Nome_paciente}"
    DADOS_CONSULTA = {"nome":nome_consulta, 'data':data_consulta,"hora":hora_consulta,"paciente":Nome_paciente}
    from tela_gerenciador_clínica import agendamentos_totais
    agendamentos_totais(agendamento)
    agendamentos.append(DADOS_CONSULTA)

def obter_agendamentos_pilates():
    return agendamentos

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
    aula_lbl = ctk.CTkLabel(master=frame_campos, text='Consulta',font=('Arial',20))
    aula_lbl.grid(row=0,column=0,padx=2,pady=2)
    cmp_nome_aula = ctk.CTkEntry(master=frame_campos, placeholder_text="", font=('Arial',20) , width=200, height=20, corner_radius=1, border_color="#BFBFBF")
    cmp_nome_aula.pack(pady=(10,10))
    cmp_nome_aula.grid(row=1, column=0, padx=2, pady=2)

    # CAMPO NOME DA AULA
    sala_lbl = ctk.CTkLabel(master=frame_campos, text='Sala',font=('Arial',20))
    sala_lbl.grid(row=0,column=1,padx=2,pady=2)
    cmp_sala = ctk.CTkEntry(master=frame_campos, placeholder_text="", font=('Arial',20) , width=100, height=20, corner_radius=1, border_color="#BFBFBF")
    cmp_sala.pack(pady=(10,10))
    cmp_sala.grid(row=1, column=1, padx=2, pady=2)

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

    btn_esc_pac = ctk.CTkButton(master=frame_campos, text='Escolher \nPaciente', font=('Arial',20), fg_color='#4CAF50', hover_color= "#45a049"
                                ,width=130, height=40, corner_radius=1)
    btn_esc_pac.grid(row=5,column=0,padx=2, pady=10)

    esc_pac_lbl = ctk.CTkLabel(master=frame_campos, text='Paciente', font=('Arial',20))
    esc_pac_lbl.grid(row=5,column=1,padx=2, pady=10)

    nome_atual = ctk.StringVar(value="Nenhum aluno selecionado")
    # pac_esc_lbl = ctk.CTkLabel(master=frame_campos, textvariable=nome_atual, font=('Arial',20))
    # pac_esc_lbl.grid(row=6,column=1,padx=2, pady=10)

    frame_btn = ctk.CTkFrame(master=frame_principal, width=400, height=450, fg_color="transparent")
    frame_btn.place(relx=0.5, rely=0.8,anchor='n')

    def salvar_aula():
        nome_consulta = cmp_nome_aula.get()
        dia = cmp_dia.get()
        mes = cmp_mes.get()
        ano = cmp_ano.get()
        hora = cmp_hora_aula.get()
        minuto = cmp_min_aula.get()

        data = f"{dia}/{mes}/{ano}"
        hora_aula = f"{hora}:{minuto}"
        nome_paciente = nome_atual.get()
        if not nome_consulta or not dia or not mes or not ano or not hora or not minuto:
            messagebox.showwarning("Atenção", "Preencha todos os campos!", parent=janela)
            return
        else:
            janela.destroy()
            messagebox.showinfo("Sucesso", "Agendamento realizado com sucesso!")
            adicionar_agendamentos(nome_consulta, data, hora_aula, nome_paciente)

            if atualizar_callback:
                atualizar_callback()
        
    btn_salvar = ctk.CTkButton(master=frame_btn, text='Salvar', text_color="#000000",width=150,height=40, 
                                corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049", command=salvar_aula)
    btn_salvar.pack(pady=(10,10))

    janela.mainloop()