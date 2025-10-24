cadastros = []
DADOS_CADASTRAIS = []

cadastro = " "

def adicionar_cadastros(nome, email, telefone, opcao_pagamento, valor_pagar, endereco):
    # cadastro = f"{nome}, {email}, {telefone}, {opcao_pagamento}, {valor_pagar}, {endereco}"
    DADOS_CADASTRAIS.append(nome)               # INDICE = 1
    DADOS_CADASTRAIS.append(email)              # INDICE = 2
    DADOS_CADASTRAIS.append(telefone)           # INDICE = 3
    DADOS_CADASTRAIS.append(opcao_pagamento)    # INDICE = 4
    DADOS_CADASTRAIS.append(valor_pagar)        # INDICE = 5
    DADOS_CADASTRAIS.append(endereco)           # INDICE = 6
    cadastros.append(DADOS_CADASTRAIS)          # INDICE = 7

nome = input("Digite um nome:")
email = input("Digite um email:")
telefone = input("Digite um telefone:")
opcao_pagamento = input("Digite um opcao_pagamento:")
valor_pagar = input("Digite um valor_pagar:")
endereco = input("Digite um endereco:")

adicionar_cadastros(nome, email, telefone, opcao_pagamento, valor_pagar, endereco)
print(cadastros)