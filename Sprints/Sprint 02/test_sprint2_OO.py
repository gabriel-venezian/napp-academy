from sprint2_OO import Sprint2
from datetime import date
import pytest


class TestSprint2:
    def test_class_declared(self):
        objeto = Sprint2()
        assert isinstance(objeto, Sprint2)

    def test_inner_list_declared(self):
        objeto = Sprint2()
        assert isinstance(objeto.lista, list)

    def test_metodo_carregar_arquivo_para_lista_ok_1(self):
        objeto = Sprint2()
        retorno = objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        assert isinstance(objeto.lista, list)
        assert len(objeto.lista) == 250
        assert retorno is None

    def test_metodo_carregar_arquivo_para_lista_ok_2(self):
        objeto = Sprint2()
        retorno = objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        retorno = objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        assert isinstance(objeto.lista, list)
        assert len(objeto.lista), 500
        assert retorno is None

    def test_metodo_carregar_arquivo_para_lista_ok_3(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        assert isinstance(objeto.lista, list)
        assert len(objeto.lista) == 750

    def test_metodo_carregar_arquivo_para_lista_ok_4(self):
        objeto = Sprint2()
        assert isinstance(objeto, Sprint2)
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        assert len(objeto.lista) == 250
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        assert len(objeto.lista) == 500
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        assert isinstance(objeto.lista, list)
        assert len(objeto.lista) == 500

    def test_metodo_carregar_arquivo_para_lista_fail(self):
        objeto = Sprint2()
        msg = "[Errno 2] No such file or directory: 'none.csv'"
        with pytest.raises(FileNotFoundError) as error:
            objeto.carregar_arquivo_para_lista('none.csv')
        assert str(error.value) == msg

    def test_metodo_busca_trecho_nome_ok_1(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        retorno = objeto.busca_trecho_nome('Silva')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno)== 3
        assert len(retorno[0]) == 2
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_trecho_nome('Silva')
        assert len(retorno)== 6

    def test_metodo_busca_trecho_nome_ok_2(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        retorno = objeto.busca_trecho_nome('Fernandes')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 7
        assert len(retorno[0]) == 2
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_trecho_nome('Fernandes')
        assert len(retorno) == 15
        assert len(retorno[0]) == 2
        retorno = objeto.busca_trecho_nome('Souza')
        assert len(retorno) == 4
        assert len(retorno[0]) == 2

    def test_metodo_busca_trecho_nome_ok_3(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_trecho_nome('Diego')
        assert len(retorno) == 3
        assert len(retorno[0]) == 2
        retorno = objeto.busca_trecho_nome('Cecília')
        assert len(retorno) == 11
        assert len(retorno[0]) == 2

    def test_metodo_busca_email_ok_1(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_email('teixeiraisadora@gmail.com')
        assert isinstance(retorno, tuple)
        assert isinstance(retorno[0], str)
        assert retorno[0] == 'Ana Julia Viana'
        assert retorno[1] == '807.932.546-47'
        assert retorno[5] == '199.172.254.16'
        assert len(retorno)== 10

    def test_metodo_busca_email_ok_2(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_email('wcostela@yahoo.com.br')
        assert isinstance(retorno, tuple)
        assert isinstance(retorno[0], str)
        assert retorno[0] == 'Ana Julia Silveira'
        assert retorno[1] == '196.075.438-66'
        assert retorno[5] == '114.158.140.46'
        assert len(retorno)== 10

    def test_metodo_busca_email_ok_3(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_email('prof.orlando@nappsolutions.com')
        assert isinstance(retorno, tuple)
        assert len(retorno)== 0
        assert retorno == ()

    def test_metodo_busca_estado_ok_1(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        retorno = objeto.busca_estado()
        assert isinstance(retorno, list)
        assert len(retorno)== 27

    def test_metodo_busca_estado_ok_2(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_estado()
        assert isinstance(retorno, list)
        assert len(retorno)== 27

    def test_metodo_busca_mes_vencimento_cartao_credito_ok_1(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_mes_vencimento_cartao_credito('09')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno)== 51
        assert len(retorno[1])== 10

    def test_metodo_busca_mes_vencimento_cartao_credito_ok_2(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_mes_vencimento_cartao_credito('12')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno)== 75
        assert len(retorno[1])== 10

    def test_metodo_busca_mes_vencimento_cartao_credito_ok_3(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_mes_vencimento_cartao_credito('01')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno)== 65
        assert len(retorno[1])== 10

    def test_metodo_busca_prefixo_sufixo_ip_ok_1(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_prefixo_sufixo_ip('132')
        assert len(retorno) == 0
        retorno = objeto.busca_prefixo_sufixo_ip('132', '140')
        assert len(retorno) == 0
        assert isinstance(retorno, list)
        retorno = objeto.busca_prefixo_sufixo_ip('132', '20')
        assert len(retorno) == 0
        retorno = objeto.busca_prefixo_sufixo_ip()
        assert len(retorno) == 0
        assert isinstance(retorno, list)

    def test_metodo_busca_prefixo_sufixo_ip_ok_2(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        retorno = objeto.busca_prefixo_sufixo_ip('126', '173')
        assert len(retorno) == 0
        assert isinstance(retorno, list)
        retorno = objeto.busca_prefixo_sufixo_ip('203', '232')
        assert len(retorno) == 1
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)

    def test_metodo_contar_ocorrencia_por_dominio_hostname_ok_1(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.contar_ocorrencia_por_dominio_hostname('oliveira.com')
        assert len(retorno) == 1
        assert len(retorno[0]) == 2
        assert retorno[0][0] == 'oliveira.com'
        assert retorno[0][1] == 3
        retorno = objeto.contar_ocorrencia_por_dominio_hostname('oliveira')
        assert len(retorno) == 1
        assert len(retorno[0]) == 2
        assert retorno[0][0] == 'oliveira'
        assert retorno[0][1] == 0

    def test_metodo_contar_ocorrencia_por_dominio_hostname_ok_2(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.contar_ocorrencia_por_dominio_hostname('oliveira.com', 'goncalves.com')
        assert len(retorno) == 2
        assert len(retorno[0]) == 2
        assert retorno[0][0] == 'oliveira.com'
        assert retorno[0][1] == 3
        assert retorno[1][0] == 'goncalves.com'
        assert retorno[1][1] == 11


    def test_metodo_contar_ocorrencia_por_dominio_email_ok_1(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.contar_ocorrencia_por_dominio_email('gmail.com')
        assert len(retorno) == 1
        assert len(retorno[0]) == 2
        assert retorno[0][0] == 'gmail.com'
        assert retorno[0][1] == 63
        retorno = objeto.contar_ocorrencia_por_dominio_email('uol.com.br')
        assert len(retorno) == 1
        assert len(retorno[0]) == 2
        assert retorno[0][0] == 'uol.com.br'
        assert retorno[0][1] == 63
        retorno = objeto.contar_ocorrencia_por_dominio_email('araujo.br')
        assert len(retorno) == 1
        assert len(retorno[0]) == 2
        assert retorno[0][0] == 'araujo.br'
        assert retorno[0][1] == 2

    def test_metodo_contar_ocorrencia_por_dominio_email_ok_2(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.contar_ocorrencia_por_dominio_email('gmail.com','uol.com.br', 'uol.com','araujo.br')
        assert len(retorno) == 4
        assert len(retorno[0]) == 2
        assert retorno[0][0] == 'gmail.com'
        assert retorno[0][1] == 63
        assert retorno[1][0] == 'uol.com.br'
        assert retorno[1][1] == 63
        assert retorno[2][0] == 'uol.com'
        assert retorno[2][1] == 0
        assert retorno[3][0] == 'araujo.br'
        assert retorno[3][1] == 2
        
    def test_metodo_busca_mes_aniversario_ok_1(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_mes_aniversario('03')
        assert len(retorno) == 113
        assert len(retorno[0]) == 10
        retorno = objeto.busca_mes_aniversario(3)
        assert len(retorno) == 113
        assert len(retorno[0]) == 10

    def test_metodo_busca_mes_aniversario_ok_2(self):
        objeto = Sprint2()
        objeto.carregar_arquivo_para_lista('arquivo_1.csv')
        objeto.carregar_arquivo_para_lista('arquivo_2.csv')
        objeto.carregar_arquivo_para_lista('arquivo_3.csv')
        retorno = objeto.busca_mes_aniversario('01')
        assert len(retorno) == 96
        assert len(retorno[0]) == 10
        retorno = objeto.busca_mes_aniversario(1)
        assert len(retorno) == 96
        assert len(retorno[0]) == 10
        retorno = objeto.busca_mes_aniversario(10)
        assert len(retorno) == 0
        retorno = objeto.busca_mes_aniversario(12)
        assert len(retorno) == 0