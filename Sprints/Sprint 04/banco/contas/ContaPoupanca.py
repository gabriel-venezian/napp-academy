from banco.contas.Conta import Conta


class ContaPoupanca(Conta):
   """
    Classe representa a conta poupança de pessoa física.
    Saldo padrão da conta: R$ 0,00

    Args:
        Conta (kwargs): Dicionário com dados da conta
    """
   def __init__(self, **kwargs):
      """
        Construtor da classe ContaPoupanca.
        Extrai do dicionário kwargs:
        - Nome
        - Saldo
        - CPF
        """
      self.cpf = kwargs.get('cpf')
      if self.cpf == None:
         raise ValueError('CPF inválido')
      super(ContaPoupanca, self).__init__(**kwargs)         
      self.limite = kwargs.get('limite', 0)


   def saque(self, valor):
      """
      Método para realizar saque.
      Este método suporta somente números maiores que zero.

      Args:
         valor (float ou int): Valor positivo do saque

      Raises:
         ValueError: Erro ocorre quando é informado valor negativo.
         TypeError: Quando o tipo passado não for inteiro ou float.

      Returns:
         Float: Valor do saque realizado.
      """
      erro = 'Valor do saque supera seu saldo.'
      return super().saque(valor, erro)


   def rendimento_aniversario(self, juros: float):
      """
      Calcula o rendimento de juros (em porcentagem)
      baseado no valor em conta (saldo)
      Args:
         juros: porcentagem de juros:
            1 = 100%
            0 = 0%
      """
      if juros >= 0 and juros <= 1:
         self.saldo += self.saldo * juros
      else:
         raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
      

   def __str__(self):
      return "Conta Poupança:" + self.nome + ", saldo=" + str(self.saldo)


   def __repr__(self):
      return  "Conta Poupança:" + self.nome + ", saldo=" + str(self.saldo)          