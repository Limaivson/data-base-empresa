from mysql_connection import Mysql_connection
from Funcionario import Funcionario
from Cliente import Cliente
from Pagamento import Pagamento

con = Mysql_connection()


class Consultas:
    @staticmethod
    def inserir_funcionario(nome, cargo):
        try:
            con.cursor.execute(f"INSERT INTO Funcionario (nome, cargo) VALUES ('{nome}', '{cargo}')")
            con.conexao.commit()
            return True
        except Exception as e:
            print(f'Erro ao inserir funcionário: {e}')
            return False

    @staticmethod
    def listar_funcionarios():
        try:
            con.cursor.execute("SELECT * FROM Funcionario")
            func = con.cursor.fetchall()
            lista_funcionarios = []
            for i in func:
                lista_funcionarios.append(Funcionario(i[0], i[1], i[2]))
            return lista_funcionarios
        except Exception as e:
            print(f'Erro ao listar funcionários: {e}')
            return False

    @staticmethod
    def deletar_funcionario(id_funcionario):
        try:
            con.cursor.execute(f"DELETE FROM Funcionario WHERE id = {id_funcionario}")
            con.conexao.commit()
            return True
        except Exception as e:
            print(f'Erro ao deletar funcionário: {e}')
            return False

    @staticmethod
    def atualizar_funcionario(id_funcionario, nome, cargo):
        try:
            con.cursor.execute(f"UPDATE Funcionario SET nome = '{nome}', cargo = '{cargo}' WHERE id = {id_funcionario}")
            con.conexao.commit()
            return True
        except Exception as e:
            print(f'Erro ao atualizar funcionário: {e}')
            return False

    @staticmethod
    def buscar_funcionario(id_funcionario):
        try:
            con.cursor.execute(f"SELECT * FROM Funcionario WHERE id = {id_funcionario}")
            func = con.cursor.fetchone()
            return Funcionario(func[0], func[1], func[2])
        except Exception as e:
            print(f'Erro ao buscar funcionário: {e}')
            return False

    @staticmethod
    def buscar_funcionario_por_nome(nome):
        try:
            con.cursor.execute(f"SELECT * FROM Funcionario WHERE nome = '{nome}'")
            func = con.cursor.fetchone()
            return Funcionario(func[0], func[1], func[2])
        except Exception as e:
            print(f'Erro ao buscar funcionário: {e}')
            return False

    @staticmethod
    def listar_clientes():
        try:
            con.cursor.execute("SELECT * FROM Cliente")
            cli = con.cursor.fetchall()
            clientes = []
            for i in cli:
                clientes.append(Cliente(i[0], i[1], i[2], i[3]))
            return clientes
        except Exception as e:
            print(f'Erro ao listar clientes: {e}')
            return False

    @staticmethod
    def inserir_cliente(nome, telefone, endereco):
        try:
            con.cursor.execute(f"INSERT INTO Cliente (nome, telefone, endereco) VALUES ('{nome}', '{telefone}', '{endereco}')")
            con.conexao.commit()
            return True
        except Exception as e:
            print(f'Erro ao inserir cliente: {e}')
            return False

    @staticmethod
    def deletar_cliente(id_cliente):
        try:
            con.cursor.execute(f"DELETE FROM Cliente WHERE id = {id_cliente}")
            con.conexao.commit()
            return True
        except Exception as e:
            print(f'Erro ao deletar cliente: {e}')
            return False

    @staticmethod
    def atualizar_cliente(id_cliente, nome, telefone, endereco):
        try:
            con.cursor.execute(f"UPDATE Cliente SET nome = '{nome}', telefone = '{telefone}', endereco = '{endereco}' WHERE id = {id_cliente}")
            con.conexao.commit()
            return True
        except Exception as e:
            print(f'Erro ao atualizar cliente: {e}')
            return False

    @staticmethod
    def buscar_cliente(id_cliente):
        try:
            con.cursor.execute(f"SELECT * FROM Cliente WHERE id = {id_cliente}")
            cli = con.cursor.fetchone()
            return Cliente(cli[0], cli[1], cli[2], cli[3])
        except Exception as e:
            print(f'Erro ao buscar cliente: {e}')
            return False

    @staticmethod
    def buscar_cliente_por_nome(nome):
        try:
            con.cursor.execute(f"SELECT * FROM Cliente WHERE nome = '{nome}'")
            cli = con.cursor.fetchone()
            return Cliente(cli[0], cli[1], cli[2], cli[3])
        except Exception as e:
            print(f'Erro ao buscar cliente: {e}')
            return False

    @staticmethod
    def buscar_cliente_por_endereco(endereco):
        try:
            con.cursor.execute(f"SELECT * FROM Cliente WHERE endereco = '{endereco}'")
            cli = con.cursor.fetchone()
            return Cliente(cli[0], cli[1], cli[2], cli[3])
        except Exception as e:
            print(f'Erro ao buscar cliente: {e}')
            return False

    @staticmethod
    def listar_pagamentos():
        try:
            con.cursor.execute("SELECT * FROM Pagamento")
            pag = con.cursor.fetchall()
            lista_pagamentos = []
            for i in pag:
                lista_pagamentos.append(Pagamento(i[0], i[1], i[2]))
            return lista_pagamentos
        except Exception as e:
            print(f'Erro ao listar pagamentos: {e}')
            return False

    @staticmethod
    def inserir_pagamento(valor, tipo_pagamento, data):
        try:
            con.cursor.execute(f"INSERT INTO Pagamento (valor, tipo_pagamento, data) VALUES ({valor}, '{tipo_pagamento}', '{data}')")
            con.conexao.commit()
            return True
        except Exception as e:
            print(f'Erro ao inserir pagamento: {e}')
            return False

    @staticmethod
    def deletar_pagamento(id_pagamento):
        try:
            con.cursor.execute(f"DELETE FROM Pagamento WHERE id = {id_pagamento}")
            con.conexao.commit()
            return True
        except Exception as e:
            print(f'Erro ao deletar pagamento: {e}')
            return False

    @staticmethod
    def atualizar_pagamento(id_pagamento, valor, tipo_pagamento, data):
        try:
            con.cursor.execute(f"UPDATE Pagamento SET valor = {valor}, tipo_pagamento = '{tipo_pagamento}', data = '{data}' WHERE id = {id_pagamento}")
            con.conexao.commit()
            return True
        except Exception as e:
            print(f'Erro ao atualizar pagamento: {e}')
            return False

    @staticmethod
    def buscar_pagamento(id_pagamento):
        try:
            con.cursor.execute(f"SELECT * FROM Pagamento WHERE id = {id_pagamento}")
            pag = con.cursor.fetchone()
            return Pagamento(pag[0], pag[1], pag[2])
        except Exception as e:
            print(f'Erro ao buscar pagamento: {e}')
            return False
