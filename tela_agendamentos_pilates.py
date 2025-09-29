import customtkinter as ctk
from tela_cadastrar_aula_pilates import obter_agendamentos

def tela_agendamentos_pilates(JANELA):
    
    frame = ctk.CTkFrame(master=JANELA, width=1200, height=750)
    frame.place(relx=0.5, rely=0.5,anchor='center')
    frame.pack_propagate(False)
    
    campo_pesquisar = ctk.CTkEntry(master=frame, placeholder_text="Pesquisar", font=('Arial', 15), width=300, height=30, corner_radius=10, border_color="#BFBFBF")
    campo_pesquisar.place(x=10,y=10)

    list_label = ctk.CTkLabel(master=frame,text="Agendamentos", font=('Arial', 25, 'bold'))
    list_label.pack(pady=(10,10))

    names = ctk.CTkTextbox(frame, width=1150, height=600, font=("Arial", 15))
    names.pack(pady=20)

    names.configure(state="normal")
    
    i = 0
    while i < len(obter_agendamentos()):
        names.insert("end", f"{obter_agendamentos()[i]}\n")
        i += 1