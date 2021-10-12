from banco.contas.Conta import Conta
import pytest


class TestConta:
    def test_instanciar_objeto_somente_nome(self):
        objeto = Conta(nome='John Doe')
        assert objeto.nome, 'John Doe'
        assert objeto.saldo == 0
        assert objeto.limite == 500

    def test_instanciar_objeto_nome_saldo(self):
        objeto = Conta(nome='John Doe', saldo=50)
        assert objeto.nome, 'John Doe'
        assert objeto.saldo == 50
        assert objeto.limite == 500

    def test_instanciar_objeto_limite_maior(self):
        objeto = Conta(nome='John Doe',limite=1000)
        assert objeto.nome, 'John Doe'
        assert objeto.saldo == 0
        assert objeto.limite == 1000

    def test_instanciar_objeto_saldo_negativo(self):
        with pytest.raises(ValueError) as error:
            objeto = Conta(nome='John Doe', saldo=-20)
        assert str(error.value) == 'Saldo negativo'
