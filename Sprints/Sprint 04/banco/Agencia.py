from banco.contas.ContaPessoaFisica import ContaPessoaFisica
from banco.contas.ContaPessoaJuridica import ContaPessoaJuridica
from banco.contas.ContaPoupanca import ContaPoupanca

class Agencia:
    def __init__(self, agencia):
        self.agencia = agencia
        self.clientes = []

    def add_conta_PF(self, nome,cpf, saldo, limite=None):
        cliente = ContaPessoaFisica(nome=nome, cpf=cpf, saldo=saldo, limite=limite)
        self.clientes.append(cliente)

    def add_conta_PJ(self, nome, cnpj, saldo, limite=None):
        cliente = ContaPessoaJuridica(nome=nome, cnpj=cnpj, saldo=saldo, limite=limite)
        self.clientes.append(cliente)

    def add_conta_poupanca(self, nome,cpf, saldo):
        cliente = ContaPoupanca(nome=nome, cpf=cpf, saldo=saldo)
        self.clientes.append(cliente)

    def __str__(self):
        return self.agencia 

    def __repr__(self):
        return  self.agencia