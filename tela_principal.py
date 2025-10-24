import customtkinter as ctk
from PIL import Image
from tela_cadastrar_profissional import tela_cadastrar_profissional
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

    frame_principal = ctk.CTkFrame(master=janela, width=1200, height=750, fg_color="transparent")
    frame_principal.place(relx=0.5,rely=0.55,anchor="center")
    frame_principal.pack_propagate(False)

    #BOTOES FRAME PRINCIPAL
    def button_painel():
        frame_btn = ctk.CTkFrame(master=frame_principal, width=1200, height=750, fg_color="#FFFFFF", corner_radius=10)
        frame_btn.place(relx=0.5,rely=0.5,anchor="center")
        frame_btn.pack_propagate(False)

        text_label = ctk.CTkLabel(master=frame_btn, text=f"Bem-vindo", font=('Arial', 30, 'bold'), text_color="#000000")
        text_label.pack(pady=(10,10))

        painel_principal(frame_btn)
        
    def painel_principal(frame):
    
        frame_btn1 = ctk.CTkFrame(master=frame, width=1200, height=750, fg_color="transparent", corner_radius=0)
        frame_btn1.place(relx=0.5,rely=0.5,anchor="center")
        frame_btn1.pack_propagate(False)

        btn_fisio = ctk.CTkButton(master=frame_btn1, text='Fisioterapia', font=("Arial", 30),text_color="#FFFFFF",width=350,height=200, 
                                corner_radius=20, fg_color= "#00B179" , hover_color= "#007F57",command=fisio)
        btn_fisio.grid(row=0, column=0, padx=20, pady=20)

        btn_pilates = ctk.CTkButton(master=frame_btn1, text='Pilates', font=("Arial", 30),text_color="#FFFFFF",width=350,height=200, 
                                corner_radius=20, fg_color= "#00B179" , hover_color= "#007F57",command=pilates)
        btn_pilates.grid(row=0, column=1, padx=20, pady=20)

        frame_prof = ctk.CTkFrame(master=frame_btn1,width=350,height=200, corner_radius=20, fg_color="transparent")
        frame_prof.grid(row=1, column=0, padx=5, pady=5)
        frame_prof.pack_propagate(False)

        btn_cad_pro = ctk.CTkButton(master=frame_prof, text='Cadastro \nFuncionário', font=("Arial", 20),text_color="#FFFFFF", 
                                    width=170,height=200, corner_radius=20, fg_color= "#00B179" , hover_color= "#007F57", command=profissional)
        btn_cad_pro.grid(row=0, column=0, padx=5, pady=5)

        from tela_quadro_funcionarios import tela_lista_funcionarios 
        btn_list_pro = ctk.CTkButton(master=frame_prof, text='Quadro \nFuncionários', font=("Arial", 20),text_color="#FFFFFF", 
                                    width=170,height=200, corner_radius=20, fg_color= "#00B179" , hover_color= "#007F57", command=lambda:tela_lista_funcionarios(frame_principal))
        btn_list_pro.grid(row=0, column=1, padx=5, pady=5)

        btn_relatorio = ctk.CTkButton(master=frame_btn1, text='Relatórios', font=("Arial", 30),text_color="#FFFFFF",width=350,height=200, 
                                corner_radius=20, fg_color= "#00B179" , hover_color= "#007F57")
        btn_relatorio.grid(row=1, column=1, padx=20, pady=20)

    #BOTOES DO FRAME TOP
    frame_top = ctk.CTkFrame(master=janela, width=1980, height=50, fg_color="#0068B1", corner_radius=0)
    frame_top.place(relx=0.5, rely=0.03, anchor='center')
    frame_top.pack_propagate(False)

    frame_1 = ctk.CTkFrame(master=frame_top, width=300, height=50, fg_color="transparent", corner_radius=0)
    frame_1.place(relx=0.5, rely=0.5, anchor='center')
    frame_1.pack_propagate(False)

    #BOTOES PRINCIPAIS
    def arbir_inicio():
        abrir_inicio(frame_principal)
    btn_inicio = ctk.CTkButton(master=frame_1, text='Início', font=("Arial", 17),text_color="#FFFFFF",width=100,height=50, 
                            corner_radius=0, fg_color= "transparent" , hover_color= "#005089", command=lambda: (arbir_inicio()))
    btn_inicio.grid(row=0, column=0, padx=0, pady=5)

    btn_painel = ctk.CTkButton(master=frame_1, text='Painel', font=("Arial", 17),text_color="#FFFFFF",width=100,height=50, 
                            corner_radius=0, fg_color= "transparent" , hover_color= "#005089", command=lambda: (button_painel()))
    btn_painel.grid(row=0, column=1, padx=0, pady=5)

    btn_clinica = ctk.CTkButton(master=frame_1, text='Clínica', font=("Arial", 17),text_color="#FFFFFF",width=100,height=50, 
                            corner_radius=0, fg_color= "transparent" , hover_color= "#005089", command=lambda:tela_gerenciador_clinica(frame_principal))
    btn_clinica.grid(row=0, column=2, padx=0, pady=5)

    #BOTOES DO USUÁRIO
    frame_user = ctk.CTkFrame(master=frame_top, width=100, height=50, fg_color="transparent")
    frame_user.place(relx=0.88, rely=0.5, anchor='center')
    frame_user.pack_propagate(False)

    icone_user = ctk.CTkImage(Image.open("icone_usuario.png"), size=(25, 25))
    botao_icon = ctk.CTkButton(frame_user,text="Usuário",image=icone_user, compound="right",width=40,height=40,
                               fg_color="transparent",hover_color="#005089", command=lambda: tela_informaçoes_usuário)
    botao_icon.pack(pady=10)

    #LOGO IMAGEM
    frame_img = ctk.CTkFrame(master=frame_top, width=200, height=80, fg_color='transparent')
    frame_img.place(relx=0.15, rely=0.5,anchor='center')
    frame_img.propagate(False)

    imagem_logo = ctk.CTkImage(light_image=Image.open('imagem.png'), dark_image=Image.open('imagem2.png'), size=(140,40))
    label_ = ctk.CTkLabel(master=frame_img, image=imagem_logo, text="")
    label_.pack(pady=(20,10))

    #TELA INICIO
    abrir_inicio(frame_principal)
    # ==== BOTÃO FISIOTERAPIA E PILATES ====
    def fisio():
        abrir_menu_aba_fisioterapia(janela)
    def pilates():
        abrir_menu_pilates(janela)
    def profissional():
        tela_cadastrar_profissional(frame_principal)

    janela.mainloop()