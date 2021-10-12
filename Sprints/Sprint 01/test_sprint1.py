from sprint1 import prefixo_dr_dra, total_prefixo_dr_dra
from sprint1 import prefixo_dra,total_prefixo_dra
from sprint1 import prefixo_dr, total_prefixo_dr
from sprint1 import busca_sobrenomes, busca_sobrenomes_primeiros
from sprint1 import busca_sobrenomes_ultimos
from sprint1 import busca_email, busca_email_por_dominio, busca_email_por_usuario
from sprint1 import busca_endereco, busca_estado
from sprint1 import busca_cartao_credito, busca_vencimento_cartao_credito
from sprint1 import busca_mes_vencimento_cartao_credito
from sprint1 import busca_ip, busca_prefixo_ip, busca_prefixo_sufixo_ip
import pickle
import pytest

class LoadData:
    def load_list(self):
        with open('lista.bin', 'rb') as list_in_file:
            self.lista = pickle.load(list_in_file)

 
class TestPrefixoDrDra(LoadData):
    def test_prefixo_dr_dra(self):
        self.load_list()
        sublista = prefixo_dr_dra(self.lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 329

    def test_total_prefixo_dr_dra(self):
        self.load_list()
        total = total_prefixo_dr_dra(self.lista)
        assert isinstance(total, int)
        assert total == 329


class TestPrefixoDra(LoadData):
    def test_prefixo_dra(self):
        self.load_list()
        sublista = prefixo_dra(self.lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], str)
        assert sublista[0] == 'Dra. Eduarda Aragão'
        assert sublista[1] == 'Dra. Pietra Azevedo'
        assert sublista[2] == 'Dra. Gabriela da Conceição'
        assert len(sublista) == 128

    def test_total_prefixo_dra(self):
        self.load_list()
        total = total_prefixo_dra(self.lista)
        assert isinstance(total, int)
        assert total == 128


class TestPrefixoDr(LoadData):
    def test_prefixo_dr(self):
        self.load_list()
        sublista = prefixo_dr(self.lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], str)
        assert sublista[0] == 'Dr. Miguel Azevedo'
        assert sublista[1] == 'Dr. Nicolas Fernandes'
        assert sublista[2] == 'Dr. João Araújo'
        assert len(sublista) == 201

    def test_total_prefixo_dr(self):
        self.load_list()
        total = total_prefixo_dr(self.lista)
        assert isinstance(total, int)
        assert total == 201


class TestBuscaSobrenomes(LoadData):
    def test_busca_sobrenomes(self):
        self.load_list()
        sublista = busca_sobrenomes(self.lista, 'Silva')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 62
        assert len(sublista[0]) == 2
        sublista = busca_sobrenomes(self.lista, 'Fogaça')
        assert len(sublista) == 56
        assert len(sublista[0]) == 2

    def test_busca_sobrenomes_primeiros(self):
        self.load_list()
        sublista = busca_sobrenomes_primeiros(self.lista, 'Silva')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 10
        assert len(sublista[0]) == 2
        assert sublista[0][0] == 'Larissa Silva'
        assert sublista[0][1] == '013.976.852-12'
        assert sublista[1][0] == 'João Guilherme Silva'
        assert sublista[1][1] == '079.138.645-75'
        sublista = busca_sobrenomes_primeiros(self.lista, 'Fogaça')
        assert len(sublista) == 10
        assert len(sublista[0]) == 2
        assert sublista[0][0] == 'Sra. Beatriz Fogaça'
        assert sublista[0][1] == '350.418.926-60'
        assert sublista[1][0] == 'Juan Fogaça'
        assert sublista[1][1] == '789.365.140-75'

    def test_busca_sobrenomes_ultimos(self):
        self.load_list()
        sublista = busca_sobrenomes_ultimos(self.lista, 'Silva')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 10
        assert len(sublista[0]) == 2
        assert sublista[0][0] == 'Sophie Silva'
        assert sublista[0][1] == '429.835.610-89'
        assert sublista[1][0] == 'Laura Silva'
        assert sublista[1][1] == '309.768.145-01'
        sublista = busca_sobrenomes_ultimos(self.lista, 'Fogaça')
        assert len(sublista) == 10
        assert len(sublista[0]) == 2
        assert sublista[0][0] == 'Caio Fogaça'
        assert sublista[0][1] == '256.019.483-05'
        assert sublista[1][0] == 'Srta. Maysa Fogaça'
        assert sublista[1][1] == '526.790.183-03'


