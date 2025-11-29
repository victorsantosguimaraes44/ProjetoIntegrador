import customtkinter as ctk
from PIL import Image
# from tela_fisioterapia_or_pilates import abrir_menu_

def abrir_inicio(JANELA_INICIO):
    frame_principal = ctk.CTkFrame(master=JANELA_INICIO, width=1600, height=850, corner_radius=0, fg_color="transparent")
    frame_principal.place(relx=0.5, rely=0.5,anchor='center')
    frame_principal.pack_propagate(False)

    imagem_logo = ctk.CTkImage(light_image=Image.open('imagem.png'), dark_image=Image.open('imagem2.png'), size=(800,200))
    label_ = ctk.CTkLabel(master=frame_principal, image=imagem_logo, text="")
    label_.pack(pady=(10,10))

    # Frame superior
    frame_topo = ctk.CTkFrame(master=frame_principal, width=1000, height=100,fg_color="transparent")
    frame_topo.pack(fill='x', side='top', pady=10)

    titulo = "SEJA BEM-VINDO(A) à Clínica RETRATA fisio"
    label_titulo = ctk.CTkLabel(
        master=frame_topo,
        text=titulo,
        font=ctk.CTkFont(family="Helvetica", size=30, weight="bold", slant="italic"),
        justify='center',
        text_color="#4E342E"  # marrom escuro
    )
    label_titulo.pack(pady=(5, 10), padx=20)

    # Texto de boas-vindas em tom terroso
    texto_resto = (
        "Um espaço dedicado à sua saúde e qualidade de vida. "
        "Atuamos com foco na fisioterapia reabilitadora e funcional, "
        "além de oferecer aulas personalizadas de Pilates, sempre com o acompanhamento de profissionais qualificados."
    )

    # Frame de fundo bege claro (terra suave)
    frame_texto = ctk.CTkFrame(
        master=frame_topo,
        fg_color="transparent",  # bege claro
        corner_radius=10
    )
    frame_texto.pack(pady=(0, 20), padx=40, fill='x')

    # Texto com cor marrom média
    label_resto = ctk.CTkLabel(
        master=frame_texto,
        text=texto_resto,
        font=ctk.CTkFont(family="Arial", size=25),
        justify='center',
        wraplength=700,
        text_color="#6D4C41",  # marrom médio
        fg_color="transparent"
    )
    label_resto.pack(padx=15, pady=15)

    # Frame intermediário
    frame_meio = ctk.CTkFrame(master=frame_principal, height=20, fg_color="transparent")
    frame_meio.pack(padx=15, pady=15, side='top')

    # Frame inferior com imagens
    frame_inferior = ctk.CTkFrame(master=frame_principal, height=325, fg_color="transparent")
    frame_inferior.place(relx=0.5,rely=0.8,anchor="center")

    imagem2 = ctk.CTkImage(
        light_image=Image.open('pilates_1.png'),
        dark_image=Image.open('pilates_1.png'),
        size=(375, 325)
    )
    label_img2 = ctk.CTkLabel(master=frame_inferior, image=imagem2, text="")
    label_img2.pack(side='left')

    imagem3 = ctk.CTkImage(
        light_image=Image.open('fisio1.png'),
        dark_image=Image.open('fisio1.png'),
        size=(375, 325)
    )
    label_img3 = ctk.CTkLabel(master=frame_inferior, image=imagem3, text="")
    label_img3.pack(side='left')

    return frame_principal