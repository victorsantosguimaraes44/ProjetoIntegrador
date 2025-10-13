import customtkinter as ctk
from tkinter import messagebox
from turtle import left
from PIL import Image

def abrir_tela_cadastro():
    ctk.set_appearance_mode('light')
    ctk.set_default_color_theme('blue')

    janela = ctk.CTk()
    janela.geometry('500x600')
    janela.title('CADASTRAR-SE - Clinica RETRATA FISIO')
    janela.attributes("-topmost", True)

    frame = ctk.CTkFrame(master=janela, width=450, height=550, fg_color="#CECECE", corner_radius=20)
    frame.place(relx=0.5, rely=0.5,anchor='center')
    frame.propagate(False)
    
    # TITULO
    titulo = ctk.CTkLabel(master=frame,text="Cadastrar-se",font=('Arial',30,'bold'))
    titulo.pack(pady=(10,10))

    # CAMPO NOME
    cmp_nome = ctk.CTkEntry(master=frame, placeholder_text="Nome completo", font=('Arial',20), width=400, height=50, corner_radius=10, border_color="#BFBFBF")
    cmp_nome.pack(pady=(10,10))

    # CAMPO USUARIOS
    cmp_nome = ctk.CTkEntry(master=frame, placeholder_text="Nome de usuário", font=('Arial',20), width=400, height=50, corner_radius=10, border_color="#BFBFBF")
    cmp_nome.pack(pady=(10,10))

    # CAMPO SENHA
    cmp_senha = ctk.CTkEntry(master=frame, placeholder_text="Crie uma senha", font=('Arial',20), width=400, height=50, corner_radius=10,show="*", border_color="#BFBFBF")
    cmp_senha.pack(pady=(10,10))

    # CAMPO CONFIRMAR SENHA
    cmp_confirmar_senha = ctk.CTkEntry(master=frame, placeholder_text="Confirmar senha", font=('Arial',20), width=400, height=50, corner_radius=10,show="*", border_color="#BFBFBF")
    cmp_confirmar_senha.pack(pady=(10,10))

    #BOTAO SALVAR

    def salvar():
        nome = cmp_nome.get()
        nome_usuario = cmp_nome.get()
        senha = cmp_senha.get()
        conf_senha = cmp_confirmar_senha.get()

        if conf_senha != senha:
            messagebox.showwarning("Atenção!", "as senhas são diferentes!")
        
        elif not nome or not nome_usuario or not senha or not conf_senha:
            messagebox.showwarning("Atenção!", "Preencha todos os campos")
             
        else:
            messagebox.showinfo("INFO", f"Usuário {nome_usuario} cadastrado com sucesso!")
            janela.destroy()


    def cancelar():
        janela.destroy()

    btn_salvar = ctk.CTkButton(master= frame, text="Salvar", width=100, height=40, corner_radius=10, fg_color= "#00B179" , hover_color= "#008057", command=salvar)
    btn_salvar.pack(pady=(10,10))

    #BOTAO CANCELAR
    btn_cancelar = ctk.CTkButton(master= frame, text="Cancelar", text_color="#000000",width=100, height=40, corner_radius=10, fg_color= "transparent" , hover_color= "#00B179", border_width=2, border_color="#00B179", command=cancelar)
    btn_cancelar.pack(pady=(10,10))

    # ===== GUARDAR AS INFORMAÇÕES =====
    janela.mainloop()