class TestBuscaEmail(LoadData):
    def test_busca_email(self):
        self.load_list()
        tupla_com_dados = busca_email(self.lista, 'pintoluiz-fernando@bol.com.br')
        assert isinstance(tupla_com_dados, tuple)
        assert isinstance(tupla_com_dados[0], str)
        assert len(tupla_com_dados) == 10
        assert tupla_com_dados[0] == 'Rodrigo Moraes'
        assert tupla_com_dados[2] == 'pintoluiz-fernando@bol.com.br'
        assert tupla_com_dados[4] == 'web-98.porto.com'
        tupla_vazia = busca_email(self.lista, 'xyz@gmail.com')
        assert isinstance(tupla_vazia, tuple)
        assert tupla_vazia == ()

    def test_busca_email_por_dominio(self):
        self.load_list()
        lista_com_dados = busca_email_por_dominio(self.lista, 'bol.com.br')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 432
        assert lista_com_dados[0][0] == 'Dra. Eduarda Aragão'
        assert lista_com_dados[0][2] == 'xpires@bol.com.br'
        assert lista_com_dados[0][4] == 'web-72.santos.org'
        lista_com_dados = busca_email_por_dominio(self.lista)
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 413
        lista_vazia = busca_email_por_dominio(self.lista, 'xyz.com.br')
        assert isinstance(lista_vazia, list)
        assert lista_vazia == []

    def test_busca_email_por_usuario(self):
        self.load_list()
        lista_com_dados = busca_email_por_usuario(self.lista, 'thiagoda-paz')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 1
        assert lista_com_dados[0][0] == 'Sr. Renan Barros'
        assert lista_com_dados[0][2] == 'thiagoda-paz@hotmail.com'
        assert lista_com_dados[0][4] == 'db-78.da.com'
        lista_vazia = busca_email_por_usuario(self.lista, 'orlandosaraivajr')
        assert isinstance(lista_vazia, list)
        assert lista_vazia == []


class TestBuscaEndereco(LoadData):
    def test_busca_endereco(self):
        self.load_list()
        lista_com_dados = busca_endereco(self.lista, 'Pátio de Lopes')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 1
        assert lista_com_dados[0][0] == 'Sr. Lucas Nogueira'
        assert lista_com_dados[0][2] == 'zpires@teixeira.com'
        assert lista_com_dados[0][4] == 'laptop-25.vieira.com'
        lista_vazia = busca_endereco(self.lista, 'Pátio de Lopes xxxx')
        assert isinstance(lista_vazia, list)
        assert lista_vazia == []

    def test_busca_estado(self):
        self.load_list()
        lista_com_dados = busca_estado(self.lista)
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], str)
        assert len(lista_com_dados) == 27
        assert 'SP' in lista_com_dados


class TestBuscaCartao(LoadData):
    def test_busca_cartao_credito(self):
        self.load_list()
        lista_com_dados = busca_cartao_credito(self.lista, '12390')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 1
        assert lista_com_dados[0][0] == 'Dra. Evelyn Ferreira'
        assert lista_com_dados[0][2] == 'maria-sophia00@ig.com.br'
        lista_com_dados = busca_cartao_credito(self.lista, '123901213')
        assert isinstance(lista_com_dados, list)
        assert len(lista_com_dados) == 0

    def test_busca_vencimento_cartao_credito(self):
        self.load_list()
        lista_com_dados = busca_vencimento_cartao_credito(self.lista, '03/25')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 42
        lista_com_dados = busca_vencimento_cartao_credito(self.lista, '08/22')
        assert len(lista_com_dados) == 34
        lista_com_dados = busca_vencimento_cartao_credito(self.lista, '07/24')
        assert len(lista_com_dados) == 47

    def test_busca_mes_vencimento_cartao_credito(self):
        self.load_list()
        lista_com_dados = busca_mes_vencimento_cartao_credito(self.lista, '03')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 394
        lista_com_dados = busca_mes_vencimento_cartao_credito(self.lista, 3)
        assert len(lista_com_dados) == 394
        lista_com_dados = busca_mes_vencimento_cartao_credito(self.lista, '3')
        assert len(lista_com_dados) == 394
        lista_com_dados = busca_mes_vencimento_cartao_credito(self.lista, '08')
        assert len(lista_com_dados) == 439
        lista_com_dados = busca_mes_vencimento_cartao_credito(self.lista, '8')
        assert len(lista_com_dados) == 439
        lista_com_dados = busca_mes_vencimento_cartao_credito(self.lista, 8)
        assert len(lista_com_dados) == 439


class TestBuscaIP(LoadData):
    def test_busca_IP(self):
        self.load_list()
        lista_com_dados = busca_ip(self.lista, '196.14.132.233')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 1
        assert lista_com_dados[0][0] == 'Bruna da Luz'
        assert lista_com_dados[0][2] == 'ferreirabryan@yahoo.com.br'
        lista_com_dados = busca_ip(self.lista, '163.122.148.57')
        assert len(lista_com_dados) == 1
        lista_com_dados = busca_ip(self.lista, '192.168.0.1')
        assert len(lista_com_dados) == 0

    def test_busca_prefixo_IP(self):
        self.load_list()
        lista_com_dados = busca_prefixo_ip(self.lista, '163')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 23
        assert len(lista_com_dados[0]) == 10
        lista_com_dados = busca_prefixo_ip(self.lista)
        assert len(lista_com_dados) == 30
        assert len(lista_com_dados[0]) == 10
        lista_com_dados = busca_prefixo_ip(self.lista, '143')
        assert len(lista_com_dados) == 32
        assert len(lista_com_dados[0]) == 10

    def test_busca_prefixo_sufixo_IP(self):
        self.load_list()
        lista_com_dados = busca_prefixo_sufixo_ip(self.lista, '132')
        assert len(lista_com_dados) == 0
        lista_com_dados = busca_prefixo_sufixo_ip(self.lista, '132', '140')
        assert len(lista_com_dados) == 1
        assert len(lista_com_dados[0]) == 10
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        lista_com_dados = busca_prefixo_sufixo_ip(self.lista, '132', '20')
        assert len(lista_com_dados) == 1
        assert len(lista_com_dados[0]) == 10
        lista_com_dados = busca_prefixo_sufixo_ip(self.lista)
        assert len(lista_com_dados) == 0
