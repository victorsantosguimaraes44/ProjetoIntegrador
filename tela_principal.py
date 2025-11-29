import customtkinter as ctk
from PIL import Image
from tela_inicio import abrir_inicio
from tela_gerenciador_clínica import tela_gerenciador_clinica
from tela_menu_aba_fisioterapia import abrir_menu_aba_fisioterapia
from tela_menu_aba_pilates import abrir_menu_pilates
from tela_informações_usuário import tela_informaçoes_usuário

def abrir_tela_principal():
    ctk.set_appearance_mode('light')
    ctk.set_default_color_theme('blue')

    janela = ctk.CTk()
    janela.geometry("1600x900")
    janela.resizable(False, False)
    janela.title('Clínica RETRATA FISIO - PRINCIPAL')

    # Frame principal que conterá todas as telas
    frame_principal = ctk.CTkFrame(master=janela, width=1600, height=850, fg_color="#F5F5F5", corner_radius=0)
    frame_principal.place(relx=0.5, rely=0.53, anchor="center")
    frame_principal.pack_propagate(False)

    # Função para trocar telas
    def mostrar_tela(funcao_tela):
        for widget in frame_principal.winfo_children():
            widget.pack_forget()  # Remove a tela atual
        nova_tela = funcao_tela(frame_principal)
        nova_tela.pack(fill="both", expand=True)

    # Frame superior (menu)
    frame_top = ctk.CTkFrame(master=janela, width=1980, height=50, fg_color="#2E8B57", corner_radius=0)
    frame_top.pack(side='top')
    frame_top.pack_propagate(False)

    frame_1 = ctk.CTkFrame(master=frame_top, width=300, height=50, fg_color="transparent", corner_radius=0)
    frame_1.place(relx=0.5, rely=0.5, anchor='center')
    frame_1.pack_propagate(False)

    # Abre tela inicial ao iniciar
    mostrar_tela(abrir_inicio)

    # BOTÕES DO MENU SUPERIOR
    btn_inicio = ctk.CTkButton(
        master=frame_1, text='Início', font=("Arial", 17), text_color="#FFFFFF",
        width=100, height=50, corner_radius=0, fg_color="transparent",
        hover_color="#246C43", command=lambda: mostrar_tela(abrir_inicio)
    )
    btn_inicio.grid(row=0, column=0, padx=5, pady=0)

    btn_fisioterapia = ctk.CTkButton(
        master=frame_1, text='Fisioterapia', font=("Arial", 17), text_color="#FFFFFF",
        width=100, height=50, corner_radius=0, fg_color="transparent",
        hover_color="#246C43", command=lambda: mostrar_tela(abrir_menu_aba_fisioterapia)
    )
    btn_fisioterapia.grid(row=0, column=1, padx=5, pady=0)

    btn_agendamento = ctk.CTkButton(
        master=frame_1, text='Pilates', font=("Arial", 17), text_color="#FFFFFF",
        width=100, height=50, corner_radius=0, fg_color="transparent",
        hover_color="#246C43", command=lambda: mostrar_tela(abrir_menu_pilates)
    )
    btn_agendamento.grid(row=0, column=2, padx=5, pady=0)

    btn_gerenciador = ctk.CTkButton(
        master=frame_1, text='Gerenciador', font=("Arial", 17), text_color="#FFFFFF",
        width=100, height=50, corner_radius=0, fg_color="transparent",
        hover_color="#246C43", command=lambda: mostrar_tela(tela_gerenciador_clinica)
    )
    btn_gerenciador.grid(row=0, column=3, padx=5, pady=0)

    # BOTOES DO USUÁRIO
    frame_user = ctk.CTkFrame(master=frame_top, width=100, height=50, fg_color="transparent")
    frame_user.pack(side='right')
    frame_user.pack_propagate(False)

    icone_user = ctk.CTkImage(Image.open("icone_usuario.png"), size=(25, 25))
    botao_icon = ctk.CTkButton(
        frame_user, text="Usuário", image=icone_user, compound="right",
        width=40, height=40, fg_color="transparent", hover_color="#005089",
        command=lambda: mostrar_tela(tela_informaçoes_usuário)
    )
    botao_icon.pack(pady=10)

    # LOGO IMAGEM
    frame_img = ctk.CTkFrame(master=frame_top, width=200, height=80, fg_color='transparent')
    frame_img.pack(side='left')
    frame_img.propagate(False)

    imagem_logo = ctk.CTkImage(light_image=Image.open('imagem.png'), dark_image=Image.open('imagem2.png'), size=(140, 40))
    label_ = ctk.CTkLabel(master=frame_img, image=imagem_logo, text="")
    label_.pack(pady=(20, 10))

    janela.mainloop()
abrir_tela_principal()