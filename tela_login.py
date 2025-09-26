import customtkinter as ctk
from PIL import Image
import tela_fisioterapia_or_pilates
import tela_cadastro
from screeninfo import get_monitors

# === CONFIGURAÇÃO INICIAL === 
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

monitor = get_monitors()[0]
janela = ctk.CTk()

width = monitor.width
height = monitor.height
janela.geometry(f"{width}x{height}+0+0")
janela.resizable(True, True)
janela.title('Login - Clínica RETRATA FISIO')



# === FRAME CENTRAL ===

frame_login = ctk.CTkFrame(master=janela, width=750, height=750, corner_radius=0)
frame_login.place(relx=0.5, rely=0.5,anchor='e')
frame_login.propagate(False)

frame = ctk.CTkFrame(master=frame_login, width=525, height=400, fg_color="#CECECE", corner_radius=20)
frame.place(relx=0.5, rely=0.5,anchor='center')
frame.propagate(False)

frame_imagem = ctk.CTkFrame(master=janela, width=750, height=750, border_color="#BDC3C7", corner_radius=0)
frame_imagem.place(relx=0.5, rely=0.5,anchor='w')
frame_imagem.pack_propagate(False)

frame_img = ctk.CTkFrame(master=frame_imagem, width=600, height=300, fg_color='transparent', border_width=2, border_color="#BF8989", corner_radius=20)
frame_img.place(relx=0.5, rely=0.5,anchor='center')
frame_img.propagate(False)

imagem_logo = ctk.CTkImage(light_image=Image.open('imagem.png'), dark_image=Image.open('imagem2.png'), size=(500,250))
label_ = ctk.CTkLabel(master=frame_img, image=imagem_logo, text="")
label_.pack(pady=(20,10))

# TITULO
titulo = ctk.CTkLabel(master=frame,text="LOGIN",font=('Arial',30,'bold'))
titulo.pack(pady=(10,10))

# SUBTITULO
subtitulo = ctk.CTkLabel(master=frame,text="Faça login para continuar",font=('Arial',20))
subtitulo.pack(pady=(10,10))

# CAMPO DE USUARIO
cmp_entrar = ctk.CTkEntry(master=frame, placeholder_text="Usuário", font=('Arial',20), width=450, height=50, corner_radius=10, border_color="#BFBFBF")
cmp_entrar.pack(pady=(10,10))

# CAMPO SENHA
cmp_senha = ctk.CTkEntry(master=frame, placeholder_text="Senha", font=('Arial',20), width=450, height=50, corner_radius=10,show="*", border_color="#BFBFBF")
cmp_senha.pack(pady=(10,10))

# === FUNÇÃO PARA ABRIR O MENU ===
def abrir_menu():
    janela.destroy()
    tela_fisioterapia_or_pilates.abrir_menu_()

# BOTAO LOGIN
btn_login = ctk.CTkButton(master=frame, text="Entrar", font=('Arial',20) , width=250 , height=40,
                           corner_radius=50, fg_color= "#4CAF50" , hover_color= "#45a049" , command=abrir_menu)
btn_login.pack(pady=20)

# === BOTÃO DE CADASTRO === 

def abrir_cadastro():
    tela_cadastro.abrir_tela_cadastro()

btn_register = ctk.CTkButton(master=frame, text = "Cadastre-se", font=('Arial',20) , width=250 , height=40,
                             corner_radius=50, fg_color="transparent" , hover_color= "#45a049" ,
                             border_width=2, border_color= "#4CAF50" , text_color= "#0E140E", command=abrir_cadastro)

btn_register.pack()

janela.mainloop()

