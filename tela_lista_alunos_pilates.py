import customtkinter as ctk
from tela_cadastro_usuario_pilates import obter_cadastros
# from gerador_de_dados_aleatorios import obter_dados_aleatorios

def tela_lista_alunos_pilates(JANELA):
    
    frame = ctk.CTkFrame(master=JANELA, width=1200, height=750)
    frame.place(relx=0.5, rely=0.5,anchor='center')
    frame.pack_propagate(False)

    campo_pesquisar = ctk.CTkEntry(master=frame, placeholder_text="Pesquisar", font=('Arial', 15), width=300, height=30, corner_radius=10, border_color="#BFBFBF")
    campo_pesquisar.place(x=10,y=10)

    list_label = ctk.CTkLabel(master=frame,text="Lista de alunos", font=('Arial', 25, 'bold'))
    list_label.pack(pady=(10,10))


    frame_btn_name = ctk.CTkScrollableFrame(master=JANELA, width=1150, height=600, corner_radius=0, fg_color="#FFFFFF")
    frame_btn_name.place(relx=0.5, rely=0.5,anchor='center')

    for i in range(len(obter_cadastros())):
        btn_name = ctk.CTkButton(master=frame_btn_name, text=f"{obter_cadastros()[i]}", font=('Arial', 15), 
                                 width=1150, height=20, corner_radius=0, text_color="#000000",
                                 fg_color="#E3E3E3", hover_color="#929090")
        btn_name.pack(pady=2)