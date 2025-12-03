from arquivo_conexao import conectar 

def inserir_aluno(Nome_Aluno , Data_Nascimento_Aluno , CPF_Aluno, Endereco_Aluno, Telefone_Aluno):
    con = conectar
    if con is None:
        return False
    cursor = con.cursor()
    comando = "INSERT INTO Alunos (Nome_Aluno , Data_Nascimento_Aluno , CPF_Aluno, Endereco_Aluno, Telefone_Aluno) VALUES (%s , %s , %s , %s , %s)"
    cursor.execute(comando(Nome_Aluno , Data_Nascimento_Aluno , CPF_Aluno, Endereco_Aluno, Telefone_Aluno))
    con.commit()
    con.close()
    return True

def listar_aluno():
    con = conectar()
    if con is None:
        return[]
    cursor = con.cursor(dictionary=True)
    comando = "SELECT * FROM Alunos ORDER BY Nome_Aluno ASC"
    cursor.execute(comando)
    resultado = cursor.fetchall()
    con.close()
    return resultado

def excluir_aluno(ID_Aluno):
    con = conectar()
    if con is None: 
        return False 
    cursor = con.cursor()
    comando = "DELETE FROM Alunos WHERE ID_Aluno = %s"
    cursor.execute(comando , (ID_Aluno,))
    con.commit()
    con.close()
    return True 