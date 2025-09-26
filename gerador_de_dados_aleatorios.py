import random
import string

qnt_dados_gerados = 2
qnt_letras = 5
qnt_num = 5
list = []
num_tel_list = []
dds_list = []
nome = " "
num_tel = " "
email = " "
data_nascimento = " "
forma_pagamento = " "
dados_aleatorios = " "

def gerar_dados_aleatorios():
    #NOMES ALEATORIOS
    i = 0
    while i < qnt_letras and qnt_num:
        i += 1
        letras = random.choice(string.ascii_letters)
        numeros = str(random.randint(1, 10))
        list.append(letras + numeros)
        nome = ''.join(str(i) for i in list)
        
    #TELEFONES ALEATORIOS
    j = 0
    while j < 8:
        j += 1
        num_tel_list.append(str(random.randint(0, 9)))
        num_ = ''.join(str(j) for j in num_tel_list)
        num_tel = "919" + num_
    #EMAILS ALEATORIOS
    email = nome + "@gmail.com"
    #DATA DE NASCIMENTO ALEATORIA
    o = 0
    while o < 8:
        o += 1
        dia = (str(random.randint(1, 30)))
        mes = (str(random.randint(1, 12)))
        ano = (str(random.randint(1950, 2025)))
        data_nascimento = f"{dia}/{mes}/{ano}"
    #DADOS CONCATENADOS
    dados_aleatorios = f"nome: {nome} | tel: {num_tel} | email: {email} | data de nascimento:{data_nascimento}"
    dds_list.append(dados_aleatorios)
    # print(dados_aleatorios)
    #ELIMINAR DADOS
    list.clear()
    num_tel_list.clear()

def obter_dados_aleatorios():
    return dds_list
print(obter_dados_aleatorios())



