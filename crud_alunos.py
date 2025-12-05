from arquivo_conexao import conectar 
from mysql.connector import Error

def inserir_aluno(Nome_Aluno, Data_Nascimento_Aluno, CPF_Aluno, Endereco_Aluno, Telefone_Aluno, Email_Aluno):
    con = conectar()  # CHAMAR a função
    if con is None:
        return False
    
    cursor = con.cursor()

    comando = """
        INSERT INTO Alunos 
        (Nome_Aluno, Data_Nascimento_Aluno, CPF_Aluno, Endereco_Aluno, Telefone_Aluno, Email_Aluno) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        Nome_Aluno,
        Data_Nascimento_Aluno,
        CPF_Aluno,
        Endereco_Aluno,
        Telefone_Aluno,
        Email_Aluno
    )

    cursor.execute(comando, valores)  # AQUI EXECUTA CERTO
    con.commit()
    con.close()
    
    return True


def buscar_alunos():
    try:
        con = conectar()
        cursor = con.cursor(dictionary=True)

        sql = "SELECT * FROM Alunos ORDER BY Nome_Aluno ASC"
        cursor.execute(sql)

        dados = cursor.fetchall()  # retorna lista de dicionários

        con.close()
        return dados
    
    except Exception as e:
        print("Erro ao buscar alunos:", e)
        return []

def deletar_aluno(id_aluno):
    try:
        con = conectar()
        cursor = con.cursor()

        sql = "DELETE FROM Alunos WHERE ID_Aluno = %s"
        cursor.execute(sql, (id_aluno,))

        con.commit()
        con.close()
        return True

    except Exception as e:
        print("Erro ao deletar aluno:", e)
        return False

def atualizar_aluno(id, nome, cpf, data_nascimento, endereco, email, telefone):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = """
            UPDATE Alunos 
            SET Nome_Aluno=%s,
                CPF_Aluno=%s,
                Data_Nascimento_Aluno=%s,
                Endereco_Aluno=%s,
                Email_Aluno=%s,
                Telefone_Aluno=%s
            WHERE ID_Aluno=%s
        """

        valores = (nome, cpf, data_nascimento, endereco, email, telefone, id)

        cursor.execute(sql, valores)
        conn.commit()

        return True

    except Error as e:
        print("Erro ao atualizar:", e)
        return False

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()