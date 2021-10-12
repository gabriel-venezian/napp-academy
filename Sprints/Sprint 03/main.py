from Compras import Compras

compras = Compras('vendas.db')

compras.localizar_compras_no_dia_mes(4, 4)
compras.localizar_compras_por_preco(60, 61)
produto = '3b84c693178d68d7351bd7c757371924'
compras.localizar_compras_por_produto(produto)


compras.gravar_para_arquivo_csv('todos')
