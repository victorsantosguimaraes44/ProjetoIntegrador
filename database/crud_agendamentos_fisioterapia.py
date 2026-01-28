from database.arquivo_conexao import conectar
from mysql.connector import Error

def buscar_agendamento_f():
    con = conectar()
    cursor = con.cursor(dictionary=True)

    sql = 'SELECT * FROM Consultas ORDER BY Nome_Consulta'

    cursor.execute(sql)
    dados = cursor.fetchall()

    con.close()
    return dados

def inserir_agendamento_f(data_consulta, hora_consulta, id_paciente, nome_consulta):
    con = conectar()
    cursor = con.cursor(dictionary=True)

    sql = """INSERT INTO Consultas(Data_Consulta, Hora_Consulta, ID_Paciente, Nome_Consulta) 
             VALUES(%s, %s, %s, %s)"""
    
    values = (data_consulta, hora_consulta, id_paciente, nome_consulta)

    cursor.execute(sql, values)

    con.commit()
    con.close()

def deletar_agendamento_f(id_consulta):
    try:
        con = conectar()
        cursor = con.cursor(dictionary=True)

        sql = """DELETE FROM Consultas WHERE ID_Consulta = %s"""

        cursor.execute(sql, (id_consulta,))
        con.commit
        con.close

        return True
    except Exception as e:
        print(f"Erro: {e}")

def atualizar_agendamento(id, nome, data, hora):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = """
            UPDATE Consultas 
            SET Nome_Consulta=%s,
                Data_Consulta=%s,
                Hora_Consulta=%s
            WHERE ID_Consulta=%s
        """

        valores = (nome, data, hora, id)

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


def pesquisar_ag_f(nome):
    con = conectar()
    cursor = con.cursor(dictionary=True)

    sql = """SELECT * FROM Consultas WHERE Nome_Consulta LIKE %s ORDER BY Nome_Consulta"""

    cursor.execute(sql, (f"%{nome}%",))
    dados = cursor.fetchall()

    cursor.close()  
    con.close()
    return dados