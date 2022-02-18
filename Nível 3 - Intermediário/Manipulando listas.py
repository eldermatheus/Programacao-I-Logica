# ---- Fuções ----
def start():
    entrada = input()
    lista = entrada.split()
    for item in range(len(lista)):
        valor = lista[item]
        del lista[item]
        lista.insert(item,int(valor))
    return lista

def inserir(string):
    valor = string.split()
    lista.append(int(valor[1]))
    #print(lista)           # Utilizado para debugging
    
def remover(string):
    valor = string.split()
    lista.remove(int(valor[1]))
    #print(lista)           # Utilizado para debugging

def parcial():
    lista.sort()
    saida = ' '.join(str(item) for item in lista)
    print(saida)



# ---- Programa Principal ----

final = False
lista = start()

while not final:
    entrada = input()
    
    if 'inserir' in entrada:
        inserir(entrada)

    if 'remover' in entrada:
        remover(entrada)    

    if 'parcial' in entrada:
        parcial()

    if 'final' in entrada:
        parcial()
        final += True