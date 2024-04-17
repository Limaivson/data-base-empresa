import mysql.connector
import config


class Mysql_connection:
    def __init__(self):
        # Conectando ao banco de dados
        self.conexao = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.data_base
        )

        # Criando o cursor
        self.cursor = self.conexao.cursor()
