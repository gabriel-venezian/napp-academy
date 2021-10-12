import sqlite3


class DAO:
    def __init__(self, nome_banco_dados):
        self._nome_banco_dados = nome_banco_dados
        self.conn = sqlite3.connect(self._nome_banco_dados)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM vendas;")

    def get_registros_todos(self):
        lista = []
        sql = "SELECT * FROM vendas;"
        self.cursor.execute(sql)
        for registro in self.cursor.fetchall():
            lista.append(registro)
        return lista

    def get_registros_por_produto(self, produto):
        lista = []
        sql = "SELECT * FROM vendas WHERE produto = '" + produto + "';"
        self.cursor.execute(sql)
        for registro in self.cursor.fetchall():
                lista.append(registro)
        return lista

    def get_registros_por_data(self, data):
        lista = []
        sql = "SELECT * FROM vendas where criado_em = '" + data + "';"
        self.cursor.execute(sql)
        for registro in self.cursor.fetchall():
            lista.append(registro)
        return lista

    def get_registros_quantidade(self, minimo=0, maximo=20):
        lista = []
        sql = "SELECT * FROM vendas where quantidade  > " + str(minimo)
        sql = sql + " AND quantidade < " + str(maximo) + ";"
        self.cursor.execute(sql)
        for registro in self.cursor.fetchall():
            lista.append(registro)
        return lista

    def get_registros_preco(self, minimo=30, maximo=40):
        lista = []
        sql = "SELECT * FROM vendas WHERE preco > " + str(minimo)
        sql = sql + " AND preco < " + str(maximo) + ";"
        self.cursor.execute(sql)
        for registro in self.cursor.fetchall():
            lista.append(registro)
        return lista
    
    def close(self):
        self.conn.close()

    def __str__(self):
        return self._nome_banco_dados

    def __repr__(self):
        return 'DAO: ' + self._nome_banco_dados
