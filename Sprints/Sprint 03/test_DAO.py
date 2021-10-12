from DAO import DAO
import sqlite3
from sqlite3 import OperationalError
import pytest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "vendas.db")


class TestDAO:
    def test_class_declared(self):
        objeto = DAO(db_path)
        assert isinstance(objeto, DAO)

    def test_class_declared_fail(self):
        msg_erro = "no such table: vendas"
        with pytest.raises(OperationalError) as error:
            DAO('erro.db')
        assert str(error.value) == msg_erro

    def test_instance(self):
        objeto = DAO(db_path)
        assert type(objeto.cursor) == sqlite3.Cursor
        assert type(objeto.conn) == sqlite3.Connection
        assert type(objeto._nome_banco_dados) == str

    def test_str_repr(self):
        objeto = DAO('vendas.db')
        assert str(objeto) == 'vendas.db'
        assert repr(objeto) == 'DAO: vendas.db'

    def test_method_get_todos_registros(self):
        objeto = DAO(db_path)
        lista = objeto.get_registros_todos()
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 796
        assert len(lista[0]) == 5

    def test_method_get_registros_por_produto_1(self):
        objeto = DAO(db_path)
        produto = 'd674bcde198b3bba3e2cecadf00f7a83'
        lista = objeto.get_registros_por_produto(produto)
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 199
        assert len(lista[0]) == 5

    def test_method_get_registros_por_produto_2(self):
        objeto = DAO(db_path)
        produto = '3b84c693178d68d7351bd7c757371924'
        lista = objeto.get_registros_por_produto(produto)
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 199
        assert len(lista[0]) == 5

    def test_method_get_registros_por_data_1(self):
        objeto = DAO(db_path)
        data = '2021-02-21'
        lista = objeto.get_registros_por_data(data)
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 4
        assert len(lista[0]) == 5

    def test_method_get_registros_por_data_2(self):
        objeto = DAO(db_path)
        data = '2021-06-20'
        lista = objeto.get_registros_por_data(data)
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 4
        assert len(lista[0]) == 5

    def test_method_get_registros_quantidade_1(self):
        objeto = DAO(db_path)
        minimo = 20
        maximo = 40
        lista = objeto.get_registros_quantidade(minimo, maximo)
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 75
        assert len(lista[0]) == 5

    def test_method_get_registros_quantidade_2(self):
        objeto = DAO(db_path)
        minimo = 20
        maximo = 50
        lista = objeto.get_registros_quantidade(minimo, maximo)
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 114
        assert len(lista[0]) == 5

    def test_method_get_registros_quantidade_3(self):
        objeto = DAO(db_path)
        minimo = 10
        lista = objeto.get_registros_quantidade(minimo)
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 39
        assert len(lista[0]) == 5

    def test_method_get_registros_quantidade_4(self):
        objeto = DAO(db_path)
        lista = objeto.get_registros_quantidade()
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 76
        assert len(lista[0]) == 5

    def test_method_get_registros_preco_1(self):
        objeto = DAO(db_path)
        minimo = 40
        maximo = 45
        lista = objeto.get_registros_preco(minimo, maximo)
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 12
        assert len(lista[0]) == 5

    def test_method_get_registros_preco_2(self):
        objeto = DAO(db_path)
        minimo = 70
        maximo = 100
        lista = objeto.get_registros_preco(minimo, maximo)
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 63
        assert len(lista[0]) == 5

    def test_method_get_registros_preco_3(self):
        objeto = DAO(db_path)
        minimo = 35
        lista = objeto.get_registros_preco(minimo)
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 9
        assert len(lista[0]) == 5

    def test_method_get_registros_preco_4(self):
        objeto = DAO(db_path)
        lista = objeto.get_registros_preco()
        assert type(lista) == list
        assert type(lista[0]) == tuple
        assert len(lista) == 228
        assert len(lista[0]) == 5
