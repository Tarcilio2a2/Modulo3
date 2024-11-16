import mysql.connector
from mysql.connector import Error

# Função para criar a conexão com o banco de dados
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Altere conforme seu banco de dados
            database='farmtech',  # Nome do seu banco de dados
            user='root',  # Seu usuário
            password='password'  # Sua senha
        )
        if connection.is_connected():
            print("Conexão bem-sucedida ao MySQL")
        return connection
    except Error as e:
        print("Erro ao conectar no MySQL", e)
        return None

# Função para inserir dados no banco
def insert_sensor_data(p, k, ph, humidity):
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()
    query = """INSERT INTO sensor_data (p_sensor, k_sensor, ph_value, humidity)
               VALUES (%s, %s, %s, %s)"""
    data = (p, k, ph, humidity)

    try:
        cursor.execute(query, data)
        connection.commit()
        print("Dados inseridos com sucesso")
    except Error as e:
        print("Erro ao inserir dados no MySQL", e)
    finally:
        cursor.close()
        connection.close()

# Função para ler dados do banco
def fetch_data():
    connection = create_connection()
    if connection is None:
        return []

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 10")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Exemplo de como inserir e consultar dados
insert_sensor_data(1, 0, 6.8, 30.5)  # Insira os dados do sensor manualmente
data = fetch_data()
print(data)
