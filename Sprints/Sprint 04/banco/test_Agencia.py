from banco.contas.ContaPoupanca import ContaPoupanca
from banco.contas.ContaPessoaJuridica import ContaPessoaJuridica
from banco.contas.ContaPessoaFisica import ContaPessoaFisica
from banco.contas.Conta import Conta
from banco.Agencia import Agencia
import pytest


class TestAgencia:
    def test_instanciar_objeto(self):
        objeto = Agencia('Banco Forte')
        assert objeto.agencia, 'Banco Forte'
        assert objeto.clientes == []

    def test_str_repr(self):
        objeto = Agencia('Banco Forte')
        msg = 'Banco Forte'
        assert str(objeto) == msg
        assert repr(objeto) == msg

    def test_metodo_add_conta_PF(self):
        objeto = Agencia('Banco Forte')
        objeto.add_conta_PF("Pessoa1", "123", 50, 500)
        assert type(objeto.clientes[0]) == ContaPessoaFisica
        assert len(objeto.clientes) == 1

    def test_metodo_add_conta_PJ(self):
        objeto = Agencia('Banco Forte')
        objeto.add_conta_PJ("Empresa XYZ", "123", 1000, 1500)
        assert type(objeto.clientes[0]) == ContaPessoaJuridica
        assert len(objeto.clientes) == 1
    
    def test_metodo_add_conta_Poupanca(self):
        objeto = Agencia('Banco Forte')
        objeto.add_conta_poupanca("Pessoa1", "123", 1000)
        assert type(objeto.clientes[0]) == ContaPoupanca
        assert len(objeto.clientes) == 1

    def test_metodo_add_conta_PJ_e_PF(self):
        objeto = Agencia('Banco Forte')
        objeto.add_conta_PJ("Empresa XYZ", "123", 1000, 1500)
        objeto.add_conta_PF("Pessoa1", "123", 50, 500)
        assert type(objeto.clientes[0]) == ContaPessoaJuridica
        assert type(objeto.clientes[1]) == ContaPessoaFisica
        assert len(objeto.clientes) == 2

    def test_metodo_add_conta_PJ_PF_Poupanca(self):
        objeto = Agencia('Banco Forte')
        objeto.add_conta_PJ("Empresa XYZ", "123", 1000, 1500)
        objeto.add_conta_PF("Pessoa1", "123", 50, 500)
        objeto.add_conta_poupanca("Pessoa1", "123", 1000)
        assert type(objeto.clientes[0]) == ContaPessoaJuridica
        assert type(objeto.clientes[1]) == ContaPessoaFisica
        assert type(objeto.clientes[2]) == ContaPoupanca
        assert len(objeto.clientes) == 3