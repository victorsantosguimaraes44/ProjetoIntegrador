import customtkinter as ctk
from PIL import Image

def tela_informaçoes_usuário(usuario):
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    janela = ctk.CTk()
    janela.geometry("400x600")
    janela.title("Informações do Usuário")
    janela.attributes("-topmost", True)

    frame = ctk.CTkFrame(master=janela, width=380, height=580, fg_color="#FFFFFF", corner_radius=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    frame.pack_propagate(False)

    nome_text = ctk.CTkLabel(master=frame, text=f"Nome: {usuario}", font=('Arial', 20))
    nome_text.pack(pady=(20,10))

    janela.mainloop()

