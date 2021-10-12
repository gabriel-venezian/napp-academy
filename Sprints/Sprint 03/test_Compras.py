from Registro import Registro
from Compras import Compras
from sqlite3 import OperationalError
import os
import pytest


class TestCompras:
    def test_class_declared(self):
        objeto = Compras('vendas.db')
        assert isinstance(objeto, Compras)

    def test_instanciar(self):
        objeto = Compras('vendas.db')
        assert isinstance(objeto, Compras)
        assert type(objeto._registros) == list
        assert type(objeto._registros[0]) == Registro
        assert len(objeto._registros) == 796

    def test_instanciar_fail_data(self):
        msg_erro = "no such table: vendas"
        with pytest.raises(OperationalError) as error:
            Compras('erro.db')
        assert str(error.value) == msg_erro

    def test_metodo_localizar_compras_no_dia_mes_1(self):
        objeto = Compras('vendas.db')
        lista = objeto.localizar_compras_no_dia_mes(1, 9)
        assert type(lista) == list
        assert len(lista) == 4
        assert type(lista[0]) == Registro

    def test_metodo_localizar_compras_no_dia_mes_2(self):
        objeto = Compras('vendas.db')
        lista = objeto.localizar_compras_no_dia_mes(5, 12)
        assert type(lista) == list
        assert len(lista) == 0

    def test_metodo_localizar_compras_por_produto_1(self):
        objeto = Compras('vendas.db')
        produto_procurado = 'd674bcde198b3bba3e2cecadf00f7a83'
        lista = objeto.localizar_compras_por_produto(produto_procurado)
        assert type(lista) == list
        assert len(lista) == 199
        assert type(lista[0]) == Registro

    def test_metodo_localizar_compras_por_produto_2(self):
        objeto = Compras('vendas.db')
        produto_procurado = 'd674bcde198b3bba3e2cecadf00'
        lista = objeto.localizar_compras_por_produto(produto_procurado)
        assert type(lista) == list
        assert len(lista) == 0

    def test_metodo_localizar_compras_por_produto_3(self):
        objeto = Compras('vendas.db')
        produto_procurado = 'nenhum_produto_na_base'
        lista = objeto.localizar_compras_por_produto(produto_procurado)
        assert type(lista) == list
        assert len(lista) == 0

    def test_metodo_localizar_compras_por_preco_1(self):
        objeto = Compras('vendas.db')
        preco_minimo = 40
        preco_maximo = 45
        lista = objeto.localizar_compras_por_preco(preco_minimo, preco_maximo)
        assert type(lista) == list
        assert len(lista) == 12
        assert type(lista[0]) == Registro

    def test_metodo_localizar_compras_por_preco_2(self):
        objeto = Compras('vendas.db')
        preco_minimo = 35
        preco_maximo = 50
        lista = objeto.localizar_compras_por_preco(preco_minimo, preco_maximo)
        assert type(lista) == list
        assert len(lista) == 27
        assert type(lista[0]) == Registro

    def test_str_repr(self):
        objeto = Compras('vendas.db')
        msg = 'Lista de compras extraída do banco de dados vendas.db'
        assert str(objeto) == msg
        assert repr(objeto) == msg
