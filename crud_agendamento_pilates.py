from arquivo_conexao import conectar

def buscar_agendamentos_p():
    con = conectar()
    cursor = con.cursor(dictionary=True)

    sql = "SELECT * FROM Aulas ORDER BY Nome_Aula ASC"
    cursor.execute(sql)

    dados = cursor.fetchall()  # retorna lista de dicionários

    con.close()
    return dados
    
def inserir_agendamento_p(data_aula, hora_aula, id_aluno,nome_aula):
    con = conectar()
    cursor = con.cursor()
    sql = """ INSERT INTO  Aulas(Data_Aula, Hora_Aula, ID_Aluno, Nome_Aula)
               VALUES(%s, %s, %s, %s)"""
    
    values = (data_aula, hora_aula, id_aluno,nome_aula)

    cursor.execute(sql, values)
    con.commit()
    con.close()

def deletar_agendamento_p(id_aula):
    try:
        con = conectar()
        cursor = con.cursor(dictionary=True)
        sql = """ DELETE FROM Aulas WHERE ID_Aula = %s"""

        cursor.execute(sql, (id_aula,))

        con.commit()
        con.close()

        return True
    except Exception as e:
        print(f"Erro: {e}")
        return False

