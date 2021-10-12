from banco.Agencia import Agencia

agencia = Agencia('Banco Imobiliário')
agencia.add_conta_PF("Pessoa1", "123", 50, 500)
agencia.add_conta_PF("Pessoa2", "123", 1000, 500)
agencia.add_conta_poupanca("Pessoa3", "123", 1000, 500)
agencia.add_conta_PJ("Empresa XYZ", "123", 1000, 1500)
agencia.add_conta_poupanca("Pessoa4", "123", 1000)
