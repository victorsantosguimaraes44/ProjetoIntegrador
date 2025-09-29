import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from tela_cadastro_usuario_pilates import abrir_cadastro_pilates
from tela_lista_alunos_pilates import tela_lista_alunos_pilates
from tela_inicio import abrir_inicio
from screeninfo import get_monitors
from tela_cadastrar_aula_pilates import tela_cadastrar_aula_pilates
from tela_agendamentos_pilates import tela_agendamentos_pilates

def abrir_menu_pilates():
    #Configuração inicial
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    menu_aba = ctk.CTk()
    menu_aba.title('Pilates')

    monitor = get_monitors()[0]

    width = monitor.width
    height = monitor.height
    menu_aba.geometry(f"{width}x{height}+0+0")
    menu_aba.resizable(True, True)
    
    frame_principal = ctk.CTkFrame(master=menu_aba, width=1200, height=750, fg_color="transparent", corner_radius=0)
    frame_principal.place(relx=0.6,rely=0.5,anchor="center")
    frame_principal.pack_propagate(False)

    frame_lateral = ctk.CTkFrame(master=menu_aba, width=200, height=650, fg_color="#616161", corner_radius=0)
    frame_lateral.place(relx=0.15,rely=0.5,anchor="e")
    frame_lateral.pack_propagate(False)


    # ==== BOTÃO CADASTRO ====
    def cadastro():
        abrir_cadastro_pilates(frame_principal)

    # ==== BOTÃO LISTA PACIENTES ====
    def lista_alunos():
        tela_lista_alunos_pilates(frame_principal)
    
    def agendar_aula():
        tela_cadastrar_aula_pilates(frame_principal)
    def agendamentos():
        tela_agendamentos_pilates(frame_principal)

    def agendar(frame):
        btn_agendamentos = ctk.CTkButton(master=frame, text='Agendamentos', font=("Arial", 15),text_color="#FFFFFF",width=150,height=40, 
                            corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049", command=agendamentos)
        btn_agendamentos.pack(pady=10)
        btn_agendar = ctk.CTkButton(master=frame, text='Agendar +', font=("Arial", 15),text_color="#FFFFFF",width=150,height=40, 
                                    corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049", command=agendar_aula)
        btn_agendar.pack(pady=10)

    def buttonClick():    
        fr_lateral = ctk.CTkFrame(master=menu_aba, width=200, height=650,fg_color="#616161", corner_radius=0)
        fr_lateral.place(relx=0.26,rely=0.5,anchor="e")
        fr_lateral.pack_propagate(False)   

        agendar(fr_lateral)

    def buttonClick1():    
        fr_lateral = ctk.CTkFrame(master=menu_aba, width=200, height=650,fg_color="#616161", corner_radius=0)
        fr_lateral.place(relx=0.26,rely=0.5,anchor="e")
        fr_lateral.pack_propagate(False)   

        aluno(fr_lateral)

    def aluno(frame):
        btn_cadastro = ctk.CTkButton(master=frame, text="Cadastrar", font=("Arial", 15) ,width=150, height=40, corner_radius=20,fg_color="#4CAF50" , hover_color= "#45a049", command=cadastro)
        btn_cadastro.pack(pady=10)
        btn_lista_alunos = ctk.CTkButton(master=frame, text="Lista de alunos", font=("Arial", 15) ,width=150, height=40, corner_radius=20,fg_color="#4CAF50" , hover_color= "#45a049", command=lista_alunos)
        btn_lista_alunos.pack(pady=10)
    
    btn_aluno = ctk.CTkButton(master=frame_lateral, text="Aluno", font=("Arial", 15) ,width=150, height=40, corner_radius=20,fg_color="#4CAF50" , hover_color= "#45a049", command=buttonClick1)
    btn_aluno.pack(pady=10)

    btn_agendar_aula = ctk.CTkButton(master=frame_lateral, text="Agendamento", font=("Arial", 15) ,width=150, height=40, corner_radius=20,fg_color="#4CAF50" , hover_color= "#45a049", command=buttonClick)
    btn_agendar_aula.pack(pady=10)

    btn_relatorio = ctk.CTkButton(master=frame_lateral, text="Relatórios", font=("Arial", 15) ,width=150, height=40, corner_radius=20,fg_color="#4CAF50" , hover_color= "#45a049")
    btn_relatorio.pack(pady=10)


    menu_aba.mainloop()











