import customtkinter as ctk
from PIL import Image
from tela_agendar_consultas import obter_agendamentos_fisio
from tela_cadastrar_aula_pilates import obter_agendamentos_pilates

def tela_gerenciador_clinica(JANELA):
    
    agendamentos_totais = []

    num_atendimentos_totais = 0
    while num_atendimentos_totais < len(obter_agendamentos_fisio()) + len(obter_agendamentos_pilates()):
        num_atendimentos_totais += 1
        print(num_atendimentos_totais)
    num_atendimentos_concluidos = 0
    num_atendimentos_pendentes = num_atendimentos_totais - num_atendimentos_concluidos

    if len(obter_agendamentos_fisio()) != 0 or len(obter_agendamentos_pilates()):
        agendamentos_totais.append(obter_agendamentos_fisio())
        agendamentos_totais.append(obter_agendamentos_pilates())

    frame_principal = ctk.CTkFrame(master=JANELA, width=1200, height=750, fg_color="#E4E1E1", corner_radius=0)
    frame_principal.place(relx=0.5,rely=0.5,anchor="center")
    frame_principal.pack_propagate(False)

    text_label = ctk.CTkLabel(master=frame_principal, text=f"Gerenciador da Clínica", font=('Arial', 25, 'bold'), text_color="#000000")
    text_label.pack(pady=(10,10))


    #ATENDIMENTOS REALIZADOS
    frame_atendimentos_realizados = ctk.CTkFrame(master=frame_principal, width=200, height=200, fg_color="#C6C6C6", corner_radius=10)
    frame_atendimentos_realizados.place(relx=0.2,rely=0.4,anchor="se")
    frame_atendimentos_realizados.pack_propagate(False)

    text_atendimentos_realizados = ctk.CTkLabel(master=frame_atendimentos_realizados, text=f"Atendimentos concluídos", font=('Arial', 15, 'bold'), text_color="#000000")
    text_atendimentos_realizados.pack(pady=(10,10))

    number_atendimentos_realizados = ctk.CTkLabel(master=frame_atendimentos_realizados, text=f"{num_atendimentos_concluidos}", font=('Arial', 60, 'bold'), text_color="#26FF00")
    number_atendimentos_realizados.pack(pady=(10,10))

    #ATENDIMENTOS PENDENTES
    frame_atendimentos_pendentes = ctk.CTkFrame(master=frame_principal, width=200, height=200, fg_color="#C6C6C6", corner_radius=10)
    frame_atendimentos_pendentes.place(relx=0.4,rely=0.4,anchor="se")
    frame_atendimentos_pendentes.pack_propagate(False)

    text_atendimentos_pendentes = ctk.CTkLabel(master=frame_atendimentos_pendentes, text=f"Atendimentos pendentes", font=('Arial', 15, 'bold'), text_color="#000000")
    text_atendimentos_pendentes.pack(pady=(10,10))

    number_atendimentos_pendentes = ctk.CTkLabel(master=frame_atendimentos_pendentes, text=f"{num_atendimentos_pendentes}", font=('Arial', 60, 'bold'), text_color="#FF0000")
    number_atendimentos_pendentes.pack(pady=(10,10))

    #ATENDIMENTOS TOTAIS
    frame_atendimentos_totais = ctk.CTkFrame(master=frame_principal, width=200, height=200, fg_color="#C6C6C6", corner_radius=10)
    frame_atendimentos_totais.place(relx=0.6,rely=0.4,anchor="se")
    frame_atendimentos_totais.pack_propagate(False)

    text_atendimentos_totais = ctk.CTkLabel(master=frame_atendimentos_totais, text=f"Atendimentos totais", font=('Arial', 15, 'bold'), text_color="#000000")
    text_atendimentos_totais.pack(pady=(10,10))

    number_atendimentos_totais = ctk.CTkLabel(master=frame_atendimentos_totais, text=f"{num_atendimentos_totais}", font=('Arial', 60, 'bold'), text_color="#4F4F4F")
    number_atendimentos_totais.pack(pady=(10,10))

    #SCROLL VIEW DE ATENDIMENTOS

    
    frame_scroll = ctk.CTkScrollableFrame(master=frame_principal, width=1150, height=350, fg_color="#C6C6C6", corner_radius=10)
    frame_scroll.place(relx=0.5,rely=0.75,anchor="center")

    for i in range(len(agendamentos_totais)):
        btn_name = ctk.CTkButton(master=frame_scroll, text=f"{agendamentos_totais[i]}", font=('Arial', 15), 
                                    width=1150, height=20, corner_radius=0, text_color="#000000",
                                    fg_color="#E3E3E3", hover_color="#929090")
        btn_name.pack(pady=1)