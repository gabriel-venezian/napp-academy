from Registro import Registro
from datetime import date
import pytest


class TestRegistro:
    def test_class_declared(self):
        objeto = Registro((1, 'produto', 10, 1, '2021-09-01'))
        assert isinstance(objeto, Registro)

    def test_class_declared_fail_data(self):
        msg_erro = "Data não está no formado aaaa-MM-dd"
        with pytest.raises(ValueError) as error:
            tupla_com_dados = (1, 'produto', 10, 1, 'data_errada')
            Registro(tupla_com_dados)
        assert str(error.value) == msg_erro

    def test_class_declared_fail_1(self):
        msg_erro = "Dados inválidos"
        with pytest.raises(ValueError) as error:
            tupla_com_dados = (1, 'produto', 10, 1)
            Registro(tupla_com_dados)
        assert str(error.value) == msg_erro

    def test_class_declared_fail_2(self):
        msg_erro = "Dados inválidos"
        with pytest.raises(ValueError) as error:
            tupla_com_dados = (1, 'produto', 10)
            Registro(tupla_com_dados)
        assert str(error.value) == msg_erro

    def test_class_declared_fail_3(self):
        msg_erro = "Dados inválidos"
        with pytest.raises(ValueError) as error:
            tupla_com_dados = (1, 'produto')
            Registro(tupla_com_dados)
        assert str(error.value) == msg_erro

    def test_class_declared_fail_4(self):
        msg_erro = "Informar a data no formado aaaa-MM-dd"
        with pytest.raises(TypeError) as error:
            tupla_com_dados = (1, 'produto', 10, 1, 20)
            Registro(tupla_com_dados)
        assert str(error.value) == msg_erro

    def test_instanciar(self):
        tupla = (1, 'produto', 10, 1, '2021-09-01')
        objeto = Registro(tupla)
        assert type(objeto._nome), str
        assert type(objeto.produto), str
        assert objeto.produto, 'produto'
        assert type(objeto._criado_em), date
        assert type(objeto.data), date
        assert objeto.data, '2021-09-01'

    def test_str_repr(self):
        tupla = (1, 'produto', 10, 1, '2021-09-01')
        objeto = Registro(tupla)
        assert str(objeto) == 'produto 2021-09-01'
        assert repr(objeto) == 'id:1 => produto data: 2021-09-01  preço:10  quantidade:1'

    def test_properties_setters_1(self):
        tupla = (1, 'produto', 10, 1, '2021-09-01')
        objeto = Registro(tupla)
        assert objeto.produto == 'produto'
        objeto.produto = 'Produto Alterado'
        assert objeto._nome == 'Produto Alterado'
        assert objeto.produto == 'Produto Alterado'

    def test_properties_setters_2(self):
        tupla = (1, 'produto', 10, 1, '2021-09-01')
        objeto = Registro(tupla)
        assert objeto.quantidade == 1
        objeto.quantidade = 20
        assert objeto.quantidade == 20
        assert objeto.preco == 10
        objeto.preco = 21.32
        assert objeto.preco == 21.32

    def test_metodo_Registrodo_no_dia_mes_retorna_True(self):
        tupla = (1, 'produto', 10, 1, '2021-09-01')
        objeto = Registro(tupla)
        assert objeto.comprado_no_dia_mes(1, 9) is True
        assert objeto.comprado_no_dia_mes("1", 9) is True
        assert objeto.comprado_no_dia_mes("1", "9") is True
        assert objeto.comprado_no_dia_mes("01", "09") is True

    def test_metodo_Registrodo_no_dia_mes_retorna_False(self):
        tupla = (1, 'produto', 10, 1, '2021-09-01')
        objeto = Registro(tupla)
        assert objeto.comprado_no_dia_mes(2, 9) is False
        assert objeto.comprado_no_dia_mes("2", 9) is False
        assert objeto.comprado_no_dia_mes("2", "9") is False
        assert objeto.comprado_no_dia_mes("02", "09") is False

    def test_metodo_preco_entre_retorna_True(self):
        tupla = (1, 'produto', 10, 1, '2021-09-01')
        objeto = Registro(tupla)
        assert objeto.preco_entre(9, 11) is True
        assert objeto.preco_entre(10, 11) is True
        assert objeto.preco_entre(9, 10) is True
        assert objeto.preco_entre(10, 10) is True

    def test_metodo_preco_entre_retorna_False(self):
        tupla = (1, 'produto', 20, 1, '2021-09-01')
        objeto = Registro(tupla)
        assert objeto.preco_entre(9, 11) is False
        assert objeto.preco_entre(10, 11) is False
        assert objeto.preco_entre(9, 19.95) is False
        assert objeto.preco_entre(20.01, 200) is False