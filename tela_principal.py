import customtkinter as ctk
from screeninfo import get_monitors
from tela_cadastrar_profissional import tela_cadastrar_profissional

def abrir_tela_principal():
    # === CONFIGURAÇÃO INICIAL === 
    ctk.set_appearance_mode('light')
    ctk.set_default_color_theme('blue')

    monitor = get_monitors()[0]
    janela = ctk.CTk()

    width = monitor.width
    height = monitor.height
    janela.geometry(f"{width}x{height}+0+0")
    janela.resizable(True, True)
    janela.title('Clínica RETRATA FISIO - PRINCIPAL')

        
    frame_principal = ctk.CTkFrame(master=janela, width=1200, height=750, fg_color="transparent", corner_radius=0)
    frame_principal.place(relx=0.6,rely=0.5,anchor="center")
    frame_principal.pack_propagate(False)
    
    frame_lateral = ctk.CTkFrame(master=janela, width=200, height=650, fg_color="#616161", corner_radius=0)
    frame_lateral.place(x=2,y=2)
    frame_lateral.pack_propagate(False)

    text_label = ctk.CTkLabel(master=frame_principal, text="Bem-vindo, ", font=('Arial', 30, 'bold'), text_color="#000000")
    text_label.pack(pady=(10,10))

    # ==== BOTÃO FISIOTERAPIA E PILATES ====
    def fisio():
        from tela_menu_aba_fisioterapia import abrir_menu_aba_fisioterapia
        abrir_menu_aba_fisioterapia()
    def pilates():
        from tela_menu_aba_pilates import abrir_menu_pilates
        abrir_menu_pilates()
    def profissional(frame):
        def cadastro_profissional():
            tela_cadastrar_profissional(frame_principal)
        
        btn_cad_prof = ctk.CTkButton(master=frame, text='Cadastrar', font=("Arial", 15),text_color="#FFFFFF",width=150,height=40, 
                            corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049", command=cadastro_profissional)
        btn_cad_prof.pack(pady=10)

    def buttonClick():    
        fr_lateral = ctk.CTkFrame(master=janela, width=200, height=650,fg_color="#616161", corner_radius=0)
        fr_lateral.place(x=205,y=2)
        fr_lateral.pack_propagate(False)
        profissional(fr_lateral)

    btn_fisio = ctk.CTkButton(master=frame_lateral, text='Fisioterapia', font=("Arial", 15),text_color="#FFFFFF",width=150,height=40, 
                            corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049",command=fisio)
    btn_fisio.pack(pady=10)
    btn_pilates = ctk.CTkButton(master=frame_lateral, text='Pilates', font=("Arial", 15),text_color="#FFFFFF",width=150,height=40, 
                            corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049",command=pilates)
    btn_pilates.pack(pady=10)

    btn_profissional = ctk.CTkButton(master=frame_lateral, text='Profissional', font=("Arial", 15),text_color="#FFFFFF",width=150,height=40, 
                            corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049", command=buttonClick)
    btn_profissional.pack(pady=10)
    
    btn_relatorio = ctk.CTkButton(master=frame_lateral, text='Relatórios', font=("Arial", 15),text_color="#FFFFFF",width=150,height=40, 
                            corner_radius=20, fg_color= "#4CAF50" , hover_color= "#45a049")
    btn_relatorio.pack(pady=10)
    
    janela.mainloop()
