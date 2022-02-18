def sequencia_fibonaci():
    """ sequencia fibonnaci com 47 termos """
    anterior = 1
    sucessor = 2
    somaAS = 0
    fibonnaci = [0,1,1,2]

    n = 0
    while n <= 47:

        somaAS = anterior + sucessor
        anterior = sucessor
        sucessor = somaAS

        fibonnaci.append(somaAS)
        n += 1
    
    return fibonnaci

entradas_usuario = []
count = 0
while True:
    entradas_usuario.append(int(input()))
    if entradas_usuario[count] == 0:
        break
    count += 1

"""
para cada entrada do usuario, imprimir os valores da sequencia,
de 0 ate o valor do elemento da lista de entrada.
"""
for x in entradas_usuario:
    for y in range(0,x):
        if y == x-1:
            print(sequencia_fibonaci()[y],end='')
        else:
            print(sequencia_fibonaci()[y],end=' ')
    print()