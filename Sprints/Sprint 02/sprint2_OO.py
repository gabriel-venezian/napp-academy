import csv

class Sprint2:
    lista = []
    auxiliar = []
    contador = 0
    def __init__(self):
        pass
        
    def carregar_arquivo_para_lista(self, nome_arquivo):
        lista = []
        self.contador += 1
        with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                lista.append(row)
        lista = lista[1:]
        if nome_arquivo not in self.auxiliar:
            self.auxiliar.append(nome_arquivo)
            self.lista.extend(lista)
        elif nome_arquivo in self.auxiliar and self.contador == 1:
            self.auxiliar = []
            self.lista = []
            self.auxiliar.append(nome_arquivo)
            self.lista.extend(lista)
        return None

    def busca_trecho_nome(self, nome):
        lista = []
        for item in self.lista:
            if nome in item[0]:
                lista.append((item[0], item[1]))
        return lista

    def busca_email(self, email):
        sublista = ()
        for item in self.lista:
            if email in item[2]:
                sublista += tuple(item)
        return sublista

    def busca_estado(self):
        sublista = []
        for item in self.lista:
            if item[7][-2:] not in sublista:
                sublista.append(item[7][-2:])
        return sublista
 
    def busca_mes_vencimento_cartao_credito(self, mes_vencimento):
        sublista = []
        for item in self.lista:
            if str(mes_vencimento) in item[9]:
                sublista.append(tuple(item))
        return sublista

    def busca_prefixo_sufixo_ip(self, prefixo_ip='192', sufixo_ip='0'):
        sublista = []
        for item in self.lista:
            sufixo = item[5].split('.')[3]
            if item[5].startswith(prefixo_ip) and sufixo == sufixo_ip:
                sublista.append(tuple(item)) 
        return sublista

    def contar_ocorrencia_por_dominio_hostname(self, *dominios):
        dicionario = {}
        for dominio in dominios:
            dicionario[dominio] = 0
        for item in self.lista:
            teste = f'{item[4].split(".")[-2]}.{item[4].split(".")[-1]}'
            if teste in dicionario.keys():
                dicionario[teste] += 1
        return list(dicionario.items())
 
    def contar_ocorrencia_por_dominio_email(self, *dominios):
        dicionario = {}
        for dominio in dominios:
            dicionario[dominio] = 0
        for item in self.lista:
                if item[2].split('@')[-1].strip() in dicionario.keys():
                    dicionario[item[2].split('@')[-1].strip()] += 1
        return list(dicionario.items())
 
    def busca_mes_aniversario(self, mes_aniversario):
        sublista = []
        for item in self.lista:
            if item[3].split('-')[1].endswith(str(mes_aniversario)):
                sublista.append(item)
        return sublista
 
    def relatorio_lista_para_txt(self, arquivo, lista):
        with open(arquivo, 'w') as f:
            for registro in lista:
                f.write(40 * '*' + '\n')
                for i in range(len(registro)):
                    f.write(registro[i])
                    f.write('\n')
 
    def relatorio_lista_para_cvs(self, arquivo, lista):
        with open(arquivo, 'w') as f:
            writer = csv.writer(f)
            for registro in lista:
                writer.writerow(registro)
 
if __name__ == "__main__":
    objeto = Sprint2()
    objeto.carregar_arquivo_para_lista('arquivo_1.csv')
    objeto.carregar_arquivo_para_lista('arquivo_2.csv')
    objeto.carregar_arquivo_para_lista('arquivo_3.csv')
