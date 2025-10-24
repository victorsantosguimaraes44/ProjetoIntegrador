import mysql.connector
from mysql.connector import Error

def conectar(): 
    try: 
        conexao = mysql.connector.connect(
            host = "localhost" , 
            user = "root" , 
            password = "" , 
            database = "clinica_retratafisio"
        )
        return conexao
    except Error as e: 
        print(f'Erro ao conectar: {e}')
        return None