import csv
from datetime import date, datetime
         
def carregar_arquivo_para_lista(nome_arquivo):
    """
    Função recebe o nome de um arquivo csv e retorna a lista 
    de tuplas com 

    Args:
        nome_arquivo (string): Nome do arquivo CSV

    Returns:
        list: Lista com tuplas
    """
    lista = []
    with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lista.append(tuple(row))
    lista = lista[1:]
    return lista

def carregar_arquivos_para_lista(*lista_arquivos):
    lista = []
    for arquivo in lista_arquivos:
        lista += carregar_arquivo_para_lista(arquivo)
    return lista

def busca_mes_vencimento_cartao_credito(lista, **parametros):
    mes_vencimento = []
    mes = parametros.get('mes','03')
    ano = parametros.get('ano', '23')
    for item in lista:
        if item[-1].startswith(mes) and item[-1].endswith(ano):
            mes_vencimento.append(item)
    return mes_vencimento

def contar_ocorrencias_cartao_credito_por_mes(lista):
    dicionario = {}
    for item in lista:
        mes = item[-1][:2]
        if mes not in dicionario.keys():
           dicionario[mes] = 0
        dicionario[mes] += 1
    return dicionario

def contar_ocorrencias_cartao_credito_por_ano(lista):
    dicionario = {}
    for item in lista:
        ano = item[-1][-2:]
        if ano not in dicionario.keys():
           dicionario[ano] = 0
        dicionario[ano] += 1
    return dicionario

def busca_cvc(lista, cvc='043'):
    lista_registros = []
    for item in lista:
        codigo = item[-2].split('\n')[3][-3:]
        if 'CVC' in item[8] and codigo.endswith(cvc):
            lista_registros.append(item)
    return lista_registros

def busca_lista_cvcs(lista, *cvcs):
    sublista = []
    default = list(cvcs)
    if default == []:
        default.append('043')
    for item in default:
        sublista += busca_cvc(lista, item)
    return sublista

def contar_ocorrencias_por_estado(lista):
    dicionario = {}
    for item in lista:
        estado = item[7].split('/')[-1].strip()
        if estado not in dicionario.keys():
            dicionario[estado] = 0
        dicionario[estado] += 1
    return dicionario   

def busca_dados_navegador(lista, navegador='Chrome/24'):
    sublista = []
    for item in lista:
        if navegador in item[6]:
            sublista.append(item)
    return sublista

def contar_ocorrencias_por_sufixo_dominio(lista):
    dicionario = {}
    for item in lista:
        dominio = item[4].split('.')[-1].strip()
        if dominio not in dicionario.keys():
            dicionario[dominio] = 0
        dicionario[dominio] += 1
    return dicionario

def contar_ocorrencias_por_dominio_email(lista):
    dicionario = {}
    for item in lista:
        dominio = item[2].split('@')[-1].strip()
        if dominio not in dicionario.keys():
            dicionario[dominio] = 0
        dicionario[dominio] += 1
    return dicionario

def buscar_dominio_mais_utilizado(lista):
    dominio = contar_ocorrencias_por_dominio_email(lista)
    valor_maximo = max(dominio, key = dominio.get)
    return ((valor_maximo, dominio[valor_maximo]))

def contar_ocorrencias_por_semana(lista):
    dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    dicionario = {'Segunda':0,'Terça':0,'Quarta':0,'Quinta':0,'Sexta':0,'Sábado':0,'Domingo':0}
    for item in lista:
        data = datetime.strptime(item[3], '%Y-%m-%dT%H:%M:%S')
        dia_semana = date(data.year, data.month, data.day).weekday()
        dicionario[dias[dia_semana]] += 1
    return list(dicionario.items())
        
def contar_ocorrencias_por_hora(lista):
    dicionario = {}
    for item in lista:
        hora = item[3].split(':')[0][-2:]
        if hora not in dicionario.keys():
            dicionario[hora] = 0
        dicionario[hora] += 1
    return dicionario
        

def contar_ocorrencias_por_mes(lista):
    dicionario = {}
    for item in lista:
        mes = item[3].split('-')[1]
        if mes not in dicionario.keys():
            dicionario[mes] = 0
        dicionario[mes] += 1
    return dicionario

if __name__ == "__main__":
    lista = carregar_arquivo_para_lista('arquivo_1.csv')
    carregar_arquivos_para_lista('arquivo_1.csv', 'arquivo_2.csv')
    busca_mes_vencimento_cartao_credito(lista, mes='02', ano='27')
    contar_ocorrencias_cartao_credito_por_mes(lista)
    contar_ocorrencias_cartao_credito_por_ano(lista)
    busca_cvc(lista, cvc='503')
    contar_ocorrencias_por_sufixo_dominio(lista)
    buscar_dominio_mais_utilizado(lista)
    contar_ocorrencias_por_semana(lista)
    contar_ocorrencias_por_hora(lista)
    contar_ocorrencias_por_mes(lista)
