from tkinter import messagebox
from turtle import left
import customtkinter as ctk
from PIL import Image
# from tela_fisioterapia_or_pilates import abrir_menu_

def abrir_inicio(JANELA_INICIO):
    frame_principal = ctk.CTkFrame(master=JANELA_INICIO, width=1200, height=750, corner_radius=10, fg_color="#E4E1E1")
    frame_principal.place(relx=0.5, rely=0.5,anchor='center')
    frame_principal.pack_propagate(False)

    imagem_logo = ctk.CTkImage(light_image=Image.open('imagem.png'), dark_image=Image.open('imagem2.png'), size=(600,300))
    label_ = ctk.CTkLabel(master=frame_principal, image=imagem_logo, text="")
    label_.pack(pady=(10,10))

    text_label = ctk.CTkLabel(master=frame_principal, text=f"Seja bem-vindo ao gerenciador da clínica RETRA FÍSIO", font=('Arial', 30, 'bold'), text_color="#000000")
    text_label.pack(pady=(10,10))