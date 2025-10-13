import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from tela_cadastro_usuario_fisioterapia import abrir_cadastro_fisioterapia
from tela_lista_pacientes_fisioterapia import tela_lista_pacientes_fisio
from tela_inicio import abrir_inicio
from screeninfo import get_monitors
from tela_lista_pacientes_fisioterapia import tela_lista_pacientes_fisio
from tela_agendar_consultas import agendar_consultas
from tela_agendamentos_fisioterapia import tela_agendamentos_fisio

def abrir_menu_aba_fisioterapia():
    #Configuração inicial
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    menu_aba = ctk.CTk()
    menu_aba.title('Fisioterapia')

    menu_aba.geometry('1400x900')
    menu_aba.resizable(False, False)
    
    frame_principal = ctk.CTkFrame(master=menu_aba, width=1200, height=750, fg_color="transparent", corner_radius=0)
    frame_principal.place(relx=0.55,rely=0.5,anchor="center")
    frame_principal.pack_propagate(False)

    frame_top = ctk.CTkFrame(master=menu_aba, width=1600, height=50, fg_color="#1CA8D6", corner_radius=0)
    frame_top.place(x=2,y=2)
    frame_top.pack_propagate(False)


    # ==== BOTÃO CADASTRO ====
    def cadastro():
        abrir_cadastro_fisioterapia(frame_principal)

    # ==== BOTÃO LISTA PACIENTES ====
    def lista_alunos():
        tela_lista_pacientes_fisio(frame_principal)
    
    def agendar_aula():
        agendar_consultas(frame_principal)
    def agendamentos():
        tela_agendamentos_fisio(frame_principal)

    def buttonClick():    
        fr_lateral = ctk.CTkFrame(master=menu_aba, width=160, height=650,fg_color="#616161", corner_radius=0)
        fr_lateral.place(x=2,y=70)
        fr_lateral.pack_propagate(False)   

        btn_agendamentos = ctk.CTkButton(master=fr_lateral, text='Agendamentos', font=("Arial", 15),text_color="#FFFFFF",width=130,height=40, 
                            corner_radius=20, fg_color= "transparent" , hover_color= "#979797", command=agendamentos)
        btn_agendamentos.pack(pady=10)
        btn_agendar = ctk.CTkButton(master=fr_lateral, text='Agendar +', font=("Arial", 15),text_color="#FFFFFF",width=130,height=40, 
                                    corner_radius=20, fg_color= "transparent" , hover_color= "#979797", command=agendar_aula)
        btn_agendar.pack(pady=10)

    def buttonClick1():    
        fr_lateral = ctk.CTkFrame(master=menu_aba, width=160, height=650,fg_color="#616161", corner_radius=0)
        fr_lateral.place(x=2,y=70)
        fr_lateral.pack_propagate(False)   

        btn_cadastro = ctk.CTkButton(master=fr_lateral, text="Cadastrar", font=("Arial", 15) ,width=150, height=40, corner_radius=20,fg_color="transparent" , hover_color= "#979797", command=cadastro)
        btn_cadastro.pack(pady=10)
        btn_lista_paciente = ctk.CTkButton(master=fr_lateral, text="Lista de pacientes", font=("Arial", 15) ,width=150, height=40, corner_radius=20,fg_color="transparent" , hover_color= "#979797", command=lista_alunos)
        btn_lista_paciente.pack(pady=10)
    
    btn_paciente = ctk.CTkButton(master=frame_top, text="Paciente", font=("Arial", 15),text_color="#000000" ,width=130, height=50,
                                  corner_radius=0,fg_color="transparent" , hover_color= "#0093FC", command=buttonClick1)
    btn_paciente.pack(side="left", padx=10, pady=10)

    btn_consulta = ctk.CTkButton(master=frame_top, text="Agendamento", font=("Arial", 15),text_color="#000000" ,width=130, height=50, 
                                 corner_radius=0,fg_color="transparent" , hover_color= "#0093FC", command=buttonClick)
    btn_consulta.pack(side="left", padx=10, pady=10)

    menu_aba.mainloop()







