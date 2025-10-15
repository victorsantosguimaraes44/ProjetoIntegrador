import customtkinter as ctk
from PIL import Image
def posicionar_superior_direita(janela, largura, altura, margem=20):
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    x = largura_tela - largura - margem
    y = margem
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def tela_informaçoes_usuário(usuario):
    global image_user

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    janela = ctk.CTkToplevel()
    posicionar_superior_direita(janela, 400, 600)
    janela.title("Informações do Usuário")
    janela.attributes("-topmost", True)
    janela.resizable(False, False)
    janela.grab_set()

    frame = ctk.CTkFrame(master=janela, width=380, height=580, fg_color="#FFFFFF", corner_radius=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    frame.pack_propagate(False)

    image_user = ctk.CTkImage(Image.open("usuario.png"), size=(200,200))
    label_image_user = ctk.CTkLabel(master=frame, image=image_user, text="")
    label_image_user.pack(pady=(5,5))

    user_text = ctk.CTkLabel(master=frame, text=f"Usuário: {usuario}", font=('Arial', 20))
    user_text.pack(pady=(20,10))

    nome_text = ctk.CTkLabel(master=frame, text=f"Nome completo: ", font=('Arial', 20))
    nome_text.pack(pady=(20,10))

    btn_deslogar = ctk.CTkButton(master=frame, text="Sair", text_color="#000000", font=('Arial', 15),width=80, height=40, corner_radius=5, fg_color="#FF0000")
    btn_deslogar.pack(pady=(20,10))
    janela.mainloop()
