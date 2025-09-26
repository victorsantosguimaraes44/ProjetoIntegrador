import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from tela_cadastro_usuario_pilates import abrir_cadastro_pilates
from tela_lista_alunos_pilates import tela_lista_alunos_pilates
from tela_inicio import abrir_inicio
from screeninfo import get_monitors

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
    
    frame_principal = ctk.CTkFrame(master=menu_aba, width=1200, height=750, fg_color="#B5B6B5", corner_radius=0)
    frame_principal.place(relx=0.6,rely=0.5,anchor="center")
    frame_principal.pack_propagate(False)

    frame_lateral = ctk.CTkFrame(master=menu_aba, width=200, height=650, fg_color="#616161", corner_radius=0)
    frame_lateral.place(relx=0.15,rely=0.5,anchor="e")
    frame_lateral.pack_propagate(False)


    # ==== BOTÃO CADASTRO ====
    def cadastro():
        abrir_cadastro_pilates(frame_principal)
    btn_cadastro = ctk.CTkButton(master=frame_lateral, text="Cadastrar", font=("Arial", 15) ,width=150, height=40, fg_color="#4CAF50" , hover_color= "#45a049", command=cadastro)
    btn_cadastro.pack(pady=10)

    # ==== BOTÃO LISTA PACIENTES ====
    def lista_alunos():
        tela_lista_alunos_pilates(frame_principal)

    btn_lista_alunos = ctk.CTkButton(master=frame_lateral, text="Lista de alunos", font=("Arial", 15) ,width=150, height=40, fg_color="#4CAF50" , hover_color= "#45a049", command=lista_alunos)
    btn_lista_alunos.pack(pady=10)
    
    btn_cadastrar_aula = ctk.CTkButton(master=frame_lateral, text="Cadastrar aula", font=("Arial", 15) ,width=150, height=40, fg_color="#4CAF50" , hover_color= "#45a049")
    btn_cadastrar_aula.pack(pady=10)

    btn_relatorio = ctk.CTkButton(master=frame_lateral, text="Relatórios", font=("Arial", 15) ,width=150, height=40, fg_color="#4CAF50" , hover_color= "#45a049")
    btn_relatorio.pack(pady=10)


    menu_aba.mainloop()











