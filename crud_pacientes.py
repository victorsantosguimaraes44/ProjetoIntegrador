from arquivo_conexao import conectar
from mysql.connector import Error

def inserir_paciente(nome_paciente, data_nascimento_paciente, telefone_paciente, cpf_paciente, endereco_paciente,email_paciente):
    con = conectar()
    if con is None:
        return False

    cursor = con.cursor()
    
    comando = """
                INSERT INTO Pacientes(Nome_Paciente, Data_Nascimento_Paciente, CPF_Paciente, Endereco_Paciente, Telefone_Paciente, Email_Paciente)
                VALUES (%s, %s, %s, %s,%s, %s)
              """
    valores=(nome_paciente, data_nascimento_paciente, cpf_paciente, endereco_paciente, telefone_paciente, email_paciente)
    cursor.execute(comando, valores)
    con.commit()
    con.close()

    return True

def buscar_paciente():
    try: 
        con = conectar() 
        cursor = con.cursor(dictionary=True)

        sql = "SELECT * FROM Pacientes ORDER BY Nome_Paciente ASC"
        cursor.execute(sql)

        dados = cursor.fetchall()
        con.close()

        return dados
    except Exception as e:
        print("Erro ao buscar paciente:", e)
        return []
    
def deletar_paciente(id_paciente):
    try:
        con = conectar()
        cursor = con.cursor(dictionary=True)

        sql = "DELETE FROM Pacientes WHERE ID_Paciente = %s"

        cursor.execute(sql,(id_paciente,))

        con.commit()
        con.close()

        return True
    except Exception as e:
        print("Erro ao deletar paciente:", e)
        return False

def atualizar_paciente(id, nome, cpf, data_nascimento, endereco, email, telefone):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = """
            UPDATE pacientes 
            SET Nome_Paciente=%s,
                CPF_Paciente=%s,
                Data_Nascimento_Paciente=%s,
                Endereco_Paciente=%s,
                Email_Paciente=%s,
                Telefone_Paciente=%s
            WHERE ID_Paciente=%s
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



