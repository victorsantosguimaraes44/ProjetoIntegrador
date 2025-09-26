import customtkinter as ctk
from tela_cadastro_usuario_pilates import obter_cadastros
# from gerador_de_dados_aleatorios import obter_dados_aleatorios

def tela_lista_alunos_pilates(JANELA):
    
    frame = ctk.CTkFrame(master=JANELA, width=1200, height=750)
    frame.place(relx=0.5, rely=0.5,anchor='center')
    frame.pack_propagate(False)

    list_label = ctk.CTkLabel(master=frame,text="Lista de pacientes", font=('Arial', 25, 'bold'))
    list_label.pack(pady=(10,10))

    names = ctk.CTkTextbox(frame, width=1150, height=600, font=("Arial", 15))
    names.pack(pady=20)

    names.configure(state="normal")
    
    i = 0
    while i < len(obter_cadastros()):
        names.insert("end", f"{obter_cadastros()[i]}\n")
        i += 1