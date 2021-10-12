from banco.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    """
    Classe representa a conta corrente de pessoa jurídica.
    Limite padrão da conta: R$ 1500,00

    Args:
        Conta (kwargs): Dicionário com dados da conta
    """
    def __init__(self, **kwargs):
        """
        Construtor da classe PessoaJurídica.
        Extrai do dicionário kwargs:
        - Nome
        - Limite
        - Saldo
        - CNPJ
        """
        self.cnpj = kwargs.get('cnpj')
        if self.cnpj == None:
            raise ValueError('CNPJ inválido')
        super(ContaPessoaJuridica, self).__init__(**kwargs)   
        self.limite = kwargs.get('limite', 1500)    


    def __str__(self):
        return "Conta PJ:" + self.nome + ",saldo=" + str(self.saldo)


    def __repr__(self):
        return  "Conta PJ:" + self.nome + ",saldo=" + str(self.saldo)            