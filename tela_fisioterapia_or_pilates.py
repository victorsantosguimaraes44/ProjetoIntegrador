import customtkinter as ctk
from PIL import Image
import tela_menu_aba_fisioterapia
import tela_menu_aba_pilates

# # === FUNÇÃO PARA ABRIR MENU === 
def abrir_menu_():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    meu_app = ctk.CTk()
    meu_app.geometry("700x800")
    meu_app.title('Login - Clinica RETRATA FISIO')

    # === FRAME PRINCIPAL === 
    frame = ctk.CTkFrame(master=meu_app, width=600, height=700, corner_radius=15, border_color="#BDC3C7", border_width=3)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    frame.pack_propagate(False)

    logo_image = ctk.CTkImage(light_image=Image.open("imagem.png"),
    dark_image=Image.open("imagem2.png"),
    size=(300,150)) #TAMANHO DA LOGO (80X80 PX)

    #=== EXIBE A IMAGEM NO FRAME ===
    logo_label = ctk.CTkLabel(master=frame, image=logo_image, text="")
    logo_label.pack(pady=(50,40))


    def abrir_fisioterapia():
        meu_app.destroy()
        tela_menu_aba_fisioterapia.abrir_menu_aba_fisioterapia()

    def abrir_pilates():
        meu_app.destroy()
        tela_menu_aba_pilates.abrir_menu_pilates()
        
    # === BOTÕES DO MENU === 
    btn_cadastro_alunos = ctk.CTkButton(frame, text="PILATES", width=400 , height=100 , font=("Arial" , 25), fg_color= "#4CAF50" , hover_color= "#45a049" , command=abrir_pilates)
    btn_cadastro_alunos.pack(pady=10)

    btn_cadastro_pacientes = ctk.CTkButton(frame, text="FISIOTERAPIA", width=400 , height=100, font=("Arial" , 25) , fg_color= "#4CAF50" , hover_color= "#45a049", command=abrir_fisioterapia)
    btn_cadastro_pacientes.pack(pady=10)

    btn_sair = ctk.CTkButton(frame, text="Sair", width=180 , height=50, command=meu_app.destroy , fg_color= "#E74C3C"  , hover_color= "#FF4C4C")
    btn_sair.pack(pady=20)

    meu_app.mainloop()