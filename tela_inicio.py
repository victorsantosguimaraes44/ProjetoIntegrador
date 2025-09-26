from tkinter import messagebox
from turtle import left
import customtkinter as ctk
from PIL import Image
# from tela_fisioterapia_or_pilates import abrir_menu_

def abrir_inicio(JANELA_INICIO):
    frame_principal = ctk.CTkFrame(master=JANELA_INICIO, width=750, height=650, corner_radius=10, fg_color="transparent")
    frame_principal.place(relx=0.5, rely=0.5,anchor='center')
    frame_principal.pack_propagate(False)

    frame_btn = ctk.CTkFrame(master=frame_principal, width=400, height=450, fg_color="transparent")
    frame_btn.place(relx=0.5, rely=0.8,anchor='n')

    imagem_logo = ctk.CTkImage(light_image=Image.open('imagem.png'), dark_image=Image.open('imagem2.png'), size=(300,150))
    label_ = ctk.CTkLabel(master=frame_principal, image=imagem_logo, text="")
    label_.pack(pady=(10,10))

    # def voltar():
    #     abrir_menu_()

    btn_voltar = ctk.CTkButton(master=frame_btn, text='Voltar', text_color="#000000",width=150,height=40, 
                                corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049")
    btn_voltar.pack(pady=(10,10), side = 'left', padx = 5)