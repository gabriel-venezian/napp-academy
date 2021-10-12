import pickle 
         
def prefixo_dr_dra(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DR'):
            sublista.append(item)
    return sublista

def total_prefixo_dr_dra(lista):
    total = 0
    for item in lista:
        if item[0].upper().startswith('DR'):
            total += 1
    return total

def prefixo_dra(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DRA'):
            sublista.append(item[0])
    return sublista

def total_prefixo_dra(lista):
    total = 0
    for item in lista:
        if item[0].upper().startswith('DRA'):
            total += 1
    return total

def prefixo_dr(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DR.'):
            sublista.append(item[0])
    return sublista

def total_prefixo_dr(lista):
    total = 0
    for item in lista:
        if item[0].upper().startswith('DR.'):
            total += 1
    return total

def busca_sobrenomes(lista, sobrenome):
    sublista = []
    for item in lista:
        if item[0].endswith(sobrenome):
            sublista.append(item[:2])
    return sublista

def busca_sobrenomes_primeiros(lista, sobrenome):
    sublista = []
    for item in lista:
        if item[0].endswith(sobrenome):
            sublista.append(item[:2])
    return sublista[:10]

def busca_sobrenomes_ultimos(lista, sobrenome):
    sublista = []
    for item in lista:
        if item[0].endswith(sobrenome):
            sublista.append(item[:2])
    return sublista[-10:]

def busca_email(lista, email):
    tupla = ()
    for item in lista:
        if item[2].startswith(email):
            tupla = item
    return tupla

def busca_email_por_dominio(lista, dominio='gmail.com'):
    sublista = []
    for item in lista:
        if item[2].endswith(dominio):
            sublista.append(item)
    return sublista

def busca_email_por_usuario(lista, username):
    sublista = []
    for item in lista:
        if item[2].startswith(username):
            sublista.append(item)
    return sublista

def busca_endereco(lista, endereco):
    sublista = []
    for item in lista:
        if item[7].startswith(endereco):
            sublista.append(item)
    return sublista

def busca_estado(lista):
    sublista = []
    for item in lista:
        if item[7][-2:] not in sublista:
            sublista.append(item[7][-2:])
    return sublista

def busca_cartao_credito(lista, numero_cartao_procurado):
    sublista = []
    for item in lista:
        numeroCartao = item[8].split('\n')
        if numero_cartao_procurado in numeroCartao[2]:
            sublista.append(item)
    return sublista

def busca_vencimento_cartao_credito(lista, mes_ano_vencimento):
    sublista = []
    for item in lista:
        if mes_ano_vencimento in item[9]: 
            sublista.append(item)
    return sublista

def busca_mes_vencimento_cartao_credito(lista, mes_vencimento):
    sublista = []
    for item in lista:
        if str(mes_vencimento) in item[9][:2]:
            sublista.append(item)
    return sublista

def busca_ip(lista, ip_procurado):
    sublista  = []
    for item in lista:
        if item[5] in ip_procurado:
            sublista.append(item)
    return sublista

def busca_prefixo_ip(lista, prefixo_ip='192'):
    sublista = []
    for item in lista:
        if item[5].startswith(prefixo_ip):
            sublista.append(item)
    return sublista

def busca_prefixo_sufixo_ip(lista, prefixo_ip='192', sufixo_ip='0'):
    sublista = []
    for item in lista:
        sufixo = item[5].split('.')[3]
        if item[5].startswith(prefixo_ip) and sufixo == sufixo_ip:
            sublista.append(item) 
    return sublista

if __name__ == "__main__":
    with open('lista.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)
    prefixo_dr_dra(lista)
