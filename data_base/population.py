import mysql.connector
from mysql_connection import Mysql_connection

connection = Mysql_connection()

# Lista de clientes com nomes e endereços reais
clientes = [
    ("João Silva", "(11) 91234-5678", "Rua A, 123"),
    ("Maria Santos", "(11) 98765-4321", "Avenida B, 456"),
    ("Carlos Oliveira", "(11) 99876-5432", "Rua C, 789"),
    ("Ana Pereira", "(11) 95555-4444", "Rua D, 321"),
    ("Fernanda Lima", "(11) 93333-1111", "Avenida E, 567"),
    ("Paulo Costa", "(11) 92222-2222", "Rua F, 987"),
    ("Aline Almeida", "(11) 94444-3333", "Avenida G, 654"),
    ("Roberto Martins", "(11) 97777-5555", "Rua H, 321"),
    ("Juliana Ferreira", "(11) 96666-4444", "Avenida I, 987"),
    ("Lucas Gomes", "(11) 95555-8888", "Rua J, 123"),
    ("Camila Barbosa", "(11) 98888-1111", "Avenida K, 456"),
    ("Ricardo Araújo", "(11) 96666-2222", "Rua L, 789"),
    ("Mariana Ribeiro", "(11) 93333-3333", "Avenida M, 321"),
    ("Felipe Nunes", "(11) 92222-4444", "Rua N, 654"),
    ("Bianca Cardoso", "(11) 91111-5555", "Avenida O, 987"),
    ("Gustavo Batista", "(11) 94444-6666", "Rua P, 123"),
    ("Larissa Rocha", "(11) 93333-7777", "Avenida Q, 456"),
    ("Daniel Oliveira", "(11) 96666-8888", "Rua R, 789"),
    ("Amanda Alves", "(11) 95555-9999", "Avenida S, 321"),
    ("Guilherme Santos", "(11) 92222-1111", "Rua T, 654"),
    ("Patricia Costa", "(11) 98888-2222", "Avenida U, 987"),
    ("Diego Martins", "(11) 93333-4444", "Rua V, 123"),
    ("Leticia Ferreira", "(11) 94444-5555", "Avenida W, 456"),
    ("Luciana Lima", "(11) 91111-6666", "Rua X, 789"),
    ("Roberto Souza", "(11) 96666-9999", "Avenida Y, 321"),
    ("Renata Barbosa", "(11) 93333-1111", "Rua Z, 654"),
    ("Laura Silva", "(11) 91234-5678", "Rua AA, 123"),
    ("Gabriel Santos", "(11) 98765-4321", "Avenida BB, 456"),
    ("Luis Oliveira", "(11) 99876-5432", "Rua CC, 789"),
    ("Fernanda Pereira", "(11) 95555-4444", "Rua DD, 321")
]

# Lista de funcionários
funcionarios = [
    ("Rafael", "Dono"),
    ("José", "Funcionário"),
    ("Suemo", "Funcionário"),
    ("Marcos", "Funcionário"),
    ("Pedro", "Funcionário")
]

connection.cursor.execute("DROP TABLE IF EXISTS Pagamento_Cliente")
connection.cursor.execute("DROP TABLE IF EXISTS Funcionario")
connection.cursor.execute("DROP TABLE IF EXISTS Cliente")
connection.cursor.execute("DROP TABLE IF EXISTS Pagamento")

import create_tables

create_tables.create_tables()

# Inserir dados na tabela Cliente
for cliente in clientes:
    connection.cursor.execute("INSERT INTO Cliente (nome, telefone, endereco) VALUES (%s, %s, %s)", cliente)

# Inserir dados na tabela Funcionario
for funcionario in funcionarios:
    connection.cursor.execute("INSERT INTO Funcionario (nome, cargo) VALUES (%s, %s)", funcionario)

# Inserir dados na tabela Pagamento
connection.cursor.execute("INSERT INTO Pagamento (valor, tipo_pagamento, data) VALUES (100.00, 'Cartão de crédito', "
                          "'2024-04-17')")
connection.cursor.execute("INSERT INTO Pagamento (valor, tipo_pagamento, data) VALUES (50.00, 'Dinheiro', "
                          "'2024-04-18')")

# Inserir dados na tabela de associação Pagamento_Cliente
connection.cursor.execute("INSERT INTO Pagamento_Cliente (pagamento_id, cliente_id) VALUES (1, 1)")
connection.cursor.execute("INSERT INTO Pagamento_Cliente (pagamento_id, cliente_id) VALUES (2, 2)")

# Finalizar e salvar as alterações
connection.conexao.commit()

# Fechar o cursor e a conexão
connection.cursor.close()
connection.conexao.close()

print("Dados inseridos com sucesso!")
