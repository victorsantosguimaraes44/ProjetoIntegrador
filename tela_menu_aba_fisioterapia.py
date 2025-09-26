import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from tela_cadastro_usuario_fisioterapia import abrir_cadastro_fisioterapia
from tela_lista_pacientes_fisioterapia import tela_lista_pacientes_fisio
from tela_inicio import abrir_inicio
from screeninfo import get_monitors
from tela_lista_pacientes_fisioterapia import tela_lista_pacientes_fisio

def abrir_menu_aba_fisioterapia():
    #Configuração inicial
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    menu_aba = ctk.CTk()
    menu_aba.title('Fisioterapia')

    monitor = get_monitors()[0]

    width = monitor.width
    height = monitor.height
    menu_aba.geometry(f"{width}x{height}+0+0")
    menu_aba.resizable(True, True)
    
    frame_principal = ctk.CTkFrame(master=menu_aba, width=1200, height=750, fg_color="#B5B6B5", corner_radius=0)
    frame_principal.place(relx=0.6,rely=0.5,anchor="center")
    frame_principal.pack_propagate(False)

    frame_lateral = ctk.CTkFrame(master=menu_aba, width=200, height=650, fg_color="#616161", corner_radius=0)
    frame_lateral.place(relx=0.15,rely=0.5,anchor="e")
    frame_lateral.pack_propagate(False)


    # ==== BOTÃO CADASTRO ====
    def cadastro():
        abrir_cadastro_fisioterapia(frame_principal)
    btn_cadastro = ctk.CTkButton(master=frame_lateral, text="Cadastrar", font=("Arial", 15) ,width=150, height=40, fg_color="#4CAF50" , hover_color= "#45a049", command=cadastro)
    btn_cadastro.pack(pady=10)

    # ==== BOTÃO LISTA PACIENTES ====
    def lista_pacientes():
        tela_lista_pacientes_fisio(frame_principal)
    btn_lista_pacientes = ctk.CTkButton(master=frame_lateral, text="Lista de pacientes", font=("Arial", 15) ,width=150, height=40, fg_color="#4CAF50" , hover_color= "#45a049", command=lista_pacientes)
    btn_lista_pacientes.pack(pady=10)
    
    btn_cadastrar_aula = ctk.CTkButton(master=frame_lateral, text="Cadastrar aula", font=("Arial", 15) ,width=150, height=40, fg_color="#4CAF50" , hover_color= "#45a049")
    btn_cadastrar_aula.pack(pady=10)

    btn_relatorio = ctk.CTkButton(master=frame_lateral, text="Relatórios", font=("Arial", 15) ,width=150, height=40, fg_color="#4CAF50" , hover_color= "#45a049")
    btn_relatorio.pack(pady=10)


    menu_aba.mainloop()





