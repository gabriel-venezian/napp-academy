from sprint2 import carregar_arquivo_para_lista
from sprint2 import carregar_arquivos_para_lista
from sprint2 import busca_mes_vencimento_cartao_credito
from sprint2 import contar_ocorrencias_cartao_credito_por_mes
from sprint2 import contar_ocorrencias_cartao_credito_por_ano
from sprint2 import busca_cvc
from sprint2 import busca_lista_cvcs
from sprint2 import contar_ocorrencias_por_estado
from sprint2 import busca_dados_navegador
from sprint2 import contar_ocorrencias_por_sufixo_dominio
from sprint2 import contar_ocorrencias_por_dominio_email
from sprint2 import buscar_dominio_mais_utilizado
from sprint2 import contar_ocorrencias_por_semana
from sprint2 import contar_ocorrencias_por_hora
from sprint2 import contar_ocorrencias_por_mes
import csv
import pytest


class TestCarregarArquivo:
    def test_carregar_arquivo_para_lista(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        assert isinstance(lista, list)
        assert isinstance(lista[0], tuple)
        assert isinstance(lista[0][0], str)
        assert len(lista) == 250
        assert len(lista[0]) == 10

    def test_carregar_arquivo_para_lista_sem_arquivos(self):
        msg = "[Errno 2] No such file or directory: 'none.csv'"
        with pytest.raises(FileNotFoundError) as error:
            lista = carregar_arquivo_para_lista('none.csv')
        assert str(error.value) == msg


class TestCarregarArquivos:
    def test_carregar_arquivos_para_lista_um_arquivo(self):
        lista = carregar_arquivos_para_lista('arquivo_1.csv')
        assert isinstance(lista, list)
        assert isinstance(lista[0], tuple)
        assert isinstance(lista[0][0], str)
        assert len(lista) == 250
        assert len(lista[0]) == 10

    def test_carregar_arquivos_para_lista_dois_arquivos(self):
        lista = carregar_arquivos_para_lista('arquivo_1.csv', 'arquivo_2.csv')
        assert isinstance(lista, list)
        assert isinstance(lista[0], tuple)
        assert isinstance(lista[0][0], str)
        assert len(lista) == 500
        assert len(lista[0]) == 10

    def test_carregar_arquivos_para_lista_tres_arquivos(self):
        lista = carregar_arquivos_para_lista('arquivo_1.csv', 'arquivo_2.csv', 'arquivo_3.csv')
        assert isinstance(lista, list)
        assert isinstance(lista[0], tuple)
        assert isinstance(lista[0][0], str)
        assert len(lista) == 750
        assert len(lista[0]) == 10

    def test_carregar_arquivo_para_lista_faltando_um_arquivo(self):
        msg = "[Errno 2] No such file or directory: 'none.csv'"
        with pytest.raises(FileNotFoundError) as error:
            lista = carregar_arquivos_para_lista('arquivo_1.csv', 'none.csv')
        assert str(error.value) == msg


class TestBuscaCartaoCreditoMesCartao:
    def test_busca_mes_vencimento_cartao_credito_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_mes_vencimento_cartao_credito(lista, mes='02', ano='27')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert isinstance(sublista[0][0], str)
        assert len(sublista) == 3
        assert len(lista[0]) == 10
        sublista = busca_mes_vencimento_cartao_credito(lista, mes='06', ano='28')
        assert len(sublista) == 4
        assert len(lista[0]) == 10
        sublista = busca_mes_vencimento_cartao_credito(lista, ano='23')
        assert len(sublista) == 4
        assert len(lista[0]) == 10
        sublista = busca_mes_vencimento_cartao_credito(lista, mes='09')
        assert len(sublista) == 3
        assert len(lista[0]) == 10
        sublista = busca_mes_vencimento_cartao_credito(lista)
        assert len(sublista) == 4
        assert len(lista[0]) == 10

    def test_busca_mes_vencimento_cartao_credito_2(self):
        lista = carregar_arquivo_para_lista('arquivo_2.csv')
        sublista = busca_mes_vencimento_cartao_credito(lista, mes='02', ano='27')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert isinstance(sublista[0][0], str)
        assert len(sublista) == 2
        assert len(lista[0]) == 10
        sublista = busca_mes_vencimento_cartao_credito(lista, mes='06', ano='28')
        assert len(sublista) == 1
        assert len(lista[0]) == 10
        sublista = busca_mes_vencimento_cartao_credito(lista, ano='23')
        assert len(sublista) == 1
        assert len(lista[0]) == 10
        sublista = busca_mes_vencimento_cartao_credito(lista, mes='09')
        assert len(sublista) == 0
        sublista = busca_mes_vencimento_cartao_credito(lista)
        assert len(sublista) == 1
        assert len(lista[0]) == 10

class TestContaCartaoCreditoOcorrenciaMes:
    def test_contar_ocorrencias_por_mes_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        dicionario = contar_ocorrencias_cartao_credito_por_mes(lista)
        assert len(dicionario) == 12
        assert isinstance(dicionario, dict)
        assert dicionario['01'] == 28
        assert dicionario['02'] == 12
        assert dicionario['03'] == 20
        assert dicionario['04'] == 21
        assert dicionario['05'] == 19
        assert dicionario['06'] == 17
        assert dicionario['07'] == 26
        assert dicionario['08'] == 19
        assert dicionario['09'] == 22
        assert dicionario['10'] == 24
        assert dicionario['11'] == 23
        assert dicionario['12'] == 19

    def test_contar_ocorrencias_por_mes_2(self):
        lista = carregar_arquivo_para_lista('arquivo_2.csv')
        dicionario = contar_ocorrencias_cartao_credito_por_mes(lista)
        assert isinstance(dicionario, dict)
        assert len(dicionario) == 12
        assert dicionario['01'] == 19
        assert dicionario['02'] == 19
        assert dicionario['03'] == 16
        assert dicionario['04'] == 29
        assert dicionario['05'] == 17
        assert dicionario['06'] == 17
        assert dicionario['07'] == 24
        assert dicionario['08'] == 23
        assert dicionario['09'] == 16
        assert dicionario['10'] == 15
        assert dicionario['11'] == 22
        assert dicionario['12'] == 33


class TestContaCartaoCreditoOcorrenciaAno:
    def test_contar_ocorrencias_por_ano(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        dicionario = contar_ocorrencias_cartao_credito_por_ano(lista)
        assert len(dicionario) == 11
        assert isinstance(dicionario, dict)
        assert dicionario['21'] == 2
        assert dicionario['22'] == 27
        assert dicionario['23'] == 24
        assert dicionario['24'] == 31
        assert dicionario['25'] == 23
        assert dicionario['26'] == 27
        assert dicionario['27'] == 32
        assert dicionario['28'] == 23
        assert dicionario['29'] == 24
        assert dicionario['30'] == 26
        assert dicionario['31'] == 11

    def test_contar_ocorrencias_por_ano2(self):
        lista = carregar_arquivo_para_lista('arquivo_2.csv')
        dicionario = contar_ocorrencias_cartao_credito_por_ano(lista)
        assert isinstance(dicionario, dict)
        assert len(dicionario) == 11
        assert dicionario['21'] == 8
        assert dicionario['22'] == 20
        assert dicionario['23'] == 36
        assert dicionario['24'] == 27
        assert dicionario['25'] == 21
        assert dicionario['26'] == 15
        assert dicionario['27'] == 30
        assert dicionario['28'] == 28
        assert dicionario['29'] == 18
        assert dicionario['30'] == 27
        assert dicionario['31'] == 20

class TestBuscaCVC:
    def test_busca_cvc_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_cvc(lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1
        assert sublista[0][0] == 'Murilo Fogaça'
        assert sublista[0][9] == '01/30'

    def test_busca_cvc_2(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_cvc(lista, '503')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1
        assert sublista[0][0] == 'Matheus Costela'
        assert sublista[0][9] == '06/30'

    def test_busca_cvc_3(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_cvc(lista, cvc='226')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 2
        assert sublista[0][0] == 'Giovanna Azevedo'
        assert sublista[0][9] == '06/27'
        assert sublista[1][0] == 'Raul Martins'
        assert sublista[1][9] == '10/26'

class TestBuscaListaCVCs:
    def test_busca_lista_cvcs_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_lista_cvcs(lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1
        assert sublista[0][0] == 'Murilo Fogaça'
        assert sublista[0][9] == '01/30'

    def test_busca_lista_cvcs_2(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_lista_cvcs(lista, '503')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1
        assert sublista[0][0] == 'Matheus Costela'
        assert sublista[0][9] == '06/30'

    def test_busca_lista_cvcs_3(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_lista_cvcs(lista, '503', '226')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 3

    def test_busca_lista_cvcs_4(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_lista_cvcs(lista, '503', '226','428')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 5

class TestContaOcorrenciaEstado:
    def test_contar_ocorrencias_por_estado_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        dicionario = contar_ocorrencias_por_estado(lista)
        assert len(dicionario) == 27
        assert isinstance(dicionario, dict)
        assert dicionario['SP'] == 5
        assert dicionario['MG'] == 10
        assert dicionario['RJ'] == 16

    def test_contar_ocorrencias_por_estado_2(self):
        lista = carregar_arquivo_para_lista('arquivo_2.csv')
        dicionario = contar_ocorrencias_por_estado(lista)
        assert isinstance(dicionario, dict)
        assert len(dicionario) == 27
        assert isinstance(dicionario, dict)
        assert dicionario['SP'] == 10
        assert dicionario['MG'] == 12
        assert dicionario['RJ'] == 8

class TestBuscaDadosNavegador:
    def test_busca_dados_navegador_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_dados_navegador(lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 7
        assert sublista[0][0] == 'João Lucas Carvalho'

    def test_busca_dados_navegador_2(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_dados_navegador(lista, 'Android')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 38
        assert sublista[0][0] == 'Agatha Ramos'

    def test_busca_dados_navegador_3(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = busca_dados_navegador(lista, navegador='X11')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 44
        assert sublista[0][0] == 'Sophie da Mata'

class TestContaOcorrenciaSufixoDominio:
    def test_contar_ocorrencias_por_estado(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        dicionario = contar_ocorrencias_por_sufixo_dominio(lista)
        assert len(dicionario) == 4
        assert isinstance(dicionario, dict)
        assert dicionario['com'] == 86
        assert dicionario['br'] == 94
        assert dicionario['org'] == 34
        assert dicionario['net'] == 36

    def test_contar_ocorrencias_por_estado_2(self):
        lista = carregar_arquivo_para_lista('arquivo_2.csv')
        dicionario = contar_ocorrencias_por_sufixo_dominio(lista)
        assert isinstance(dicionario, dict)
        assert len(dicionario) == 4
        assert isinstance(dicionario, dict)
        assert dicionario['com'] == 94
        assert dicionario['br'] == 96
        assert dicionario['org'] == 32
        assert dicionario['net'] == 28

class TestContarOcorrenciaPorDominioEmail:
    def test_contar_ocorrencia_por_dominio_email_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        dicionario = contar_ocorrencias_por_dominio_email(lista)
        assert isinstance(dicionario, dict)
        assert len(dicionario) == 94
        assert dicionario['vieira.org'] == 1
        assert dicionario['bol.com.br'] == 24
        assert dicionario['costa.com'] == 2

class TestBuscaDominioMaisUtilizado:
    def test_busca_dominio_mais_utilizado_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        tupla = buscar_dominio_mais_utilizado(lista)
        assert isinstance(tupla, tuple)
        assert len(tupla) == 2
        assert tupla[0] == 'ig.com.br'
        assert tupla[1] == 27

    def test_busca_dominio_mais_utilizado_2(self):
        lista = carregar_arquivo_para_lista('arquivo_2.csv')
        tupla = buscar_dominio_mais_utilizado(lista)
        assert isinstance(tupla, tuple)
        assert len(tupla) == 2
        assert tupla[0] == 'hotmail.com'
        assert tupla[1] == 25

class TestContarOcorrenciaPorSemana:
    def test_busca_ocorrencia_por_semana_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        sublista = contar_ocorrencias_por_semana(lista)
        assert isinstance(sublista, list)
        assert len(sublista) == 7
        assert sublista[0][0] == 'Segunda'
        assert sublista[0][1] == 40
        assert sublista[1][0] == 'Terça'
        assert sublista[1][1] == 28
        assert sublista[2][0] == 'Quarta'
        assert sublista[2][1] == 37
        assert sublista[3][0] == 'Quinta'
        assert sublista[3][1] == 26
        assert sublista[4][0] == 'Sexta'
        assert sublista[4][1] == 44
        assert sublista[5][0] == 'Sábado'
        assert sublista[5][1] == 37
        assert sublista[6][0] == 'Domingo'
        assert sublista[6][1] == 38

    def test_busca_ocorrencia_por_semana_2(self):
        lista = carregar_arquivo_para_lista('arquivo_2.csv')
        sublista = contar_ocorrencias_por_semana(lista)
        assert isinstance(sublista, list)
        assert len(sublista) == 7
        assert sublista[0][0] == 'Segunda'
        assert sublista[0][1] == 35
        assert sublista[1][0] == 'Terça'
        assert sublista[1][1] == 44
        assert sublista[2][0] == 'Quarta'
        assert sublista[2][1] == 28
        assert sublista[3][0] == 'Quinta'
        assert sublista[3][1] == 33
        assert sublista[4][0] == 'Sexta'
        assert sublista[4][1] == 41
        assert sublista[5][0] == 'Sábado'
        assert sublista[5][1] == 35
        assert sublista[6][0] == 'Domingo'
        assert sublista[6][1] == 34

class TestContaOcorrenciaHora:
    def test_contar_ocorrencias_por_hora_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        dicionario = contar_ocorrencias_por_hora(lista)
        assert len(dicionario) == 24
        assert isinstance(dicionario, dict)
        assert dicionario['02'] == 11
        assert dicionario['04'] == 7
        assert dicionario['06'] == 21

    def test_contar_ocorrencias_por_hora_2(self):
        lista = carregar_arquivo_para_lista('arquivo_2.csv')
        dicionario = contar_ocorrencias_por_hora(lista)
        assert isinstance(dicionario, dict)
        assert len(dicionario) == 24
        assert dicionario['02'] == 8
        assert dicionario['04'] == 12
        assert dicionario['06'] == 12

class TestContaOcorrenciaMes:
    def test_contar_ocorrencias_por_mes_1(self):
        lista = carregar_arquivo_para_lista('arquivo_1.csv')
        dicionario = contar_ocorrencias_por_mes(lista)
        assert len(dicionario) == 8
        assert isinstance(dicionario, dict)
        assert dicionario['02'] == 31
        assert dicionario['04'] == 36
        assert dicionario['06'] == 30

    def test_contar_ocorrencias_por_mes_2(self):
        lista = carregar_arquivo_para_lista('arquivo_2.csv')
        dicionario = contar_ocorrencias_por_mes(lista)
        assert isinstance(dicionario, dict)
        assert len(dicionario) == 8
        assert dicionario['02'] == 38
        assert dicionario['04'] == 36
        assert dicionario['06'] == 27