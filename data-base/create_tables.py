from mysql_connection import Mysql_connection

connection = Mysql_connection()


def create_tables():
    # Criando a tabela Cliente
    connection.cursor.execute("""
    CREATE TABLE Cliente (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        telefone VARCHAR(15),
        endereco VARCHAR(255)
    )
    """)

    # Criando a tabela Funcionario
    connection.cursor.execute("""
    CREATE TABLE Funcionario (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        cargo VARCHAR(255)
    )
    """)

    # Criando a tabela Pagamento
    connection.cursor.execute("""
    CREATE TABLE Pagamento (
        id INT AUTO_INCREMENT PRIMARY KEY,
        valor DECIMAL(10, 2),
        tipo_pagamento VARCHAR(50),
        data DATE
    )
    """)

    # Criando a tabela de associação Pagamento_Cliente
    connection.cursor.execute("""
    CREATE TABLE Pagamento_Cliente (
        pagamento_id INT,
        cliente_id INT,
        FOREIGN KEY (pagamento_id) REFERENCES Pagamento(id),
        FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
    )
    """)

    # Finalizando e salvando as alterações
    connection.conexao.commit()

    # Fechando o cursor e a conexão
    connection.cursor.close()
    connection.conexao.close()

    print("Tabelas criadas com sucesso!")
