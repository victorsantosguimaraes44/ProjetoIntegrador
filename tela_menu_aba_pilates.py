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

    menu_aba.geometry('1400x900')
    menu_aba.resizable(False, False)
    
    frame_principal = ctk.CTkFrame(master=menu_aba, width=1200, height=750, fg_color="transparent", corner_radius=0)
    frame_principal.place(relx=0.55,rely=0.5,anchor="center")
    frame_principal.pack_propagate(False)

    frame_top = ctk.CTkFrame(master=menu_aba, width=1600, height=50, fg_color="#616161", corner_radius=0)
    frame_top.place(x=2,y=2)
    frame_top.pack_propagate(False)


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
        btn_agendamentos = ctk.CTkButton(master=frame, text='Agendamentos', font=("Arial", 15),text_color="#FFFFFF",width=130,height=50, 
                            corner_radius=0, fg_color= "transparent" , hover_color= "#979797", command=agendamentos)
        btn_agendamentos.pack(pady=10)
        btn_agendar = ctk.CTkButton(master=frame, text='Agendar +', font=("Arial", 15),text_color="#FFFFFF",width=130,height=50, 
                                    corner_radius=0, fg_color= "transparent" , hover_color= "#979797", command=agendar_aula)
        btn_agendar.pack(pady=10)

    def buttonClick():    
        fr_lateral = ctk.CTkFrame(master=menu_aba, width=150, height=650,fg_color="#616161", corner_radius=0)
        fr_lateral.place(x=2,y=70)
        fr_lateral.pack_propagate(False)   

        agendar(fr_lateral)

    def buttonClick1():    
        fr_lateral = ctk.CTkFrame(master=menu_aba, width=150, height=650,fg_color="#616161", corner_radius=0)
        fr_lateral.place(x=2,y=70)
        fr_lateral.pack_propagate(False)   

        aluno(fr_lateral)

    def aluno(frame):
        btn_cadastro = ctk.CTkButton(master=frame, text="Cadastrar", font=("Arial", 15) ,width=130, height=50, corner_radius=0,fg_color="transparent" , hover_color= "#979797", command=cadastro)
        btn_cadastro.pack(pady=10)
        btn_lista_alunos = ctk.CTkButton(master=frame, text="Lista de alunos", font=("Arial", 15) ,width=130, height=50, corner_radius=0,fg_color="transparent" , hover_color= "#979797", command=lista_alunos)
        btn_lista_alunos.pack(pady=10)

    # frame_btn = ctk.CTkFrame(master=frame_top, width=300, height=50, fg_color="transparent", corner_radius=0)
    # frame_btn.place(relx=0.1, rely=0.5, anchor='center')

    btn_aluno = ctk.CTkButton(master=frame_top, text="Aluno", font=("Arial", 15) ,width=130, height=50, corner_radius=0,fg_color="transparent" , hover_color= "#979797", command=buttonClick1)
    btn_aluno.pack(side="left", padx=10, pady=10)

    btn_agendar_aula = ctk.CTkButton(master=frame_top, text="Agendamento", font=("Arial", 15) ,width=130, height=50, corner_radius=0,fg_color="transparent" , hover_color= "#979797", command=buttonClick)
    btn_agendar_aula.pack(side="left", padx=10, pady=10)

    menu_aba.mainloop()











