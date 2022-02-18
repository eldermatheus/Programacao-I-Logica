entrada = input()
codigo_produto = maior_preco = quantidade_produto = 0

# coleta de itens
if entrada[0] == '0':
    print('nao tem compras')
else:
    while entrada[0] != '0':
        codigo_temp,quantidade_temp,preco_temp = entrada.split()
        codigo = int(codigo_temp)
        quantidade = int(quantidade_temp)
        preco = float(preco_temp)

        if preco*quantidade > maior_preco:
            codigo_produto = codigo
            quantidade_produto = quantidade
            maior_preco = preco*quantidade
        entrada = input()

    print('Item mais caro')
    print('Codigo:', codigo_produto)
    print('Quantidade:', quantidade_produto)
    print('Custo', '%.2f' % maior_preco)